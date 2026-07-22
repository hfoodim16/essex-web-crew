# Backgrounds — depth & texture cookbook

Purpose: flat single-color backgrounds are the #1 tell of a template. Depth, texture, and atmosphere are what make a site feel designed. Copy-paste-ready recipes below; adapt colors to the chosen palette (use CSS variables).

## Layered gradient mesh (the workhorse)
Multiple radial gradients at different corners = organic, expensive-looking depth.
```css
.mesh {
  background-color: #0b0f1a;
  background-image:
    radial-gradient(at 20% 15%, hsla(265,80%,55%,0.35) 0px, transparent 55%),
    radial-gradient(at 80% 10%, hsla(190,90%,50%,0.25) 0px, transparent 50%),
    radial-gradient(at 75% 85%, hsla(330,85%,60%,0.30) 0px, transparent 55%);
}
```
Light-mode version: raise base to a near-white, drop alphas to ~0.12–0.18.

## Noise / grain overlay (removes the "flat digital" feel)
SVG turbulence as a tiling overlay. Sits above the background, below content.
```css
.grain::before {
  content: ""; position: absolute; inset: 0; pointer-events: none;
  opacity: 0.05; mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

## Animated gradient (subtle, always tasteful)
```css
.animated-bg {
  background: linear-gradient(120deg,#1a0b2e,#2d1b4e,#0b2e2a,#1a0b2e);
  background-size: 300% 300%;
  animation: drift 18s ease infinite;
}
@keyframes drift { 0%,100%{background-position:0% 50%} 50%{background-position:100% 50%} }
@media (prefers-reduced-motion: reduce){ .animated-bg{animation:none} }
```

## Geometric SVG patterns (dot grid / lines)
Dot grid via pure CSS — great for technical/SaaS looks:
```css
.dotgrid {
  background-image: radial-gradient(circle, rgba(255,255,255,.12) 1px, transparent 1px);
  background-size: 22px 22px;
}
```
Fading grid: wrap the above and add a `mask-image: radial-gradient(ellipse at center, black, transparent 70%)`.

## Glow / orb ambience
Soft blurred color blobs behind content for a premium dark look:
```css
.orb { position:absolute; border-radius:50%; filter: blur(90px); opacity:.55; }
/* place two or three, e.g. */
.orb.a{ width:420px;height:420px; background:#7c3aed; top:-80px; left:-60px; }
.orb.b{ width:360px;height:360px; background:#06b6d4; bottom:-100px; right:-40px; }
```

## Section transitions (break the boring stacked-rectangle rhythm)
- **Angled dividers:** `clip-path: polygon(0 0,100% 0,100% 92%,0 100%)` on a section.
- **Curved:** an inline SVG wave between sections.
- **Marquee strip:** an infinite-scroll text/logo band as a divider (pairs with kinetic motion).
- **Overlap:** pull the next section up with negative margin so cards straddle the seam.

## Custom cursor (distinctive, use when the direction is bold)
```css
* { cursor: none; }
.cursor { position:fixed; width:18px;height:18px;border:2px solid #fff;border-radius:50%;
  transform:translate(-50%,-50%); pointer-events:none; mix-blend-mode:difference; z-index:9999;
  transition: transform .12s ease; }
```
Track with a small pointermove listener; scale up on hoverable elements. Always keep a real fallback for touch/reduced-motion.

## When to reach for canvas / WebGL / three.js
Only when the direction genuinely calls for it (immersive hero, 3D product, particle field) and the payoff justifies it. **Cost warning:** heavier bundle, performance/accessibility burden, more build time. Prefer CSS/SVG for 90% of cases; use three.js for the signature hero moment, lazy-loaded, with a static fallback and `prefers-reduced-motion` respected.

## Animated atmosphere
For *moving* light and air — drifting fog, parallax clouds, god rays / beams, aurora ribbons, shimmer sweeps, dust motes — see `atmosphere.md`. This file is static/ambient depth; that one is the weather-and-light layer, with performance guardrails.

## Rules
- Every background must layer with content contrast intact — check text still hits WCAG AA over it.
- Combine recipes (mesh + grain + one orb) rather than relying on a single flat treatment.
- Match the background system to the direction's axis-4 choice; don't default every site to the mesh.
