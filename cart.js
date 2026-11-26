// Zero Regret Buys — cart. Add products, view them on the cart page,
// check out by loading them all into an Amazon cart.
// Runs on every page; the shop filter (site.js) is separate and untouched.
(function () {
  "use strict";
  var TAG = "zeroregretb04-20";
  var KEY = "zrb-cart";
  var OLD_KEY = "zrb-shortlist";
  var PRODUCTS = {"magnesium-glycinate": {"t": "Magnesium Bisglycinate", "img": "images/products/mg-glycinate-webber-1.jpg", "asin": "B08WVD2YDB"}, "creatine-monohydrate": {"t": "Creatine Monohydrate", "img": "images/products/creatine-monohydrate-2.jpg", "asin": "B0043YLNSC"}, "omega-3-fish-oil": {"t": "Omega-3 Fish Oil", "img": "images/products/omega-3-1.jpg", "asin": "B079NP724M"}, "zinc-citrate": {"t": "Zinc Citrate", "img": "images/products/zinc-citrate.jpg", "asin": "B009D9NIGW"}, "vitamin-d3-k2": {"t": "Vitamin D3 + K2", "img": "images/products/vitamin-d3-k2.jpg", "asin": "B08WNTMWRV"}, "vichy-dercos": {"t": "Vichy Dercos Anti-Dandruff Shampoo", "img": "images/products/vichy-dercos.jpg", "asin": "B01BPHAD1W"}, "retinal-shot-booster": {"t": "celimax Vita A Retinal Shot Tightening Booster", "img": "images/products/retinal-shot-celimax.webp", "asin": "B0DK4Y2YP3"}, "dr-althea-345": {"t": "Dr. Althea 345 Relief Cream", "img": "images/products/dr-althea-345.jpg", "asin": "B07PK2P2XB"}, "axis-y-dark-spot": {"t": "Axis-Y Dark Spot Correcting Glow Serum", "img": "images/products/axis-y-dark-spot.jpg", "asin": "B091238V7N"}, "arencia-rice-cleanser": {"t": "Arencia Fresh Green Rice Mochi Cleanser", "img": "images/products/arencia-rice-cleanser.jpg", "asin": "B0C1BMWPR2"}, "complex-15-cream": {"t": "Complex 15 Daily Face Cream", "img": "images/products/complex-15.jpg", "asin": "B00BPDF0YC"}, "azelaic-acid-10": {"t": "The Ordinary Azelaic Acid Suspension 10%", "img": "images/products/azelaic-acid-10.png", "asin": "B06WD5J8KY"}, "ashwagandha-ksm66": {"t": "Webber Naturals Ashwagandha 7200mg (KSM-66)", "img": "images/products/ashwagandha-ksm66.jpg", "asin": "B0B8PGT48W"}, "organika-collagen": {"t": "Organika Enhanced Collagen Powder", "img": "images/products/organika-collagen.jpg", "asin": "B01MZ1FC46"}, "probiotic-30b": {"t": "Webber Naturals Probiotic 30 Billion", "img": "images/products/probiotic-30b.jpg", "asin": "B00L3WSHDG"}, "truskin-vitamin-c": {"t": "TruSkin Vitamin C Serum", "img": "images/products/truskin-vitamin-c.jpg", "asin": "B01M4MCUAF"}, "ordinary-hyaluronic": {"t": "The Ordinary Hyaluronic Acid 2% + B5", "img": "images/products/ordinary-hyaluronic.jpg", "asin": "B01MYEZPC8"}, "ombrelle-spf60": {"t": "Garnier Ombrelle Anti-Shine SPF 60", "img": "images/products/ombrelle-spf60.jpg", "asin": "B081DNB1B2"}, "myhalos-sleep-mask": {"t": "MyHalos 3D Blackout Sleep Mask", "img": "images/products/myhalos-sleep-mask.jpg", "asin": "B09CZ68WV3"}, "schiara-posture": {"t": "Schiara Posture Corrector", "img": "images/products/schiara-posture.jpg", "asin": "B07VST9VYH"}, "philips-wake-up": {"t": "Philips SmartSleep Wake-Up Light", "img": "images/products/philips-wake-up.jpg", "asin": "B0093162RM"}, "b12-2500": {"t": "Nature's Bounty Vitamin B12 2500mcg", "img": "images/products/b12-2500.jpg", "asin": "B00BMEHEXE"}, "turmeric-curcumin": {"t": "Webber Naturals Turmeric Curcumin + Black Pepper", "img": "images/products/turmeric-curcumin.jpg", "asin": "B09T8PKKRG"}, "melatonin-10mg": {"t": "Jamieson Melatonin 10mg Dual-Action", "img": "images/products/melatonin-10mg.jpg", "asin": "B0797NJW1Q"}, "cerave-cream": {"t": "CeraVe Moisturizing Cream", "img": "images/products/cerave-cream.jpg", "asin": "B083GGFTPW"}, "ordinary-niacinamide": {"t": "The Ordinary Niacinamide 10% + Zinc 1%", "img": "images/products/ordinary-niacinamide.jpg", "asin": "B01MDTVZTZ"}, "hydro-boost-gel": {"t": "Neutrogena Hydro Boost Gel Cream", "img": "images/products/hydro-boost-gel.jpg", "asin": "B00YPBGIIS"}, "acupressure-mat": {"t": "ELEBOX Acupressure Mat + Pillow Set", "img": "images/products/acupressure-mat.jpg", "asin": "B07M9CGZNY"}, "scalp-massager": {"t": "Comfier Cordless Scalp Massager", "img": "images/products/scalp-massager.jpg", "asin": "B08KGD8JWK"}, "olaplex-no3": {"t": "Olaplex No.3 Hair Perfector", "img": "images/products/olaplex-no3.jpg", "asin": "B08TWTQDCX"}};

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
        btn.textContent = on ? "\u2713" : "+";
      } else {
        btn.textContent = on ? "\u2713 In your cart" : "+ Add to cart";
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
      rm.textContent = "\u00d7";
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
