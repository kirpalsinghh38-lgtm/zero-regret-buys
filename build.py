"""Zero Regret Buys — v2 builder (from-scratch rebuild, 2026-11-25).

Customer first: a shop, not a story. Products up front, almost no
paragraphs. All content (products, links, photos, copy) comes from
data.py untouched, so every affiliate link, ASIN and photo is identical
to v1. This file holds only the new design: templates + page assembly.
"""
import json
import os
from datetime import datetime

from data import (
    PRODUCTS, BADGES, PDP_COPY, PHOTOS, PDP_EXTRA, FAQS,
    TAG, BASE, DISCLOSURE, CART_ALL_URL, CART_ALL_HTML,
)

BUILD_MONTH = datetime.now().strftime("%B %Y")
SITE = os.path.dirname(os.path.abspath(__file__))

# Badge label -> job theme slug (keeps ?job= deep links working).
JOB_BY_BADGE = {
    "Sleep": "sleep", "Blackout Sleep": "sleep", "Falling Asleep": "sleep",
    "Stress & Sleep": "sleep", "Mornings": "sleep",
    "Glass Skin": "skin", "Dark Spots": "skin", "Bright Cleanse": "skin",
    "Dry Skin": "skin", "Even Tone": "skin", "Firmness": "skin",
    "Brightness": "skin", "Budget Hydration": "skin",
    "Lightweight Hydration": "skin", "Pores & Oil": "skin",
    "24hr Moisture": "skin", "Daily SPF": "skin",
    "Scalp": "hair-scalp", "Scalp Care": "hair-scalp",
    "Damaged Hair": "hair-scalp", "Hair, Skin & Nails": "hair-scalp",
    "Gym Days": "body-recovery", "Posture": "body-recovery",
    "Back Relief": "body-recovery", "Joint Comfort": "body-recovery",
    "Daily Omegas": "inner-health", "Immunity": "inner-health",
    "Bones": "inner-health", "Gut Health": "inner-health",
    "Energy Metabolism": "inner-health",
}

# The five job themes, in display order. Home shows one horizontal row per theme.
THEMES = [
    ("sleep", "Sleep"),
    ("skin", "Skin"),
    ("hair-scalp", "Hair & Scalp"),
    ("body-recovery", "Body & Recovery"),
    ("inner-health", "Inner Health"),
]


def theme_of(p):
    return JOB_BY_BADGE[BADGES[p["slug"]]]


def theme_products(slug):
    return sorted([p for p in PRODUCTS if theme_of(p) == slug],
                  key=lambda p: p["num"], reverse=True)


def faqs_live():
    """The price FAQ, rewritten now that prices are fetched live from Amazon."""
    out = []
    for q, a in FAQS:
        if q.startswith("Why don\u2019t you show prices"):
            out.append(("How do prices work here?",
                        "Prices are fetched live from Amazon, so what you see is today\u2019s price \u2014 never a number typed by hand. Amazon is still the final word at checkout, and the price can change between here and there."))
        else:
            out.append((q, a))
    return out

NAV = [("index.html", "Home"), ("shop.html", "Shop"), ("about.html", "About")]

# The 3 newest picks (highest episode numbers) get a NEW tag.
NEWEST = {p["num"] for p in sorted(PRODUCTS, key=lambda p: p["num"], reverse=True)[:3]}


def ep_label(p):
    return '<span class="ep">Ep %s</span>' % p["num"]


def new_tag(p):
    return '<span class="newtag">New</span>' if p["num"] in NEWEST else ""

TAB_ICONS = {
    "index.html": ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h5v-6h4v6h5V10"/></svg>', "Home"),
    "shop.html": ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 8h14l-1.2 12.5H6.2L5 8z"/><path d="M9 10V6.5a3 3 0 016 0V10"/></svg>', "Shop"),
    "about.html": ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><path d="M12 7.6v.4"/></svg>', "About"),
}


def short_verdict(p):
    """First sentence of the verdict, one line. The whole verdict is cut."""
    s = PDP_COPY[p["slug"]]["verdict"].split(". ")[0]
    return s if s.endswith(".") else s + "."


def meta_pitch(pitch, limit=155):
    return pitch if len(pitch) <= limit else pitch[: limit - 1].rsplit(" ", 1)[0] + "…"


def head(title, desc, path, root, body_class=""):
    body_attr = ' class="%s"' % body_class if body_class else ""
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<meta property="og:url" content="%s/%s">
<meta property="og:image" content="%s/images/logo.jpg">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="%simages/logo.jpg">
<link rel="stylesheet" href="%sstyles.css">
</head>
<body%s>
""" % (title, desc, title, desc, BASE, path, BASE, root, root, body_attr)


CART_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 3h2l2.4 12.4A2 2 0 009.36 17h7.9a2 2 0 001.95-1.55L21 7H6"/><circle cx="10" cy="21" r="1.6"/><circle cx="18" cy="21" r="1.6"/></svg>', "Cart")


def header(root, current, tab=True):
    links = "".join(
        '<a href="%s%s"%s>%s</a>' % (root, href, ' aria-current="page"' if href == current else "", label)
        for href, label in NAV
    )
    cart_current = ' aria-current="page"' if current == "cart.html" else ""
    cart_tab = (
        '<a href="%scart.html" class="tab-cart"%s><span class="tab-icon-wrap">%s<span class="cart-count" data-cart-count>0</span></span><span>%s</span></a>'
        % (root, cart_current, CART_ICON[0], CART_ICON[1]))
    nav_cart = ('<a class="nav-cart" href="%scart.html">Your cart '
                '<span class="cart-count" data-cart-count>0</span></a>' % root)
    tabbar = ("""
<nav class="tabbar" aria-label="Mobile">
  %s%s
</nav>""" % ("".join(
        '<a href="%s%s"%s>%s<span>%s</span></a>'
        % (root, href, ' aria-current="page"' if href == current else "",
           TAB_ICONS[href][0], TAB_ICONS[href][1])
        for href in TAB_ICONS), cart_tab)) if tab else ""
    subnav = "".join(
        '<a href="%sshop.html?job=%s">%s</a>' % (root, slug, label)
        for slug, label in THEMES)
    return """
<header class="site-header">
  <div class="header-inner">
    <a class="brandmark" href="%sindex.html" aria-label="Zero Regret Buys — home">
      <img class="logoimg" src="%simages/logo.jpg" alt="Zero Regret Buys logo">
      <span class="wordmark">Zero Regret Buys<small>THIRTY PICKS · ZERO REGRET</small></span>
    </a>
    <form class="header-search" action="%sshop.html" method="get" role="search">
      <span aria-hidden="true">⌕</span>
      <input type="search" name="q" placeholder="Search picks, ingredients, keywords…" aria-label="Search picks">
    </form>
    <nav class="mainnav" aria-label="Primary">
      %s
      %s
      <a class="nav-cta" href="%sshop.html"><span class="cta-full">Browse the picks</span><span class="cta-short">Browse</span></a>
    </nav>
  </div>
  <nav class="subnav" aria-label="Themes">
    <div class="subnav-inner">
      <a href="%sshop.html">All picks</a>
      %s
      <a href="%sabout.html">About</a>
    </div>
  </nav>
</header>
%s
""" % (root, root, root, links, nav_cart, root, root, subnav, root, tabbar)


def footer(root):
    theme_links = "".join(
        '<a href="%sshop.html?job=%s">%s</a>' % (root, slug, label)
        for slug, label in THEMES)
    return """
</main>
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-cols">
      <div class="footer-col footer-brand">
        <a class="brandmark" href="%sindex.html">
          <img class="logoimg" src="%simages/logo.jpg" alt="Zero Regret Buys logo">
          <span class="wordmark">Zero Regret Buys<small>THIRTY PICKS · ZERO REGRET</small></span>
        </a>
        <p class="footer-tag">Thirty worth-it picks. One job each. No hype.</p>
      </div>
      <nav class="footer-col" aria-label="Deals">
        <h3>Deals</h3>
        <a href="%sindex.html#top-deals">Today’s top deals</a>
        <a href="%sshop.html">Shop all picks</a>
        <a href="%scart.html">Your cart</a>
      </nav>
      <nav class="footer-col" aria-label="Themes">
        <h3>Themes</h3>
        %s
      </nav>
      <nav class="footer-col" aria-label="Company">
        <h3>Company</h3>
        <a href="%sabout.html">About</a>
        <a href="%sterms.html">Terms</a>
        <a href="%sprivacy.html">Privacy</a>
      </nav>
    </div>
    <p class="footer-disclosure">%s Product links on this site are affiliate (paid) links — if you buy through them, we may earn a commission at no extra cost to you. Certain content that appears on this site comes from Amazon. This content is provided “as is” and is subject to change or removal at any time. <a href="%sabout.html">Read our full affiliate disclosure here</a></p>
    <p class="footer-copy">© %s Zero Regret Buys</p>
  </div>
</footer>
<script src="%ssite.js"></script>
<script src="%sprices.js"></script>
<script src="%scart.js"></script>
</body>
</html>
""" % (root, root, root, root, root, theme_links, root, root, root,
       DISCLOSURE, root, datetime.now().year, root, root, root)


def badge(p):
    return '<span class="badge">Best for %s</span>' % BADGES[p["slug"]]


def search_blob(p):
    return "%s %s %s %s %s %s ep%s" % (
        p["title"], p["pitch"], p["cat"], p["sub"], BADGES[p["slug"]], p["keyword"], p["num"])


def card(p, root, pitch=True):
    """DealSeek-style deal card: photo, title, discount pill + deal type,
    live price + struck-through list price, store, View Deal on Amazon.
    The discount pill, deal type and list price stay hidden until the
    live price service returns a real saving for that ASIN."""
    photo = p["photos"][0] if p.get("photos") else ""
    img = ('<img src="%s%s" alt="%s product photo" loading="lazy">'
           % (root, photo, p["title"])) if photo else ""
    savebtn = ('<button type="button" class="cartbtn js-save" data-slug="%(slug)s" data-asin="%(asin)s" aria-pressed="false" aria-label="Add %(title)s to your cart">+</button>'
               % {"slug": p["slug"], "asin": p["asin"], "title": p["title"]})
    return """
<article class="card" data-num="%(num)s" data-title="%(title)s"
         data-cat="%(cat_slug)s" data-sub="%(sub_slug)s" data-job="%(job)s"
         data-slug="%(slug)s" data-asin="%(asin)s" data-search="%(search)s">
  <div class="card-photo">
    <a href="%(root)sproducts/%(slug)s.html">%(img)s</a>
    %(newtag)s
    %(savebtn)s
  </div>
  <div class="card-body">
    <div class="card-meta">%(badge)s %(ep)s</div>
    <h3><a href="%(root)sproducts/%(slug)s.html">%(title)s</a></h3>
    <div class="deal-line">
      <span class="off" data-off-asin="%(asin)s" hidden></span>
      <span class="dealtype" data-dealtype-asin="%(asin)s" hidden>Price Drop</span>
    </div>
    <div class="pricerow">
      <span class="price" data-price-asin="%(asin)s">Price on Amazon</span>
      <s class="was" data-was-asin="%(asin)s" hidden></s>
    </div>
    <div class="store">Amazon</div>
    <a class="btn btn-deal btn-block" href="%(url)s"
       target="_blank" rel="sponsored nofollow noopener">View Deal on Amazon</a>
    <div class="paidnote">(paid link)</div>
  </div>
</article>""" % {
        "num": p["num"], "title": p["title"], "cat_slug": p["cat_slug"],
        "sub_slug": p["sub_slug"], "job": JOB_BY_BADGE[BADGES[p["slug"]]],
        "search": search_blob(p), "root": root, "slug": p["slug"],
        "asin": p["asin"], "img": img, "badge": badge(p), "ep": ep_label(p),
        "newtag": new_tag(p), "savebtn": savebtn, "url": p["url"],
    }


def cartall_block():
    return """
      <div class="cartall">
        <a class="btn btn-deal btn-big" href="%s"
           target="_blank" rel="sponsored nofollow noopener">Add all 30 to cart on Amazon</a>
        <div class="paidnote">(paid link)</div>
        <p class="micro">One click loads all thirty picks into your Amazon.ca cart — remove anything you don’t want before checkout.</p>
      </div>""" % CART_ALL_HTML


# The five newest picks, ranked Top 1-5 on the home carousel.
TOP_DEALS = sorted(PRODUCTS, key=lambda p: p["num"], reverse=True)[:5]


def bento_tiles(root):
    """DealSeek-style bento: a big Top Picks tile + one tile per theme."""
    picks = TOP_DEALS[:3]
    pick_items = "".join(
        '<a class="bento-pick" href="%(root)sproducts/%(slug)s.html">'
        '<span class="bento-rank">%(n)d</span>'
        '<img src="%(root)s%(photo)s" alt="%(title)s" loading="lazy">'
        '<span class="bento-pick-title">%(title)s</span></a>'
        % {"root": root, "slug": q["slug"], "n": i + 1,
           "photo": q["photos"][0] if q.get("photos") else "",
           "title": q["title"]}
        for i, q in enumerate(picks))
    theme_tiles = ""
    for slug, label in THEMES:
        items = theme_products(slug)
        top = items[0]
        photo = top["photos"][0] if top.get("photos") else ""
        img = ('<img src="%s%s" alt="%s" loading="lazy">'
               % (root, photo, label)) if photo else ""
        theme_tiles += """
      <a class="bento-tile" href="shop.html?job=%s">
        %s
        <span class="bento-tile-label">%s</span>
        <span class="bento-tile-count">%d picks</span>
      </a>""" % (slug, img, label, len(items))
    return """
    <div class="bento">
      <div class="bento-tile bento-toppicks">
        <span class="bento-tile-label">Top Picks</span>
        <div class="bento-picks">%s</div>
        <a class="bento-viewall" href="shop.html">View All &rarr;</a>
      </div>
%s
    </div>""" % (pick_items, theme_tiles)


# ---------------- index ----------------
def build_index():
    root = ""
    top_cards = "".join(
        '<div class="deal-wrap"><span class="rank rank-%d">Top %d</span>%s</div>'
        % (i + 1, i + 1, card(p, root))
        for i, p in enumerate(TOP_DEALS))
    all_cards = "".join(
        card(p, root) for p in sorted(PRODUCTS, key=lambda p: p["num"], reverse=True))
    body = """
<main id="main">
  <div class="hero">
    <div class="wrap hero-copy">
      <h1>Thirty picks. Zero regret.</h1>
      <p class="sub">One job each. Live prices from Amazon, no hype.</p>
      <div class="hero-ctas">
        <a class="btn btn-deal" href="#top-deals">Today’s top deals</a>
        <a class="btn btn-outline" href="shop.html">Browse the shop</a>
      </div>
    </div>
  </div>

  <div class="wrap">
%s
    <section class="topdeals" id="top-deals">
      <div class="section-head">
        <h2>Today’s Top Deals</h2>
        <a class="viewall" href="shop.html">View All &rarr;</a>
      </div>
      <div class="hrow">
%s
      </div>
    </section>
    <section class="explore" id="explore">
      <div class="section-head">
        <h2>Explore</h2>
        <span class="explore-sub">All thirty picks, in one place.</span>
      </div>
      <div class="grid">
%s
      </div>
    </section>
%s
  </div>
""" % (bento_tiles(root), top_cards, all_cards, cartall_block())
    return (head("Zero Regret Buys — Thirty picks. Zero regret.",
                 "Zero Regret Buys: thirty worth-it products, each with one clear job. Paid Amazon links, labeled on every card.",
                 "index.html", root)
            + header(root, "index.html") + body + footer(root))


# ---------------- shop ----------------
def build_shop():
    root = ""
    cards = "".join(card(p, root) for p in PRODUCTS)
    cats = sorted(set((p["cat"], p["cat_slug"]) for p in PRODUCTS))
    subs = sorted(set((p["sub"], p["sub_slug"], p["cat_slug"]) for p in PRODUCTS))
    aisle_chips = "".join(
        '<button type="button" class="chip" data-group="cat" data-value="%s" aria-pressed="%s">%s</button>'
        % (slug, "true" if slug == "all" else "false", label)
        for label, slug in [("All", "all")] + cats)
    shelf_chips = "".join(
        '<button type="button" class="chip" data-group="sub" data-value="%s" data-cat="%s" aria-pressed="%s">%s</button>'
        % (slug, cat, "true" if slug == "all" else "false", label)
        for label, slug, cat in [("All", "all", "")] + subs)
    body = """
<main id="main">
  <div class="wrap">
    <div class="section">
      <h1>The Shop</h1>
      <p class="sub" style="color: var(--ink-soft); margin-top: 8px;">All thirty picks. Prices are fetched live from Amazon.</p>
      <div class="toolbar">
        <div class="searchrow">
          <label class="searchbox">
            <span aria-hidden="true">⌕</span>
            <input id="shop-search" type="search" placeholder="Search picks, ingredients, keywords…" aria-label="Search picks">
          </label>
          <label class="sortwrap">Sort
            <select id="shop-sort" aria-label="Sort picks">
              <option value="featured">Featured</option>
              <option value="az">A–Z</option>
              <option value="cat">Category</option>
            </select>
          </label>
        </div>
        <p class="count" id="result-count">Showing all 30 picks</p>
        <div class="chiprow" role="group" aria-label="Aisle">%s</div>
        <div class="chiprow chiprow-sub" role="group" aria-label="Shelf">%s</div>
      </div>
      <div class="grid" id="shop-grid">
%s
      </div>
      <div class="shelf-rail" aria-hidden="true"></div>
      <p class="empty" id="shop-empty" hidden>Nothing matches — try a different word.</p>
%s
      <div class="sticky-cart">
        <a class="btn btn-shelf" href="%s" target="_blank" rel="sponsored nofollow noopener">Add all 30 to cart on Amazon</a>
        <span class="sticky-paid">(paid link)</span>
      </div>
    </div>
  </div>
""" % (aisle_chips, shelf_chips, cards, cartall_block(), CART_ALL_HTML)
    return (head("The Shop — Zero Regret Buys",
                 "All thirty picks in one place. Search, filter, compare — then check today’s live price on Amazon.",
                 "shop.html", root, body_class="shop-page")
            + header(root, "shop.html") + body + footer(root))


# ---------------- product ----------------
def related(p):
    others = [q for q in PRODUCTS if q["slug"] != p["slug"]]
    same_sub = [q for q in others if q["sub_slug"] == p["sub_slug"]]
    same_cat = [q for q in others if q["cat_slug"] == p["cat_slug"] and q not in same_sub]
    return (same_sub + same_cat + others)[:4]


def build_product(p):
    root = "../"
    copy = PDP_COPY[p["slug"]]
    photo = p["photos"][0] if p.get("photos") else ""
    img = ('<img src="%s%s" alt="%s product photo">' % (root, photo, p["title"])) if photo else ""
    getif = "".join("<li>%s</li>" % g for g in copy["getif"])
    skip_text = p.get("skip") or ""
    skip_html = ('<div class="skipif"><h2>Skip this if…</h2><p>%s</p></div>'
                 % (skip_text[:1].upper() + skip_text[1:])) if skip_text else ""
    savebtn = ('<button type="button" class="btn btn-outline js-save" data-slug="%(slug)s" data-asin="%(asin)s" aria-pressed="false">+ Add to cart</button>'
               % {"slug": p["slug"], "asin": p["asin"]})
    more = "".join(card(q, root) for q in related(p))
    body = """
<main id="main">
  <div class="wrap">
    <div class="pdp">
      <p class="breadcrumb"><a href="../index.html">Home</a> / <a href="../shop.html">Shop</a> / <a href="../shop.html?cat=%(cat_slug)s">%(cat)s</a> / %(title)s</p>
      <a class="pdp-back" href="../shop.html">‹ All picks</a>
      <div class="pdp-grid">
        <div class="pdp-photo">%(img)s</div>
        <div class="pdp-info">
          <div class="pdp-store">Amazon</div>
          <div class="pdp-meta">%(badge)s %(ep)s %(newtag)s</div>
          <h1>%(title)s</h1>
          <p class="key">%(key)s</p>
          <p class="verdict">%(verdict)s</p>
          <div class="pdp-deal">
            <span class="off off--pdp" data-offpdp-asin="%(asin)s" hidden></span>
            <div class="pricerow">
              <span class="price price--pdp" data-price-asin="%(asin)s">Price on Amazon</span>
              <s class="was" data-was-asin="%(asin)s" hidden></s>
            </div>
          </div>
          <div class="pdp-buy">
            <a class="btn btn-deal" href="%(url)s" target="_blank" rel="sponsored nofollow noopener">View Deal on Amazon</a>
            <p class="pdp-disc">%(disc)s Prices and availability are accurate as of the date and time shown and are subject to change.</p>
            <a class="btn btn-outline" href="%(cart_url)s" target="_blank" rel="sponsored nofollow noopener">Add to Cart on Amazon</a>
            <div class="paidnote">(paid links)</div>
            %(savebtn)s
          </div>
          <div class="getif">
            <h2>Get this if…</h2>
            <ul>%(getif)s</ul>
          </div>
          %(skip_html)s
          <div class="kwcard">
            <div class="kw">%(keyword)s</div>
            <p>Comment this word under the reel and the link lands in your DMs.</p>
          </div>
        </div>
      </div>
      <div class="more">
        <div class="section-head">
          <h2>Similar Deals</h2>
          <a class="viewall" href="../shop.html">View All &rarr;</a>
        </div>
        <div class="hrow">
%(more)s
        </div>
      </div>
    </div>
  </div>
""" % {
        "cat_slug": p["cat_slug"], "cat": p["cat"], "title": p["title"],
        "asin": p["asin"],
        "img": img, "badge": badge(p), "ep": ep_label(p), "newtag": new_tag(p),
        "key": copy["key"],
        "verdict": short_verdict(p), "url": p["url"],
        "cart_url": p["cart_url"], "getif": getif, "skip_html": skip_html,
        "savebtn": savebtn, "disc": DISCLOSURE,
        "keyword": p["keyword"], "more": more,
    }
    return (head("%s — Zero Regret Buys" % p["title"],
                 meta_pitch(p["pitch"]),
                 "products/%s.html" % p["slug"], root)
            + header(root, "shop.html") + body + footer(root))


# ---------------- cart ----------------
def build_cart():
    root = ""
    body = """
<main id="main">
  <div class="wrap">
    <div class="section">
      <h1>Your cart</h1>
      <p class="sub" style="color: var(--ink-soft); margin-top: 8px;">Saved here, in this browser only. One click loads them into your Amazon.ca cart.</p>
      <div class="cart-empty" id="cart-empty">
        <p>Your cart is empty. Tap + on any product to add it here.</p>
        <a class="btn btn-outline" href="shop.html">Browse the picks</a>
      </div>
      <ul class="cart-list" id="cart-list"></ul>
      <div class="cart-summary" id="cart-summary" hidden>
        <div class="cart-total-row" id="cart-total-row" hidden><span>Estimated total</span><strong data-cart-total></strong></div>
        <p class="micro">Prices are fetched live from Amazon. The final total is set by Amazon at checkout.</p>
        <a class="btn btn-shelf btn-big btn-block" id="cart-checkout" href="#" target="_blank" rel="sponsored nofollow noopener">Checkout on Amazon</a>
        <div class="paidnote">(paid link)</div>
        <button type="button" class="cart-clear" id="cart-clear">Clear cart</button>
      </div>
    </div>
  </div>
"""
    return (head("Your cart — Zero Regret Buys",
                 "Your saved picks, in one place. One click loads them into your Amazon.ca cart.",
                 "cart.html", root)
            + header(root, "cart.html") + body + footer(root))


# ---------------- about ----------------
def build_about():
    root = ""
    faqs = "".join(
        '<div class="faq-item"><h3>%s</h3><p>%s</p></div>' % (q, a)
        for q, a in faqs_live())
    body = """
<main id="main">
  <div class="wrap">
    <div class="section prose">
      <h1>About</h1>
      <p>One product per reel episode. Each label checked for the right form and honest facts-panel math. If it didn’t pass, it’s not here.</p>
      <h2>Questions</h2>
      <div class="faq-list">
%s
      </div>
      <h2>Disclosure</h2>
      <p>%s Product links on this site are affiliate (paid) links — if you buy through them, we may earn a commission at no extra cost to you.</p>
    </div>
  </div>
""" % (faqs, DISCLOSURE)
    return (head("About — Zero Regret Buys",
                 "One product per reel episode. Each label checked for the right form and honest facts-panel math.",
                 "about.html", root)
            + header(root, "about.html") + body + footer(root))


# ---------------- 404 / terms / privacy ----------------
def build_404():
    root = ""
    body = """
<main id="main">
  <div class="wrap">
    <div class="section prose">
      <h1>Not found</h1>
      <p>That page isn’t here. <a href="index.html">Back to the picks</a>.</p>
    </div>
  </div>
"""
    return (head("Not found — Zero Regret Buys",
                 "That page isn’t here.", "404.html", root)
            + header(root, "index.html") + body + footer(root))


def build_terms():
    root = ""
    body = """
<main id="main">
  <div class="wrap">
    <div class="section prose">
      <h1>Terms</h1>
      <p>Zero Regret Buys lists products featured in its short-form videos. Prices shown here are fetched live from Amazon; the price and availability on Amazon are what count at checkout.</p>
      <p>Product links are affiliate links. As an Amazon Associate we earn from qualifying purchases, at no extra cost to you.</p>
      <p>Nothing here is medical advice. Supplements interact with medications and conditions — talk to your pharmacist or clinician before starting anything new.</p>
    </div>
  </div>
"""
    return (head("Terms — Zero Regret Buys",
                 "Terms for Zero Regret Buys.", "terms.html", root)
            + header(root, "index.html") + body + footer(root))


def build_privacy():
    root = ""
    body = """
<main id="main">
  <div class="wrap">
    <div class="section prose">
      <h1>Privacy</h1>
      <p>This site collects nothing from you directly — no accounts, no checkout, no tracking of your own. Clicking a product link takes you to Amazon, which has its own privacy policy.</p>
      <p>Questions: reach us through the social links on our profiles.</p>
    </div>
  </div>
"""
    return (head("Privacy — Zero Regret Buys",
                 "Privacy for Zero Regret Buys.", "privacy.html", root)
            + header(root, "index.html") + body + footer(root))


# ---------------- shop script (reused behaviour, same hooks) ----------------
SITE_JS = """// Zero Regret Buys — shop search, filter and sort. Dependency-free.
// Included in the footer of every page; does nothing when the shop grid
// is absent (e.g. product pages), so it is safe to load site-wide.
(function () {
  "use strict";
  var grid = document.getElementById("shop-grid");
  if (!grid) return;

  var search = document.getElementById("shop-search");
  var sort = document.getElementById("shop-sort");
  var count = document.getElementById("result-count");
  var empty = document.getElementById("shop-empty");
  var cards = Array.prototype.slice.call(grid.querySelectorAll(".card"));
  var total = cards.length;
  var state = { q: "", cat: "all", sub: "all", job: "all", sort: "featured" };

  var knownCats = [];
  var knownSubs = [];
  var knownJobs = [];
  cards.forEach(function (card) {
    if (knownCats.indexOf(card.dataset.cat) === -1) knownCats.push(card.dataset.cat);
    if (knownSubs.indexOf(card.dataset.sub) === -1) knownSubs.push(card.dataset.sub);
    if (card.dataset.job && knownJobs.indexOf(card.dataset.job) === -1) knownJobs.push(card.dataset.job);
  });
  var JOB_LABELS = { sleep: "Sleep", skin: "Skin", "hair-scalp": "Hair & Scalp", "body-recovery": "Body & Recovery", "inner-health": "Inner Health" };

  function setPressed(group, value) {
    var btns = document.querySelectorAll('.chip[data-group="' + group + '"]');
    btns.forEach(function (btn) {
      btn.setAttribute("aria-pressed", btn.dataset.value === value ? "true" : "false");
    });
  }

  function sortCards() {
    var ordered = cards.slice();
    if (state.sort === "az") {
      ordered.sort(function (a, b) { return a.dataset.title.localeCompare(b.dataset.title); });
    } else if (state.sort === "cat") {
      ordered.sort(function (a, b) {
        if (a.dataset.cat === b.dataset.cat) return a.dataset.title.localeCompare(b.dataset.title);
        return a.dataset.cat.localeCompare(b.dataset.cat);
      });
    } else {
      ordered.sort(function (a, b) { return Number(a.dataset.num) - Number(b.dataset.num); });
    }
    ordered.forEach(function (card) { grid.appendChild(card); });
  }

  function apply() {
    var q = state.q.trim().toLowerCase();
    var shown = 0;
    cards.forEach(function (card) {
      var okCat = state.cat === "all" || card.dataset.cat === state.cat;
      var okSub = state.sub === "all" || card.dataset.sub === state.sub;
      var okJob = state.job === "all" || card.dataset.job === state.job;
      var okQ = !q || (card.dataset.search || "").toLowerCase().indexOf(q) !== -1;
      var show = okCat && okSub && okJob && okQ;
      card.style.display = show ? "" : "none";
      if (show) shown += 1;
    });
    sortCards();
    if (count) {
      var jobLabel = state.job !== "all" ? " · " + (JOB_LABELS[state.job] || state.job) : "";
      count.textContent = shown === total
        ? "Showing all " + total + " picks" + jobLabel
        : "Showing " + shown + " of " + total + " picks" + jobLabel;
    }
    if (empty) empty.hidden = shown !== 0;
    setPressed("cat", state.job === "all" ? state.cat : "");
    setPressed("sub", state.job === "all" ? state.sub : "");
  }

  document.querySelectorAll(".chip").forEach(function (btn) {
    btn.addEventListener("click", function () {
      state.job = "all";
      if (btn.dataset.group === "cat") {
        state.cat = btn.dataset.value;
        if (state.cat !== "all" && state.sub !== "all") {
          var subBtn = document.querySelector('.chip[data-group="sub"][data-value="' + state.sub + '"]');
          if (subBtn && subBtn.dataset.cat && subBtn.dataset.cat !== state.cat) state.sub = "all";
        }
      } else {
        state.sub = btn.dataset.value;
        if (state.sub !== "all" && btn.dataset.cat) {
          state.cat = btn.dataset.cat;
        }
      }
      apply();
    });
  });

  if (search) search.addEventListener("input", function () { state.q = search.value; state.job = "all"; apply(); });
  if (sort) sort.addEventListener("change", function () { state.sort = sort.value; apply(); });

  // Deep links (?cat= / ?sub= / ?job= / ?q=) apply on load; a sub implies
  // its aisle unless a cat was given explicitly. ?q= is the header search.
  var params = new URLSearchParams(window.location.search);
  var qParam = params.get("q");
  if (qParam) {
    state.q = qParam;
    if (search) search.value = qParam;
  }
  var catParam = params.get("cat");
  var subParam = params.get("sub");
  var jobParam = params.get("job");
  if (jobParam && knownJobs.indexOf(jobParam) !== -1) state.job = jobParam;
  if (catParam && knownCats.indexOf(catParam) !== -1) state.cat = catParam;
  if (subParam && knownSubs.indexOf(subParam) !== -1) {
    state.sub = subParam;
    if (!catParam) {
      var subBtn = document.querySelector('.chip[data-group="sub"][data-value="' + subParam + '"]');
      if (subBtn && subBtn.dataset.cat) state.cat = subBtn.dataset.cat;
    }
  }
  apply();
})();
"""


# ---------------- cart (add products, view them on the cart page) ----------------
CART_JS = """// Zero Regret Buys — cart. Add products, view them on the cart page,
// check out by loading them all into an Amazon cart.
// Runs on every page; the shop filter (site.js) is separate and untouched.
(function () {
  "use strict";
  var TAG = "__TAG__";
  var KEY = "zrb-cart";
  var OLD_KEY = "zrb-shortlist";
  var PRODUCTS = __PRODUCTS_JSON__;

  function load() {
    try {
      var raw = window.localStorage.getItem(KEY);
      if (!raw) {
        var old = window.localStorage.getItem(OLD_KEY);
        if (old) {
          raw = old;
          window.localStorage.setItem(KEY, old);
          window.localStorage.removeItem(OLD_KEY);
        }
      }
      var arr = raw ? JSON.parse(raw) : [];
      return Array.isArray(arr) ? arr.filter(function (s) { return PRODUCTS[s]; }) : [];
    } catch (e) { return []; }
  }
  function save(arr) {
    try { window.localStorage.setItem(KEY, JSON.stringify(arr)); } catch (e) {}
  }
  function prefix() {
    return window.location.pathname.indexOf("/products/") !== -1 ? "../" : "";
  }
  function cartUrl(slugs) {
    var parts = slugs.map(function (slug, i) {
      return "ASIN." + (i + 1) + "=" + PRODUCTS[slug].asin + "&Quantity." + (i + 1) + "=1";
    });
    return "https://www.amazon.ca/gp/aws/cart/add.html?AssociateTag=" + TAG + "&" + parts.join("&");
  }
  function updateCounts(slugs) {
    var counts = document.querySelectorAll("[data-cart-count]");
    counts.forEach(function (el) {
      el.textContent = String(slugs.length);
      el.style.display = slugs.length ? "" : "none";
    });
  }
  function syncButtons(slugs) {
    var btns = document.querySelectorAll(".js-save");
    btns.forEach(function (btn) {
      var on = slugs.indexOf(btn.dataset.slug) !== -1;
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      if (btn.classList.contains("cartbtn")) {
        btn.textContent = on ? "\\u2713" : "+";
      } else {
        btn.textContent = on ? "\\u2713 In your cart" : "+ Add to cart";
      }
    });
  }
  function renderCartPage(slugs) {
    var list = document.getElementById("cart-list");
    if (!list) return;
    var empty = document.getElementById("cart-empty");
    var summary = document.getElementById("cart-summary");
    var checkout = document.getElementById("cart-checkout");
    list.innerHTML = "";
    if (!slugs.length) {
      if (empty) empty.hidden = false;
      if (summary) summary.hidden = true;
      return;
    }
    if (empty) empty.hidden = true;
    if (summary) summary.hidden = false;
    slugs.forEach(function (slug) {
      var p = PRODUCTS[slug];
      var li = document.createElement("li");
      li.className = "cart-item";
      var a = document.createElement("a");
      a.className = "cart-item-link";
      a.href = prefix() + "products/" + slug + ".html";
      var img = document.createElement("img");
      img.src = prefix() + p.img;
      img.alt = "";
      var span = document.createElement("span");
      span.textContent = p.t;
      a.appendChild(img);
      a.appendChild(span);
      var price = document.createElement("div");
      price.className = "price";
      price.setAttribute("data-price-asin", p.asin);
      price.textContent = "Price on Amazon";
      var rm = document.createElement("button");
      rm.type = "button";
      rm.className = "cart-remove";
      rm.setAttribute("aria-label", "Remove " + p.t + " from your cart");
      rm.textContent = "\\u00d7";
      rm.addEventListener("click", function () { toggle(slug); });
      li.appendChild(a);
      li.appendChild(price);
      li.appendChild(rm);
      list.appendChild(li);
    });
    if (checkout) checkout.href = cartUrl(slugs);
    if (window.ZRB_prices && window.ZRB_prices.refresh) window.ZRB_prices.refresh();
  }
  function render() {
    var slugs = load();
    updateCounts(slugs);
    syncButtons(slugs);
    renderCartPage(slugs);
  }
  function toggle(slug) {
    var slugs = load();
    var i = slugs.indexOf(slug);
    if (i === -1) slugs.push(slug); else slugs.splice(i, 1);
    save(slugs);
    render();
  }
  document.querySelectorAll(".js-save").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      toggle(btn.dataset.slug);
    });
  });
  var clearBtn = document.getElementById("cart-clear");
  if (clearBtn) clearBtn.addEventListener("click", function () { save([]); render(); });
  render();
})();
"""


# ---------------- prices (live Amazon prices, never typed) ----------------
PRICES_JS = """// Zero Regret Buys — prices. Fetches live Amazon prices from /api/prices
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
"""


def write(path, content):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    write("site.js", SITE_JS)
    cart_index = json.dumps({
        p["slug"]: {"t": p["title"],
                    "img": p["photos"][0] if p.get("photos") else "",
                    "asin": p["asin"]}
        for p in PRODUCTS
    })
    write("cart.js", CART_JS.replace("__TAG__", TAG).replace("__PRODUCTS_JSON__", cart_index))
    write("prices.js", PRICES_JS)
    write("index.html", build_index())
    write("shop.html", build_shop())
    write("cart.html", build_cart())
    write("about.html", build_about())
    write("404.html", build_404())
    write("terms.html", build_terms())
    write("privacy.html", build_privacy())
    for p in PRODUCTS:
        write("products/%s.html" % p["slug"], build_product(p))


if __name__ == "__main__":
    main()
