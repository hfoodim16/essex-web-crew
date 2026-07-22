/* Happy Trees by MGM — interactions (all motion reduced-motion-gated) */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Mobile menu ---- */
  var burger = document.getElementById('hamburger');
  var nav = document.getElementById('nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        burger.setAttribute('aria-label', 'Open menu');
        document.body.style.overflow = '';
      }
    });
    // close on resize up to desktop
    window.addEventListener('resize', function () {
      if (window.innerWidth > 760 && nav.classList.contains('open')) {
        nav.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
  }

  /* ---- Reveal on scroll ---- */
  var reveals = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    reveals.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ---- Rope draw on scroll ---- */
  var ropePath = document.getElementById('ropePath');
  var ropeNode = document.getElementById('ropeNode');
  var ropeWrap = document.querySelector('.rope-wrap');
  if (ropePath && ropeWrap) {
    var len = ropePath.getTotalLength();
    if (reduce) {
      ropePath.style.strokeDasharray = 'none';
      if (ropeNode) ropeNode.setAttribute('cy', 1000);
    } else {
      ropePath.style.strokeDasharray = len;
      ropePath.style.strokeDashoffset = len;
      var ticking = false;
      var update = function () {
        ticking = false;
        var rect = ropeWrap.getBoundingClientRect();
        var vh = window.innerHeight;
        // progress: 0 when top of wrap hits ~40% viewport, 1 when bottom passes ~70%
        var start = vh * 0.55;
        var total = rect.height + start - vh * 0.3;
        var scrolled = start - rect.top;
        var p = Math.max(0, Math.min(1, scrolled / total));
        ropePath.style.strokeDashoffset = (len * (1 - p)).toFixed(1);
        if (ropeNode) {
          var pt = ropePath.getPointAtLength(len * p);
          ropeNode.setAttribute('cx', pt.x);
          ropeNode.setAttribute('cy', pt.y);
        }
      };
      var onScroll = function () {
        if (!ticking) { ticking = true; requestAnimationFrame(update); }
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      window.addEventListener('resize', onScroll, { passive: true });
      update();
    }
  }

  /* ---- Subtle magnetic pull on primary buttons (fine pointers only) ---- */
  if (!reduce && window.matchMedia('(pointer: fine)').matches) {
    document.querySelectorAll('.btn-primary').forEach(function (btn) {
      btn.addEventListener('pointermove', function (e) {
        var r = btn.getBoundingClientRect();
        var mx = (e.clientX - r.left - r.width / 2) * 0.14;
        var my = (e.clientY - r.top - r.height / 2) * 0.22;
        btn.style.transform = 'translate(' + mx.toFixed(1) + 'px,' + (my - 2).toFixed(1) + 'px)';
      });
      btn.addEventListener('pointerleave', function () { btn.style.transform = ''; });
    });
  }
})();
