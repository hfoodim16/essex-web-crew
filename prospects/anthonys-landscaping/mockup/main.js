/* Anthony's Landscaping — Evening Estate
   SPA navigation + reduced-motion-safe micro-interactions. */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var coarsePointer = window.matchMedia("(pointer: coarse)").matches;

  document.getElementById("year").textContent = new Date().getFullYear();

  /* ---------------------------------------------------------------
     SPA page navigation (data-page)
  --------------------------------------------------------------- */
  var pages = Array.prototype.slice.call(document.querySelectorAll(".page"));
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".nav-link"));
  var header = document.getElementById("siteHeader");
  var nav = document.querySelector(".site-nav");
  var navToggle = document.getElementById("navToggle");

  var pageIds = pages.map(function (p) { return p.id; });

  function setActivePage(id, skipScroll) {
    if (pageIds.indexOf(id) === -1) { id = "page-home"; }
    pages.forEach(function (p) {
      var active = p.id === id;
      p.classList.toggle("is-active", active);
      if (active) { p.removeAttribute("hidden"); }
      else { p.setAttribute("hidden", ""); }
    });
    navLinks.forEach(function (l) {
      l.classList.toggle("is-active", l.getAttribute("data-page") === id);
    });
    if (history.replaceState) { history.replaceState(null, "", "#" + id); }
    // re-arm reveals on the newly shown page
    primeReveals(document.getElementById(id));
    if (!skipScroll) { window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" }); }
    onScroll();
  }

  function closeMobileNav() {
    if (nav) { nav.classList.remove("open"); }
    if (navToggle) { navToggle.setAttribute("aria-expanded", "false"); navToggle.setAttribute("aria-label", "Open menu"); }
  }

  document.addEventListener("click", function (e) {
    var pageLink = e.target.closest("[data-page]");
    if (pageLink) {
      e.preventDefault();
      setActivePage(pageLink.getAttribute("data-page"));
      closeMobileNav();
      return;
    }
    var scrollLink = e.target.closest("[data-scroll]");
    if (scrollLink) {
      e.preventDefault();
      var target = document.getElementById(scrollLink.getAttribute("data-scroll"));
      if (target) { target.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" }); }
    }
  });

  if (navToggle) {
    navToggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
      navToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
  }

  /* ---------------------------------------------------------------
     Header background on scroll
  --------------------------------------------------------------- */
  function onScroll() {
    if (window.scrollY > 24) { header.classList.add("scrolled"); }
    else { header.classList.remove("scrolled"); }
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------------------------------------------------------------
     Reveal on scroll (IntersectionObserver)
  --------------------------------------------------------------- */
  var observer = null;
  if (!reduceMotion && "IntersectionObserver" in window) {
    observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry, i) {
        if (entry.isIntersecting) {
          var el = entry.target;
          el.style.transitionDelay = Math.min(i * 80, 240) + "ms";
          el.classList.add("in");
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
  }

  function primeReveals(scope) {
    var root = scope || document;
    var items = Array.prototype.slice.call(root.querySelectorAll(".reveal"));
    if (reduceMotion || !observer) {
      items.forEach(function (el) { el.classList.add("in"); });
      return;
    }
    items.forEach(function (el) {
      if (!el.classList.contains("in")) { observer.observe(el); }
    });
  }
  // deep-link support: honor #page-* on load
  var initialHash = window.location.hash.replace("#", "");
  if (initialHash && pageIds.indexOf(initialHash) !== -1) {
    setActivePage(initialHash, true);
  } else {
    primeReveals(document.querySelector(".page.is-active"));
  }

  if (reduceMotion) { return; } // stop here — no cursor/tilt/magnetic

  /* ---------------------------------------------------------------
     Custom cursor (dot + lerped ring) — pointer:fine only
  --------------------------------------------------------------- */
  if (!coarsePointer) {
    var dot = document.querySelector(".cursor-dot");
    var ring = document.querySelector(".cursor-ring");
    var label = document.querySelector(".cursor-label");
    var mx = window.innerWidth / 2, my = window.innerHeight / 2;
    var rx = mx, ry = my;

    window.addEventListener("mousemove", function (e) {
      mx = e.clientX; my = e.clientY;
      dot.style.transform = "translate(" + mx + "px," + my + "px) translate(-50%,-50%)";
      document.body.classList.add("cursor-active");
    });
    window.addEventListener("mouseleave", function () { document.body.classList.remove("cursor-active"); });

    (function loop() {
      rx += (mx - rx) * 0.18;
      ry += (my - ry) * 0.18;
      ring.style.transform = "translate(" + rx + "px," + ry + "px) translate(-50%,-50%)";
      requestAnimationFrame(loop);
    })();

    var hoverTargets = "a, button, .index-panel, .gallery-item, .sig-card, [data-cursor]";
    document.addEventListener("mouseover", function (e) {
      var t = e.target.closest(hoverTargets);
      if (t) {
        document.body.classList.add("cursor-hover");
        label.textContent = t.getAttribute("data-cursor") || "View";
      }
    });
    document.addEventListener("mouseout", function (e) {
      var t = e.target.closest(hoverTargets);
      if (t && !e.relatedTarget) { document.body.classList.remove("cursor-hover"); }
      else if (t && !t.contains(e.relatedTarget)) { document.body.classList.remove("cursor-hover"); }
    });
  }

  /* ---------------------------------------------------------------
     Magnetic buttons (hero CTAs + nav estimate)
  --------------------------------------------------------------- */
  if (!coarsePointer) {
    var magnets = document.querySelectorAll(".hero-cta .btn, .btn-estimate");
    magnets.forEach(function (btn) {
      btn.addEventListener("mousemove", function (e) {
        var r = btn.getBoundingClientRect();
        var x = e.clientX - r.left - r.width / 2;
        var y = e.clientY - r.top - r.height / 2;
        btn.style.transform = "translate(" + x * 0.25 + "px," + y * 0.35 + "px)";
      });
      btn.addEventListener("mouseleave", function () { btn.style.transform = ""; });
    });
  }

  /* ---------------------------------------------------------------
     Subtle 3D tilt (max 3deg) on gallery/index/sig cards — no touch
  --------------------------------------------------------------- */
  if (!coarsePointer) {
    var tilts = document.querySelectorAll(".tilt");
    tilts.forEach(function (card) {
      card.addEventListener("mousemove", function (e) {
        var r = card.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = "perspective(900px) rotateY(" + (px * 3) + "deg) rotateX(" + (-py * 3) + "deg)";
      });
      card.addEventListener("mouseleave", function () { card.style.transform = ""; });
    });
  }

  /* ---- Estimate form (demo - no real submit) ---------------------------- */
  var estForm = document.querySelector('.form-shell');
  if (estForm) {
    estForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = estForm.querySelector('.form-result');
      if (note) {
        note.textContent = 'Thanks \u2014 this is a demo form. On the live site this reaches the office directly. For now, please call (973) 763-6566.';
        note.hidden = false;
      }
    });
  }

})();
