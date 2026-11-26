/**
 * prices.js — Vercel serverless function (Node.js, CommonJS, no dependencies).
 *
 * GET /api/prices?asins=ASIN1,ASIN2  (comma-separated, max 10 per request;
 * extras are ignored)
 *
 * Returns live Amazon.ca prices for the requested ASINs via the Amazon
 * Product Advertising API 5.0 (GetItems), signed with AWS Signature
 * Version 4 (implemented here with the built-in `crypto` module only).
 *
 * Response JSON:
 *   { "available": true,  "prices": { "ASIN": { "amount": 12.34,
 *       "currency": "CAD", "display": "$12.34" } } }
 *
 * Credentials come ONLY from environment variables (set them in Vercel,
 * never in this file):
 *   PAAPI_ACCESS_KEY  — Product Advertising API access key
 *   PAAPI_SECRET_KEY  — Product Advertising API secret key
 *   PAAPI_PARTNER_TAG — Associates partner tag (defaults to "zeroregretb04-20")
 *
 * Without credentials the function does NOT call Amazon and returns
 * HTTP 200 { "available": false, "prices": {} } — never an error, never a
 * fake price. Prices are cached in memory for 10 minutes; only ASINs
 * missing from the cache are fetched from Amazon.
 */

'use strict';

const crypto = require('crypto');
const https = require('https');

const HOST = 'webservices.amazon.ca';
const REGION = 'us-east-1';
const SERVICE = 'ProductAdvertisingAPI';
const PATH = '/paapi5/getitems';
const TARGET = 'com.amazon.paapi5.v1.ProductAdvertisingAPIv1.GetItems';
const DEFAULT_PARTNER_TAG = 'zeroregretb04-20';
const MAX_ASINS = 10;
const CACHE_TTL_MS = 10 * 60 * 1000; // 10 minutes
const REQUEST_TIMEOUT_MS = 6000; // 6 seconds

// In-memory price cache: { ASIN: { price: { amount, currency, display }, expiresAt: number } }
const cache = {};

function sha256Hex(data) {
  return crypto.createHash('sha256').update(data, 'utf8').digest('hex');
}

function hmac(key, data) {
  return crypto.createHmac('sha256', key).update(data, 'utf8').digest();
}

function amzDates(now) {
  const d = now || new Date();
  const pad = (n) => String(n).padStart(2, '0');
  const datestamp =
    d.getUTCFullYear() + pad(d.getUTCMonth() + 1) + pad(d.getUTCDate());
  const amzdate =
    datestamp + 'T' + pad(d.getUTCHours()) + pad(d.getUTCMinutes()) + pad(d.getUTCSeconds()) + 'Z';
  return { datestamp, amzdate };
}

/**
 * Sign a PA-API request with AWS Signature Version 4.
 * Returns { authorization, amzDate, headers }.
 * Exported (as handler.signRequest) so tests can verify the signature
 * without calling Amazon.
 */
function signRequest({ accessKey, secretKey, body }) {
  const { datestamp, amzdate } = amzDates();
  const payloadHash = sha256Hex(body);

  const canonicalHeaders =
    'content-encoding:amz-1.0\n' +
    'content-type:application/json; charset=utf-8\n' +
    'host:' + HOST + '\n' +
    'x-amz-date:' + amzdate + '\n' +
    'x-amz-target:' + TARGET + '\n';
  const signedHeaders = 'content-encoding;content-type;host;x-amz-date;x-amz-target';

  const canonicalRequest = [
    'POST',
    PATH,
    '',
    canonicalHeaders,
    signedHeaders,
    payloadHash,
  ].join('\n');

  const scope = datestamp + '/' + REGION + '/' + SERVICE + '/aws4_request';
  const stringToSign = [
    'AWS4-HMAC-SHA256',
    amzdate,
    scope,
    sha256Hex(canonicalRequest),
  ].join('\n');

  const kDate = hmac('AWS4' + secretKey, datestamp);
  const kRegion = hmac(kDate, REGION);
  const kService = hmac(kRegion, SERVICE);
  const kSigning = hmac(kService, 'aws4_request');
  const signature = crypto
    .createHmac('sha256', kSigning)
    .update(stringToSign, 'utf8')
    .digest('hex');

  const authorization =
    'AWS4-HMAC-SHA256 Credential=' + accessKey + '/' + scope +
    ', SignedHeaders=' + signedHeaders +
    ', Signature=' + signature;

  return {
    authorization,
    amzDate: amzdate,
    headers: {
      'Content-Encoding': 'amz-1.0',
      'Content-Type': 'application/json; charset=utf-8',
      Host: HOST,
      'X-Amz-Date': amzdate,
      'X-Amz-Target': TARGET,
      Authorization: authorization,
    },
  };
}

/**
 * Call PA-API 5.0 GetItems for the given ASINs.
 * Resolves to { ASIN: { amount, currency, display } } — possibly empty.
 * Never rejects: any error, non-200 status, timeout, or malformed response
 * resolves to {} (the caller then falls back to cached prices / available:false).
 */
function fetchPricesFromAmazon({ accessKey, secretKey, partnerTag, asins }) {
  return new Promise((resolve) => {
    let settled = false;
    const done = (value) => {
      if (!settled) {
        settled = true;
        resolve(value);
      }
    };

    const body = JSON.stringify({
      PartnerTag: partnerTag,
      PartnerType: 'Associates',
      Marketplace: 'www.amazon.ca',
      ItemIds: asins,
      Resources: ['Offers.Listings.Price', 'ItemInfo.Title'],
    });

    const signed = signRequest({ accessKey, secretKey, body });

    const req = https.request(
      {
        hostname: HOST,
        path: PATH,
        method: 'POST',
        headers: signed.headers,
        timeout: REQUEST_TIMEOUT_MS,
      },
      (res) => {
        let raw = '';
        res.on('data', (chunk) => {
          raw += chunk;
        });
        res.on('end', () => {
          if (res.statusCode !== 200) return done({});
          let data;
          try {
            data = JSON.parse(raw);
          } catch (e) {
            return done({});
          }
          const items =
            data && data.ItemsResult && Array.isArray(data.ItemsResult.Items)
              ? data.ItemsResult.Items
              : [];
          const out = {};
          for (const item of items) {
            const asin = item && item.ASIN;
            const price =
              item &&
              item.Offers &&
              Array.isArray(item.Offers.Listings) &&
              item.Offers.Listings[0] &&
              item.Offers.Listings[0].Price;
            // Only real prices: an item with no price is omitted, never invented.
            if (!asin || !price || typeof price.Amount !== 'number') continue;
            out[asin] = {
              amount: price.Amount,
              currency: price.Currency,
              display: price.DisplayAmount,
            };
          }
          done(out);
        });
      }
    );

    req.on('timeout', () => {
      req.destroy();
      done({});
    });
    req.on('error', () => done({}));
    req.write(body);
    req.end();
  });
}

async function handler(req, res) {
  const send = (payload) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(payload));
  };

  // Parse ?asins=ASIN1,ASIN2 — comma-separated, deduped, max 10.
  let asins = [];
  try {
    const url = new URL(req.url || '/', 'http://localhost');
    const raw = url.searchParams.get('asins') || '';
    asins = raw
      .split(',')
      .map((s) => s.trim().toUpperCase())
      .filter(Boolean);
    asins = [...new Set(asins)].slice(0, MAX_ASINS);
  } catch (e) {
    asins = [];
  }

  // Serve what the cache has; only fetch what is missing or stale.
  const now = Date.now();
  const prices = {};
  const missing = [];
  for (const asin of asins) {
    const entry = cache[asin];
    if (entry && entry.expiresAt > now) {
      prices[asin] = entry.price;
    } else {
      missing.push(asin);
    }
  }

  const accessKey = process.env.PAAPI_ACCESS_KEY;
  const secretKey = process.env.PAAPI_SECRET_KEY;
  const partnerTag = process.env.PAAPI_PARTNER_TAG || DEFAULT_PARTNER_TAG;

  if (missing.length > 0 && accessKey && secretKey) {
    const fetched = await fetchPricesFromAmazon({
      accessKey,
      secretKey,
      partnerTag,
      asins: missing,
    });
    const expiresAt = Date.now() + CACHE_TTL_MS;
    for (const asin of Object.keys(fetched)) {
      prices[asin] = fetched[asin];
      cache[asin] = { price: fetched[asin], expiresAt };
    }
  }
  // No credentials (or nothing fetched): return whatever the cache had,
  // otherwise available:false. Never an error, never a fake price.

  send({ available: Object.keys(prices).length > 0, prices });
}

module.exports = handler;
module.exports.signRequest = signRequest;
