// Zero Regret Buys — prices. Fetches live Amazon prices from /api/prices
// and writes them into [data-price-asin] elements, plus the discount pill
// [data-off-asin], the deal type [data-dealtype-asin] and the struck-through
// list price [data-was-asin] when Amazon reports a real saving.
// Never types a price: without a live price the element keeps its
// "Price on Amazon" placeholder, and the discount stays hidden.
(function () {
  "use strict";
  var loaded = {};
  function fmt(amount, currency) {
    try {
      return new Intl.NumberFormat("en-CA", { style: "currency", currency: currency || "CAD" }).format(amount);
    } catch (e) { return "$" + amount.toFixed(2); }
  }
  function updateTotal() {
    var list = document.getElementById("cart-list");
    var row = document.getElementById("cart-total-row");
    var totalEl = document.querySelector("[data-cart-total]");
    if (!list || !row || !totalEl) return;
    var els = Array.prototype.slice.call(list.querySelectorAll("[data-price-asin]"));
    if (!els.length) { row.hidden = true; return; }
    var sum = 0;
    var all = true;
    els.forEach(function (el) {
      var asin = el.getAttribute("data-price-asin");
      if (loaded[asin]) { sum += loaded[asin].amount; } else { all = false; }
    });
    if (all && sum > 0) {
      totalEl.textContent = fmt(sum, "CAD");
      row.hidden = false;
    } else {
      row.hidden = true;
    }
  }
  // Fill a live deal: discount pill, deal type, struck-through list
  // price. Any of these stay hidden until a real saving arrives.
  function applyDeal(asin, p) {
    if (!p || typeof p.off !== "number" || p.off <= 0) return;
    document.querySelectorAll('[data-off-asin="' + asin + '"]').forEach(function (el) {
      el.textContent = "-" + p.off + "%";
      el.hidden = false;
    });
    document.querySelectorAll('[data-offpdp-asin="' + asin + '"]').forEach(function (el) {
      el.textContent = p.off + "% OFF";
      el.hidden = false;
    });
    document.querySelectorAll('[data-dealtype-asin="' + asin + '"]').forEach(function (el) {
      el.hidden = false;
    });
    if (p.was && p.was.display) {
      document.querySelectorAll('[data-was-asin="' + asin + '"]').forEach(function (el) {
        el.textContent = p.was.display;
        el.hidden = false;
      });
    }
  }
  function applyPrices(prices) {
    Object.keys(prices).forEach(function (asin) {
      var p = prices[asin];
      if (p && typeof p.amount === "number") loaded[asin] = p;
    });
    document.querySelectorAll("[data-price-asin]").forEach(function (el) {
      var asin = el.getAttribute("data-price-asin");
      var p = loaded[asin];
      if (p) {
        el.textContent = p.display || fmt(p.amount, p.currency);
        el.classList.add("price--live");
        applyDeal(asin, p);
      }
    });
    updateTotal();
  }
  function fetchBatch(batch) {
    return fetch("/api/prices?asins=" + encodeURIComponent(batch.join(",")))
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) { if (d && d.prices) applyPrices(d.prices); })
      .catch(function () {});
  }
  function refresh() {
    var els = Array.prototype.slice.call(document.querySelectorAll("[data-price-asin]"));
    var asins = [];
    els.forEach(function (el) {
      var a = el.getAttribute("data-price-asin");
      if (a && asins.indexOf(a) === -1 && !loaded[a]) asins.push(a);
    });
    if (!asins.length) { updateTotal(); return; }
    var batches = [];
    for (var i = 0; i < asins.length; i += 10) batches.push(asins.slice(i, i + 10));
    batches.forEach(fetchBatch);
  }
  window.ZRB_prices = { refresh: refresh };
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", refresh);
  } else {
    refresh();
  }
})();
