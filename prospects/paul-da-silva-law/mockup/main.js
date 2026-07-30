/* ==========================================================================
   DaSilva & Associates, LLC — "Counsel of Record" (Rev 3)

   Motion: line-draw entrance (rules draw in, content settles 8px behind them)
   + weight-shift hover (CSS only, variable Albert Sans) + one scroll set-piece
   (the sticky index rail on practice-areas.html). No GSAP, no parallax.

   Rule 0: nothing on this page is hidden by the stylesheet alone. Hidden
   entrance states live behind html.js, and the first thing this file does is
   cancel the dead-man timer set in the <head> — so if this script never loads,
   .js is stripped and the page renders finished.
   ========================================================================== */
(function () {
  "use strict";

  if (window.__revealFail) { clearTimeout(window.__revealFail); }

  var motionOK = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- 1. Mobile menu ------------------------------------------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", open ? "false" : "true");
      nav.classList.toggle("open", !open);
    });
    // Tapping a link closes the sheet
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        toggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("open");
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        toggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("open");
        toggle.focus();
      }
    });
  }

  /* ---------- 2. Sticky masthead: condensing bar ------------------------ */
  var deck = document.getElementById("deck-main");
  if (deck) {
    var onScroll = function () {
      deck.classList.toggle("stuck", window.scrollY > 48);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- 3. Line-draw entrance ------------------------------------ */
  /* Position-driven rather than IntersectionObserver on purpose: half the
     authored elements here are the rules themselves, and a rule at
     transform:scaleX(0) has zero area — an IO threshold can never be met by a
     zero-area box, so the rules would never draw. Each element reveals once
     when its top crosses 88% of the viewport, then leaves the queue. */
  var pending = Array.prototype.slice.call(document.querySelectorAll(".settle, .drawx, .cells"));

  if (!motionOK) {
    pending.forEach(function (el) { el.classList.add("in"); });
    pending = [];
  } else {
    var timer = null;
    var sweep = function () {
      timer = null;
      var line = window.innerHeight * 0.88;
      for (var k = pending.length - 1; k >= 0; k--) {
        if (pending[k].getBoundingClientRect().top < line) {
          pending[k].classList.add("in");
          pending.splice(k, 1);
        }
      }
      if (!pending.length) {
        window.removeEventListener("scroll", onMove);
        window.removeEventListener("resize", onMove);
      }
    };
    /* Timer-throttled, not rAF-throttled: a backgrounded or throttled tab pins
       rAF at zero frames, and a reveal that never runs is a blank page. The
       call is trailing, so a burst of scroll events that stops abruptly still
       ends in a sweep. */
    var onMove = function () {
      if (timer) { return; }
      timer = setTimeout(sweep, 60);
    };
    sweep();
    window.addEventListener("scroll", onMove, { passive: true });
    window.addEventListener("resize", onMove);
    // Fonts landing can shift positions; re-check once they do.
    if (document.fonts && document.fonts.ready) { document.fonts.ready.then(onMove); }
  }

  /* ---------- 4. Set-piece: sticky index rail (practice-areas.html) ----- */
  var railList = document.getElementById("rail-list");
  if (railList) {
    var links = Array.prototype.slice.call(railList.querySelectorAll("a"));
    var mark = railList.querySelector(".rail-mark");
    var sections = links
      .map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); })
      .filter(Boolean);

    var setCurrent = function (id) {
      links.forEach(function (a) {
        var on = a.getAttribute("href") === "#" + id;
        if (on) {
          a.setAttribute("aria-current", "true");
          if (mark) {
            mark.style.height = a.offsetHeight + "px";
            mark.style.transform = "translateY(" + a.offsetTop + "px)";
          }
        } else {
          a.removeAttribute("aria-current");
        }
      });
    };

    if (sections.length) {
      /* Whichever section has most recently crossed the reading line owns the
         rail. Computed from position rather than observed, so a jump straight
         to an anchor (or back to the top) lands on the right item. */
      var readLine = function () { return window.innerHeight * 0.3; };
      var pick = function () {
        railTimer = null;
        var line = readLine(), best = sections[0], bestTop = -Infinity;
        sections.forEach(function (s) {
          var top = s.getBoundingClientRect().top;
          if (top <= line && top > bestTop) { bestTop = top; best = s; }
        });
        setCurrent(best.id);
      };
      var railTimer = null;
      var onRail = function () {
        if (railTimer) { return; }
        railTimer = setTimeout(pick, 80);
      };
      pick();
      window.addEventListener("scroll", onRail, { passive: true });
      window.addEventListener("resize", onRail);
    }
  }

  /* ---------- 5. Demo contact form ------------------------------------- */
  var form = document.getElementById("contact-form");
  if (form) {
    var result = form.querySelector(".form-result");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!result) { return; }
      result.textContent =
        "Thanks — this is a demo form. On the live site this reaches Paul Da Silva's " +
        "office directly. For now, please call 973-344-0808.";
      result.hidden = false;
      result.setAttribute("tabindex", "-1");
      result.focus();
    });
  }
})();
