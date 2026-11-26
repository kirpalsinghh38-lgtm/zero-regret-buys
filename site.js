// Zero Regret Buys — shop search, filter and sort. Dependency-free.
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
