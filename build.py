"""Zero Regret Buys — v2 builder (from-scratch rebuild, 2026-11-25).

Customer first: a shop, not a story. Products up front, almost no
paragraphs. All content (products, links, photos, copy) comes from
data.py untouched, so every affiliate link, ASIN and photo is identical
to v1. This file holds only the new design: templates + page assembly.
"""
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

NAV = [("index.html", "Home"), ("shop.html", "Shop"), ("about.html", "About")]

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


def head(title, desc, path, root):
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
<meta name="theme-color" content="#faf9f6">
<link rel="icon" href="%simages/logo.jpg">
<link rel="stylesheet" href="%sstyles.css">
</head>
<body>
""" % (title, desc, title, desc, BASE, path, BASE, root, root)


def header(root, current, tab=True):
    links = "".join(
        '<a href="%s%s"%s>%s</a>' % (root, href, ' aria-current="page"' if href == current else "", label)
        for href, label in NAV
    )
    tabbar = ("""
<nav class="tabbar" aria-label="Mobile">
  %s
</nav>""" % "".join(
        '<a href="%s%s"%s>%s<span>%s</span></a>'
        % (root, href, ' aria-current="page"' if href == current else "",
           TAB_ICONS[href][0], TAB_ICONS[href][1])
        for href in TAB_ICONS)) if tab else ""
    return """
<header class="site-header">
  <div class="header-inner">
    <a class="brandmark" href="%sindex.html" aria-label="Zero Regret Buys — home">
      <img class="logoimg" src="%simages/logo.jpg" alt="Zero Regret Buys logo">
      <span class="wordmark">Zero Regret Buys<small>THIRTY PICKS · ZERO REGRET</small></span>
    </a>
    <nav class="mainnav" aria-label="Primary">
      %s
      <a class="nav-cta" href="%sshop.html"><span class="cta-full">Browse the picks</span><span class="cta-short">Browse</span></a>
    </nav>
  </div>
</header>
%s
""" % (root, root, links, root, tabbar)


def footer(root):
    return """
</main>
<footer class="site-footer">
  <div class="footer-inner">
    <a class="brandmark" href="%sindex.html">
      <img class="logoimg" src="%simages/logo.jpg" alt="Zero Regret Buys logo">
      <span class="wordmark">Zero Regret Buys<small>THIRTY PICKS · ZERO REGRET</small></span>
    </a>
    <nav aria-label="Footer">
      <a href="%sshop.html">Shop all picks</a>
      <a href="%sabout.html">About</a>
      <a href="%sterms.html">Terms</a>
      <a href="%sprivacy.html">Privacy</a>
    </nav>
    <p class="footer-disclosure">%s Product links on this site are affiliate (paid) links — if you buy through them, we may earn a commission at no extra cost to you. <a href="%sabout.html">Why this matters</a></p>
    <p class="footer-copy">© %s Zero Regret Buys</p>
  </div>
</footer>
<script src="%ssite.js"></script>
</body>
</html>
""" % (root, root, root, root, root, root, DISCLOSURE, root,
       datetime.now().year, root)


def badge(p):
    return '<span class="badge">Best for %s</span>' % BADGES[p["slug"]]


def search_blob(p):
    return "%s %s %s %s %s %s" % (
        p["title"], p["pitch"], p["cat"], p["sub"], BADGES[p["slug"]], p["keyword"])


def card(p, root, pitch=True):
    """One product card: photo, job, title, one line, buy button.
    pitch=False drops the pitch line (home grid: visual only)."""
    photo = p["photos"][0] if p.get("photos") else ""
    img = ('<img src="%s%s" alt="%s product photo" loading="lazy">'
           % (root, photo, p["title"])) if photo else ""
    pitch_html = '<p class="pitch">%s</p>' % p["pitch"] if pitch else ""
    return """
<article class="card" data-num="%(num)s" data-title="%(title)s"
         data-cat="%(cat_slug)s" data-sub="%(sub_slug)s" data-job="%(job)s"
         data-search="%(search)s">
  <a class="card-photo" href="%(root)sproducts/%(slug)s.html">%(img)s</a>
  <div class="card-body">
    %(badge)s
    <h3><a href="%(root)sproducts/%(slug)s.html">%(title)s</a></h3>
    %(pitch_html)s
    <a class="btn btn-shelf btn-block" href="%(url)s"
       target="_blank" rel="sponsored nofollow noopener">Check on Amazon</a>
    <div class="paidnote">(paid link)</div>
  </div>
</article>""" % {
        "num": p["num"], "title": p["title"], "cat_slug": p["cat_slug"],
        "sub_slug": p["sub_slug"], "job": JOB_BY_BADGE[BADGES[p["slug"]]],
        "search": search_blob(p), "root": root, "slug": p["slug"],
        "img": img, "badge": badge(p), "pitch_html": pitch_html, "url": p["url"],
    }


def cartall_block():
    return """
      <div class="cartall">
        <a class="btn btn-shelf btn-big" href="%s"
           target="_blank" rel="sponsored nofollow noopener">Add all 30 to cart on Amazon</a>
        <div class="paidnote">(paid link)</div>
        <p class="micro">One click loads all thirty picks into your Amazon.ca cart — remove anything you don’t want before checkout.</p>
      </div>""" % CART_ALL_HTML


# ---------------- index ----------------
def build_index():
    root = ""
    cards = "".join(card(p, root, pitch=False) for p in sorted(PRODUCTS, key=lambda p: p["num"], reverse=True))
    body = """
<main id="main">
  <div class="hero">
    <div class="wrap hero-copy">
      <h1>Thirty picks. Zero regret.</h1>
      <p class="sub">One job each. No hype, no typed prices.</p>
      <div class="hero-ctas">
        <a class="btn btn-shelf" href="#picks">See the picks</a>
        <a class="btn btn-outline" href="shop.html">Browse the shop</a>
      </div>
    </div>
  </div>

  <div class="wrap">
    <div class="section" id="picks">
      <div class="grid">
%s
      </div>
%s
    </div>
  </div>
""" % (cards, cartall_block())
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
    rows = "".join(
        '<tr><td><a href="products/%s.html">%s</a></td><td>%s</td>'
        '<td><a href="%s" target="_blank" rel="sponsored nofollow noopener">Check on Amazon</a> <span class="paidnote">(paid link)</span></td></tr>'
        % (p["slug"], p["title"], BADGES[p["slug"]], p["url"])
        for p in PRODUCTS)
    body = """
<main id="main">
  <div class="wrap">
    <div class="section">
      <h1>The Shop</h1>
      <p class="sub" style="color: var(--ink-soft); margin-top: 8px;">All thirty picks. Click through to see today’s live price.</p>
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
      <p class="empty" id="shop-empty" hidden>Nothing matches — try a different word.</p>
      <div class="cmp">
        <h2>Compare</h2>
        <div class="cmp-scroll">
          <table>
            <thead><tr><th>Pick</th><th>Best for</th><th>Amazon</th></tr></thead>
            <tbody>%s</tbody>
          </table>
        </div>
      </div>
%s
    </div>
  </div>
""" % (aisle_chips, shelf_chips, cards, rows, cartall_block())
    return (head("The Shop — Zero Regret Buys",
                 "All thirty picks in one place. Search, filter, compare — then check today’s live price on Amazon.",
                 "shop.html", root)
            + header(root, "shop.html") + body + footer(root))


# ---------------- product ----------------
def related(p):
    others = [q for q in PRODUCTS if q["slug"] != p["slug"]]
    same_sub = [q for q in others if q["sub_slug"] == p["sub_slug"]]
    same_cat = [q for q in others if q["cat_slug"] == p["cat_slug"] and q not in same_sub]
    return (same_sub + same_cat + others)[:3]


def build_product(p):
    root = "../"
    copy = PDP_COPY[p["slug"]]
    photo = p["photos"][0] if p.get("photos") else ""
    img = ('<img src="%s%s" alt="%s product photo">' % (root, photo, p["title"])) if photo else ""
    getif = "".join("<li>%s</li>" % g for g in copy["getif"])
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
          %(badge)s
          <h1>%(title)s</h1>
          <p class="key">%(key)s</p>
          <p class="verdict">%(verdict)s</p>
          <div class="pdp-buy">
            <a class="btn btn-shelf" href="%(url)s" target="_blank" rel="sponsored nofollow noopener">Check on Amazon</a>
            <a class="btn" href="%(cart_url)s" target="_blank" rel="sponsored nofollow noopener">Add to Cart on Amazon</a>
            <div class="paidnote">(paid links)</div>
          </div>
          <div class="getif">
            <h2>Get this if…</h2>
            <ul>%(getif)s</ul>
          </div>
          <div class="kwcard">
            <div class="kw">%(keyword)s</div>
            <p>Comment this word under the reel and the link lands in your DMs.</p>
          </div>
        </div>
      </div>
      <div class="more">
        <h2>More picks</h2>
        <div class="grid">
%(more)s
        </div>
      </div>
    </div>
  </div>
""" % {
        "cat_slug": p["cat_slug"], "cat": p["cat"], "title": p["title"],
        "img": img, "badge": badge(p), "key": copy["key"],
        "verdict": short_verdict(p), "url": p["url"],
        "cart_url": p["cart_url"], "getif": getif,
        "keyword": p["keyword"], "more": more,
    }
    return (head("%s — Zero Regret Buys" % p["title"],
                 meta_pitch(p["pitch"]),
                 "products/%s.html" % p["slug"], root)
            + header(root, "shop.html", tab=False) + body + footer(root))


# ---------------- about ----------------
def build_about():
    root = ""
    faqs = "".join(
        '<div class="faq-item"><h3>%s</h3><p>%s</p></div>' % (q, a)
        for q, a in FAQS)
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
      <p>Zero Regret Buys lists products featured in its short-form videos. Prices, availability and product details live on Amazon — what you see there is what counts, not anything typed here.</p>
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

  // Deep links (?cat= / ?sub=) apply on load; a sub implies its aisle
  // unless a cat was given explicitly.
  var params = new URLSearchParams(window.location.search);
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


def write(path, content):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    write("site.js", SITE_JS)
    write("index.html", build_index())
    write("shop.html", build_shop())
    write("about.html", build_about())
    write("404.html", build_404())
    write("terms.html", build_terms())
    write("privacy.html", build_privacy())
    for p in PRODUCTS:
        write("products/%s.html" % p["slug"], build_product(p))


if __name__ == "__main__":
    main()
