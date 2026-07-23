/* ═══════════════════════════════════════════════════════════
   COREY BLAKE'S STEAKHOUSE — main.js
   SPA routing · Animations · Custom cursor · Embers
═══════════════════════════════════════════════════════════ */

'use strict';

/* ── Utilities ── */
const $ = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

/* ── Reduced motion ── */
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ══════════════════════════════════════
   1. CUSTOM CURSOR
══════════════════════════════════════ */
(function initCursor() {
  if (window.matchMedia('(pointer: coarse)').matches) return;

  const dot  = $('#cursorDot');
  const ring = $('#cursorRing');

  /* Add label span inside ring */
  const label = document.createElement('span');
  label.className = 'cursor-label';
  ring.appendChild(label);

  let mx = -100, my = -100;
  let rx = -100, ry = -100;

  function lerp(a, b, t) { return a + (b - a) * t; }

  document.addEventListener('mousemove', e => {
    mx = e.clientX; my = e.clientY;
    dot.style.left = mx + 'px';
    dot.style.top  = my + 'px';
  });

  function animCursor() {
    rx = lerp(rx, mx, 0.12);
    ry = lerp(ry, my, 0.12);
    ring.style.left = rx + 'px';
    ring.style.top  = ry + 'px';
    requestAnimationFrame(animCursor);
  }
  animCursor();

  /* Cursor label map */
  const LABELS = {
    '[data-page="reservations"]': 'BOOK',
    '[data-page="menu"]':         'MENU',
    '[data-page="about"]':        'STORY',
    '[data-page="contact"]':      'TALK',
    '[data-page="home"]':         'HOME',
    '.cut-card':                  'VIEW',
    '.menu-item':                 'TASTE',
    '.btn-primary':               'GO',
    '.btn-outline':               'EXPLORE',
    '.filter-btn':                'FILTER',
  };

  function getCursorLabel(el) {
    for (const [sel, txt] of Object.entries(LABELS)) {
      if (el.closest(sel)) return txt;
    }
    return '';
  }

  document.addEventListener('mouseover', e => {
    const interactive = e.target.closest('a, button, [role="tab"], .cut-card, .menu-item');
    if (interactive) {
      const txt = getCursorLabel(interactive);
      ring.classList.add('hovered');
      if (txt) {
        ring.classList.add('labeled');
        label.textContent = txt;
      }
    }
  });

  document.addEventListener('mouseout', e => {
    if (e.target.closest('a, button, [role="tab"], .cut-card, .menu-item')) {
      ring.classList.remove('hovered', 'labeled');
      label.textContent = '';
    }
  });
})();

/* ══════════════════════════════════════
   1b. MAGNETIC BUTTONS
══════════════════════════════════════ */
(function initMagnetic() {
  if (window.matchMedia('(pointer: coarse)').matches) return;
  if (prefersReducedMotion) return;

  const STRENGTH = 0.38;
  const RADIUS   = 90;

  function attach(el) {
    let animId;

    el.addEventListener('mousemove', e => {
      const r   = el.getBoundingClientRect();
      const cx  = r.left + r.width  / 2;
      const cy  = r.top  + r.height / 2;
      const dx  = e.clientX - cx;
      const dy  = e.clientY - cy;
      const dist = Math.sqrt(dx*dx + dy*dy);

      if (dist < RADIUS) {
        cancelAnimationFrame(animId);
        const pull = (1 - dist / RADIUS) * STRENGTH;
        el.style.transform = `translate(${dx * pull}px, ${dy * pull}px)`;
      }
    });

    el.addEventListener('mouseleave', () => {
      /* Spring back */
      let vx = 0, vy = 0;
      let cx = parseFloat(el.style.transform.match(/translate\(([^,]+)/)?.[1]) || 0;
      let cy = parseFloat(el.style.transform.match(/,\s*([^p]+)px/)?.[1]) || 0;

      function spring() {
        const stiffness = 0.14, damping = 0.72;
        vx = vx * damping - cx * stiffness;
        vy = vy * damping - cy * stiffness;
        cx += vx; cy += vy;
        el.style.transform = `translate(${cx}px, ${cy}px)`;
        if (Math.abs(cx) > 0.1 || Math.abs(cy) > 0.1) {
          animId = requestAnimationFrame(spring);
        } else {
          el.style.transform = '';
        }
      }
      spring();
    });
  }

  /* Attach after page load so SPA nav picks up fresh elements */
  function attachAll() {
    $$('.btn-primary, .btn-outline, .nav-cta').forEach(attach);
  }

  document.addEventListener('DOMContentLoaded', attachAll);

  /* Re-attach on page navigation */
  const origNav = window.navigateTo;
  if (typeof origNav === 'function') {
    window.navigateTo = function(id) {
      origNav(id);
      setTimeout(attachAll, 420);
    };
  }
})();

/* ══════════════════════════════════════
   1c. 3D CARD TILT
══════════════════════════════════════ */
(function initTilt() {
  if (window.matchMedia('(pointer: coarse)').matches) return;
  if (prefersReducedMotion) return;

  const MAX_TILT = 8; /* degrees */

  function attachTilt(el) {
    el.style.transformStyle = 'preserve-3d';
    el.style.transition = 'transform 0.1s linear';

    el.addEventListener('mousemove', e => {
      const r  = el.getBoundingClientRect();
      const nx = (e.clientX - r.left)  / r.width  - 0.5; /* -0.5 … 0.5 */
      const ny = (e.clientY - r.top)   / r.height - 0.5;
      el.style.transition = 'transform 0.08s linear';
      el.style.transform  = `perspective(600px) rotateY(${nx * MAX_TILT}deg) rotateX(${-ny * MAX_TILT}deg) scale3d(1.02,1.02,1.02)`;
    });

    el.addEventListener('mouseleave', () => {
      el.style.transition = 'transform 0.55s cubic-bezier(0.22,1,0.36,1)';
      el.style.transform  = 'perspective(600px) rotateY(0deg) rotateX(0deg) scale3d(1,1,1)';
    });
  }

  function attachAllTilts() {
    $$('.cut-card').forEach(attachTilt);
  }

  document.addEventListener('DOMContentLoaded', attachAllTilts);

  const origNav = window.navigateTo;
  if (typeof origNav === 'function') {
    window.navigateTo = function(id) {
      origNav(id);
      setTimeout(attachAllTilts, 420);
    };
  }
})();

/* ══════════════════════════════════════
   1d. NAV LINK TEXT SCRAMBLE
══════════════════════════════════════ */
(function initScramble() {
  if (window.matchMedia('(pointer: coarse)').matches) return;
  if (prefersReducedMotion) return;

  const CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const STEPS = 6;
  const DELAY = 30; /* ms per step */

  function scramble(el) {
    const original = el.dataset.original || el.textContent;
    el.dataset.original = original;
    let step = 0;

    const id = setInterval(() => {
      el.textContent = original
        .split('')
        .map((ch, i) => {
          if (ch === ' ') return ' ';
          if (step / STEPS > i / original.length) return ch;
          return CHARS[Math.floor(Math.random() * CHARS.length)];
        })
        .join('');
      step++;
      if (step > STEPS + original.length) {
        clearInterval(id);
        el.textContent = original;
      }
    }, DELAY);
  }

  document.addEventListener('mouseover', e => {
    const link = e.target.closest('.nav-link, .mobile-link');
    if (link) scramble(link);
  });
})();

/* ══════════════════════════════════════
   2. NAVIGATION SCROLL BEHAVIOR
══════════════════════════════════════ */
(function initScrollHeader() {
  const header = $('#siteHeader');
  let ticking = false;

  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(() => {
        header.classList.toggle('scrolled', window.scrollY > 40);
        ticking = false;
      });
      ticking = true;
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

/* ══════════════════════════════════════
   3. MOBILE MENU
══════════════════════════════════════ */
(function initMobileMenu() {
  const btn    = $('#hamburger');
  const menu   = $('#mobileMenu');
  const close  = $('#mobileClose');

  function open() {
    menu.classList.add('open');
    menu.removeAttribute('aria-hidden');
    btn.classList.add('open');
    btn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function close_() {
    menu.classList.remove('open');
    menu.setAttribute('aria-hidden', 'true');
    btn.classList.remove('open');
    btn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  btn.addEventListener('click', () => menu.classList.contains('open') ? close_() : open());
  close.addEventListener('click', close_);

  menu.addEventListener('click', e => {
    if (e.target.closest('[data-page]')) close_();
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && menu.classList.contains('open')) close_();
  });
})();

/* ══════════════════════════════════════
   4. PAGE ROUTING (SPA)
══════════════════════════════════════ */
const pages    = $$('.page');
const navLinks = $$('[data-page]');
const overlay  = $('#pageTransition');

let currentPage = 'home';
let isAnimating = false;

function navigateTo(pageId) {
  if (pageId === currentPage || isAnimating) return;
  isAnimating = true;

  /* 1. Slide overlay down */
  overlay.classList.add('enter');

  setTimeout(() => {
    /* 2. Swap pages */
    pages.forEach(p => {
      if (p.id === 'page-' + pageId) {
        p.removeAttribute('hidden');
        p.classList.add('active');
      } else {
        p.setAttribute('hidden', '');
        p.classList.remove('active');
      }
    });

    /* 3. Update nav active state */
    navLinks.forEach(l => l.classList.toggle('active', l.dataset.page === pageId));

    currentPage = pageId;
    window.scrollTo({ top: 0, behavior: 'instant' });

    /* 4. Re-init reveals for new page */
    initReveal();

    /* 5. Stats counter on home */
    if (pageId === 'home') initCounters();

    /* 6. Menu filter binding */
    if (pageId === 'menu') initMenuFilter();

    /* 7. Slide overlay up */
    overlay.classList.remove('enter');
    overlay.classList.add('exit');

    setTimeout(() => {
      overlay.classList.remove('exit');
      isAnimating = false;
    }, 380);

  }, 350);
}

/* Wire all data-page links */
document.addEventListener('click', e => {
  const link = e.target.closest('[data-page]');
  if (!link) return;
  e.preventDefault();
  navigateTo(link.dataset.page);
});

/* ══════════════════════════════════════
   5. SCROLL REVEAL
══════════════════════════════════════ */
function initReveal() {
  if (prefersReducedMotion) {
    $$('.reveal-up, .reveal-fade, .reveal-word, .reveal-line-inner').forEach(el => {
      el.classList.add('visible');
    });
    return;
  }

  /* Wrap .reveal-line text in inner span for clip animation */
  $$('.reveal-line').forEach(line => {
    if (!line.querySelector('.reveal-line-inner')) {
      const inner = document.createElement('span');
      inner.className = 'reveal-line-inner';
      inner.textContent = line.textContent;
      line.textContent = '';
      line.appendChild(inner);
    }
  });

  const targets = $$('.reveal-up, .reveal-fade, .reveal-word, .reveal-line-inner');

  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  targets.forEach(el => io.observe(el));

  /* Hero reveals fire immediately */
  setTimeout(() => {
    $$('.hero .reveal-word').forEach((el, i) => {
      setTimeout(() => el.classList.add('visible'), i * 150);
    });
    $$('.hero .reveal-line-inner').forEach((el, i) => {
      setTimeout(() => el.classList.add('visible'), 200 + i * 200);
    });
    setTimeout(() => {
      $$('.hero .reveal-fade').forEach(el => el.classList.add('visible'));
    }, 700);
  }, 100);
}

/* ══════════════════════════════════════
   6. STAT COUNTERS
══════════════════════════════════════ */
function initCounters() {
  const counters = $$('[data-count]');
  if (!counters.length) return;

  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseInt(el.dataset.count, 10);
      const duration = prefersReducedMotion ? 0 : 1400;
      const start = performance.now();

      function tick(now) {
        const t = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - t, 3); /* ease-out-cubic */
        el.textContent = Math.round(eased * target);
        if (t < 1) requestAnimationFrame(tick);
        else el.textContent = target;
      }

      requestAnimationFrame(tick);
      io.unobserve(el);
    });
  }, { threshold: 0.5 });

  counters.forEach(el => io.observe(el));
}

/* ══════════════════════════════════════
   7. MENU FILTER
══════════════════════════════════════ */
function initMenuFilter() {
  const btns  = $$('.filter-btn');
  const items = $$('.menu-item');

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => { b.classList.remove('active'); b.setAttribute('aria-selected','false'); });
      btn.classList.add('active');
      btn.setAttribute('aria-selected','true');

      const filter = btn.dataset.filter;

      items.forEach(item => {
        const show = filter === 'all' || item.dataset.category === filter;
        if (show) {
          item.classList.remove('hidden');
          /* Re-trigger reveal */
          item.classList.remove('visible');
          setTimeout(() => item.classList.add('visible'), 20);
        } else {
          item.classList.add('hidden');
        }
      });
    });
  });
}

/* ══════════════════════════════════════
   8. EMBER PARTICLE EFFECT
══════════════════════════════════════ */
(function initEmbers() {
  if (prefersReducedMotion) return;

  const container = $('#embersCanvas');
  if (!container) return;

  const canvas = document.createElement('canvas');
  canvas.className = 'embers-canvas';
  canvas.setAttribute('aria-hidden', 'true');
  container.appendChild(canvas);
  const ctx = canvas.getContext('2d');

  let W, H, particles = [];

  function resize() {
    W = canvas.width  = container.offsetWidth;
    H = canvas.height = container.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize, { passive: true });

  class Ember {
    constructor() { this.reset(true); }

    reset(initial = false) {
      this.x  = Math.random() * W;
      this.y  = initial ? Math.random() * H : H + 10;
      this.vx = (Math.random() - 0.5) * 0.4;
      this.vy = -(Math.random() * 0.6 + 0.2);
      this.size = Math.random() * 2.2 + 0.4;
      this.life = 0;
      this.maxLife = Math.random() * 280 + 140;
      this.color = Math.random() > 0.5 ? '#C4973A' : '#E05020';
    }

    update() {
      this.x  += this.vx + Math.sin(this.life * 0.015) * 0.3;
      this.y  += this.vy;
      this.vx *= 0.999;
      this.life++;
      if (this.y < -10 || this.life > this.maxLife) this.reset();
    }

    draw() {
      const progress = this.life / this.maxLife;
      const alpha = progress < 0.15 ? progress / 0.15
                  : progress > 0.75 ? (1 - progress) / 0.25
                  : 1;

      ctx.globalAlpha = alpha * 0.55;
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size * (1 - progress * 0.3), 0, Math.PI * 2);
      ctx.fill();
    }
  }

  const COUNT = 55;
  for (let i = 0; i < COUNT; i++) particles.push(new Ember());

  let rafActive = true;
  let lastTime  = 0;

  function loop(ts) {
    if (!rafActive) return;
    if (ts - lastTime < 28) { requestAnimationFrame(loop); return; } /* ~35fps cap */
    lastTime = ts;

    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => { p.update(); p.draw(); });
    ctx.globalAlpha = 1;

    requestAnimationFrame(loop);
  }

  requestAnimationFrame(loop);

  /* Pause when hero is not visible */
  const heroSection = $('.hero');
  if (heroSection) {
    new IntersectionObserver(entries => {
      rafActive = entries[0].isIntersecting;
      if (rafActive) requestAnimationFrame(loop);
    }, { threshold: 0 }).observe(heroSection);
  }
})();

/* ══════════════════════════════════════
   9. CONTACT FORM (mock submit)
══════════════════════════════════════ */
(function initContactForm() {
  document.addEventListener('submit', e => {
    if (!e.target.matches('#contactForm')) return;
    e.preventDefault();
    const form    = e.target;
    const btn     = form.querySelector('.form-submit');
    const success = form.querySelector('.form-success');

    /* Validation */
    let valid = true;
    form.querySelectorAll('[required]').forEach(field => {
      const errEl = field.nextElementSibling;
      if (!field.value.trim()) {
        if (errEl && errEl.classList.contains('field-error'))
          errEl.textContent = 'This field is required.';
        field.setAttribute('aria-invalid', 'true');
        valid = false;
      } else {
        if (errEl && errEl.classList.contains('field-error')) errEl.textContent = '';
        field.removeAttribute('aria-invalid');
      }
    });

    if (!valid) {
      const first = form.querySelector('[aria-invalid="true"]');
      if (first) first.focus();
      return;
    }

    /* Simulate send */
    btn.classList.add('loading');
    btn.disabled = true;

    setTimeout(() => {
      btn.classList.remove('loading');
      btn.disabled = false;
      success.removeAttribute('hidden');
      form.reset();
    }, 1600);
  });
})();

/* ══════════════════════════════════════
   10. PARALLAX HERO TEXT (subtle)
══════════════════════════════════════ */
(function initParallax() {
  if (prefersReducedMotion) return;

  const heroContent = $('.hero-content');
  if (!heroContent) return;

  let ticking = false;

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const y = window.scrollY;
        heroContent.style.transform = `translateY(${y * 0.22}px)`;
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
})();

/* ══════════════════════════════════════
   11. INIT
══════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
  initReveal();
  initCounters();
  initMenuFilter();
});
