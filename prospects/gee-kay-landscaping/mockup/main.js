/* Gee-Kay Landscaping — Heritage Ledger interactions
   SPA page routing + whisper-level motion, all gated behind prefers-reduced-motion.
   Cursor / magnetic effects disabled on coarse pointers. */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  document.getElementById("year").textContent = String(new Date().getFullYear());

  /* ---------------- SPA page routing ---------------- */
  var pages = Array.prototype.slice.call(document.querySelectorAll(".page"));
  var navLinks = Array.prototype.slice.call(document.querySelectorAll("[data-page]"));
  var navMenu = document.getElementById("navMenu");
  var navToggle = document.getElementById("navToggle");

  function setPage(name, opts) {
    opts = opts || {};
    var found = false;
    pages.forEach(function (p) {
      var isTarget = p.id === "page-" + name;
      if (isTarget) found = true;
      p.hidden = !isTarget;
      p.classList.toggle("is-active", isTarget);
    });
    if (!found) return;

    document.querySelectorAll(".nav-link[data-page]").forEach(function (l) {
      l.classList.toggle("is-active", l.getAttribute("data-page") === name);
    });

    // reset + replay reveals for the freshly shown page
    var active = document.getElementById("page-" + name);
    if (active) initReveals(active);

    if (!opts.noScroll) window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
    if (history.replaceState) history.replaceState(null, "", "#" + name);
  }

  navLinks.forEach(function (link) {
    link.addEventListener("click", function (e) {
      var name = link.getAttribute("data-page");
      if (!name) return;
      e.preventDefault();
      setPage(name);
      closeNav();
    });
  });

  /* ---------------- Mobile nav ---------------- */
  function openNav() {
    navMenu.classList.add("is-open");
    navToggle.setAttribute("aria-expanded", "true");
  }
  function closeNav() {
    navMenu.classList.remove("is-open");
    navToggle.setAttribute("aria-expanded", "false");
  }
  navToggle.addEventListener("click", function () {
    if (navMenu.classList.contains("is-open")) closeNav();
    else openNav();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeNav();
  });

  /* ---------------- Sticky header shadow ---------------- */
  var header = document.getElementById("siteHeader");
  function onScroll() {
    if (window.scrollY > 8) header.classList.add("is-scrolled");
    else header.classList.remove("is-scrolled");
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------------- Reveal on scroll + ledger draw + count-up ---------------- */
  var revealObserver = null;

  function drawLedger(scope) {
    if (reduceMotion) return;
    scope.querySelectorAll(".ledger-rule, .ledger-double span").forEach(function (rule) {
      rule.style.transform = "scaleX(0)";
      requestAnimationFrame(function () {
        rule.style.transition = "transform 0.6s " + "cubic-bezier(0.16,1,0.3,1)";
        rule.style.transform = "scaleX(1)";
      });
    });
  }

  function countUp(el) {
    if (reduceMotion) return;
    var target = parseFloat(el.getAttribute("data-count"));
    if (isNaN(target)) return;
    var decimals = parseInt(el.getAttribute("data-decimals") || "0", 10);
    var suffix = el.getAttribute("data-suffix") || "";
    var start = performance.now();
    var dur = 1100;
    function tick(now) {
      var t = Math.min((now - start) / dur, 1);
      var eased = 1 - Math.pow(1 - t, 3);
      var val = target * eased;
      el.textContent = val.toFixed(decimals) + (t >= 1 ? "" : "");
      if (t >= 1) el.textContent = target.toFixed(decimals);
      if (t < 1) requestAnimationFrame(tick);
    }
    el.textContent = (0).toFixed(decimals);
    requestAnimationFrame(tick);
  }

  function initReveals(scope) {
    var els = Array.prototype.slice.call(scope.querySelectorAll(".reveal"));
    if (reduceMotion || !("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("is-visible"); });
      scope.querySelectorAll("[data-count]").forEach(function (el) {
        var d = parseInt(el.getAttribute("data-decimals") || "0", 10);
        el.textContent = parseFloat(el.getAttribute("data-count")).toFixed(d);
      });
      return;
    }

    // reset state so a revisited page re-animates
    els.forEach(function (el) { el.classList.remove("is-visible"); });

    if (revealObserver) revealObserver.disconnect();
    revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        el.classList.add("is-visible");
        drawLedger(el);
        el.querySelectorAll("[data-count]").forEach(countUp);
        revealObserver.unobserve(el);
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -8% 0px" });

    var i = 0;
    els.forEach(function (el) {
      // stagger cards within a grid
      el.style.transitionDelay = (Math.min(i % 3, 2) * 60) + "ms";
      i++;
      revealObserver.observe(el);
    });
  }

  /* ---------------- Magnetic buttons ---------------- */
  function initMagnetic() {
    if (reduceMotion || !finePointer) return;
    document.querySelectorAll(".magnetic").forEach(function (btn) {
      btn.addEventListener("mousemove", function (e) {
        var r = btn.getBoundingClientRect();
        var mx = e.clientX - (r.left + r.width / 2);
        var my = e.clientY - (r.top + r.height / 2);
        btn.style.transform = "translate(" + (mx * 0.18).toFixed(2) + "px," + (my * 0.28).toFixed(2) + "px)";
      });
      btn.addEventListener("mouseleave", function () {
        btn.style.transform = "";
      });
    });
  }

  /* ---------------- Custom cursor ---------------- */
  function initCursor() {
    if (reduceMotion || !finePointer) return;
    var dot = document.querySelector(".cursor-dot");
    var ring = document.querySelector(".cursor-ring");
    var label = document.querySelector(".cursor-label");
    if (!dot || !ring) return;
    document.body.classList.add("has-cursor");

    var mx = window.innerWidth / 2, my = window.innerHeight / 2;
    var rx = mx, ry = my;

    window.addEventListener("mousemove", function (e) {
      mx = e.clientX; my = e.clientY;
      dot.style.transform = "translate(" + mx + "px," + my + "px) translate(-50%,-50%)";
    });

    function loop() {
      rx += (mx - rx) * 0.16;
      ry += (my - ry) * 0.16;
      ring.style.transform = "translate(" + rx + "px," + ry + "px) translate(-50%,-50%)";
      requestAnimationFrame(loop);
    }
    loop();

    document.querySelectorAll("[data-cursor], a, button").forEach(function (el) {
      el.addEventListener("mouseenter", function () {
        var text = el.getAttribute("data-cursor");
        if (text) {
          label.textContent = text;
          ring.classList.add("is-active");
        }
      });
      el.addEventListener("mouseleave", function () {
        ring.classList.remove("is-active");
        label.textContent = "";
      });
    });

    document.addEventListener("mouseleave", function () {
      dot.style.opacity = "0"; ring.style.opacity = "0";
    });
    document.addEventListener("mouseenter", function () {
      dot.style.opacity = "1"; ring.style.opacity = "1";
    });
  }

  /* ---------------- Boot ---------------- */
  var initial = (location.hash || "").replace("#", "");
  if (initial && document.getElementById("page-" + initial)) {
    setPage(initial, { noScroll: true });
  } else {
    initReveals(document.getElementById("page-home"));
  }

  initMagnetic();
  initCursor();
})();
