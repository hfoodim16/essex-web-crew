/* DaSilva & Associates — shared behavior (loaded on every page) */
(function () {
  "use strict";
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  /* ---------- Mobile nav toggle ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
    });
  }

  /* ---------- Clip-wipe reveal on scroll ---------- */
  var revealEls = document.querySelectorAll(".reveal, .reveal-up");
  if (revealEls.length) {
    if (reduceMotion || !("IntersectionObserver" in window)) {
      revealEls.forEach(function (el) { el.classList.add("in"); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
      revealEls.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---------- Subtle card tilt (fine pointer only) ---------- */
  if (finePointer && !reduceMotion) {
    document.querySelectorAll(".tilt").forEach(function (el) {
      el.addEventListener("mousemove", function (ev) {
        var r = el.getBoundingClientRect();
        var px = (ev.clientX - r.left) / r.width - 0.5;
        var py = (ev.clientY - r.top) / r.height - 0.5;
        el.style.transform = "perspective(700px) rotateX(" + (-py * 2).toFixed(2) + "deg) rotateY(" + (px * 2).toFixed(2) + "deg) translateY(-4px)";
      });
      el.addEventListener("mouseleave", function () { el.style.transform = ""; });
    });
  }

  /* ---------- Hero parallax (fine pointer, motion on, hero only) ---------- */
  if (finePointer && !reduceMotion) {
    var heroImg = document.querySelector(".hero-media img");
    if (heroImg) {
      window.addEventListener("scroll", function () {
        var y = window.scrollY;
        if (y < window.innerHeight) heroImg.style.transform = "scale(1.06) translateY(" + (y * 0.06).toFixed(1) + "px)";
      }, { passive: true });
    }
  }

  /* ---------- Placeholder contact form (demo only, no network) ---------- */
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var result = form.querySelector(".form-result");
      if (result) {
        result.hidden = false;
        result.textContent = "Thanks — this is a demo form. On the live site this reaches the office directly. For now, please call 973-344-0808 and we'll take it from there.";
        result.setAttribute("role", "status");
        form.querySelector("button[type=submit]").disabled = true;
      }
    });
  }
})();
