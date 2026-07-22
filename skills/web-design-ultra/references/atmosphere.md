# Atmosphere — animated fog, clouds, light & shimmer

Purpose: atmospheric motion is what separates gallery-grade heroes from static pages — light that moves, air that drifts. These are *felt before they're seen*: if a visitor's first thought is "there's an animation," it's too strong. Adapt every color to the direction's palette via CSS variables.

**Budget: 1–2 atmospheric effects per page, max.** Atmosphere, not weather channel.

## Global rules (non-negotiable)

- Animate **only `transform` and `opacity`**. The two exceptions (hue-rotate aurora, feTurbulence haze) are flagged expensive below — contained elements only.
- **`mix-blend-mode` + `filter: blur()` on an animated layer is the #1 perf trap.** A blend-mode layer re-composites against everything behind it *every frame*; stack 3–4 big blurred blended layers over a photo and you saturate the compositor (rAF stops firing, scroll janks — verified failure). Rules that keep it cheap:
  - **Promote every animated atmosphere layer** with `will-change: transform` or `will-change: opacity` so its blur is rasterized **once** and only the cheap property varies per frame.
  - **≤ 2 `mix-blend-mode` layers animating at once.** Beyond that, drop the blend mode and use a translucent light-colored gradient over the dark background (source-over) — over dark imagery it reads almost identical to `screen` for a fraction of the cost.
  - Keep animated blur radii **modest** (≤ ~18px). Huge blurs over large areas are fill-rate murder.
- **Every effect dies under `@media (prefers-reduced-motion: reduce)`** — kill the animation, keep a pleasant static frame.
- Any rAF/canvas loop **pauses when off-screen** (IntersectionObserver) and caps its work. Never per-frame `shadowBlur` on particles — it pegs the renderer (learned the hard way).
- Effects layer **under content and under scrims** — re-check text contrast (WCAG AA) after adding any light effect.
- Mobile: halve layer counts and blur radii; big blurs are GPU-expensive at any size but especially on battery.
- **Verify honestly:** if a screenshot/scroll tool times out with "unresponsive renderer," or `requestAnimationFrame` stops firing while your CSS animations run, the atmosphere is too heavy — lighten it (promote layers, drop blend modes, cut a layer) until it recovers. (Note: some headless preview panes starve rAF regardless of the page — confirm by pausing all animations; if rAF still doesn't fire, it's the environment, and you fall back to reasoning about cost + a static screenshot.)

## Drifting fog / mist

Layered soft bands drifting at different speeds. Hugs the bottom of a hero or seeps across a dark section.
```css
.fog{position:absolute;left:-20%;right:-20%;bottom:-8%;height:45%;pointer-events:none;z-index:1;
  will-change:transform;   /* promote: blur rasterized once, only transform varies */
  background:radial-gradient(60% 90% at 30% 80%, rgba(235,240,238,.14), transparent 70%),
             radial-gradient(50% 80% at 75% 90%, rgba(235,240,238,.10), transparent 70%);
  filter:blur(16px); mix-blend-mode:screen; animation:fog-a 26s ease-in-out infinite alternate}
.fog.b{bottom:-14%;height:36%;filter:blur(18px);opacity:.7;animation:fog-b 38s ease-in-out infinite alternate}
/* over dark backgrounds, dropping mix-blend-mode (source-over) looks nearly identical and costs far less */
@keyframes fog-a{from{transform:translateX(-4%)}to{transform:translateX(5%)}}
@keyframes fog-b{from{transform:translateX(3%)}to{transform:translateX(-6%)}}
```
Two layers at different speeds/blurs = parallax depth. Tint the rgba toward the palette (cool blue-grey for night, warm cream for golden hour).

## Clouds (parallax drift)

Blurred cloud puffs crossing very slowly. For light-sky heroes or dreamy sections.
```css
.cloud{position:absolute;pointer-events:none;filter:blur(22px);opacity:.5;
  background:radial-gradient(closest-side, rgba(255,255,255,.85), transparent);
  border-radius:50%;mix-blend-mode:screen}
.cloud.c1{width:420px;height:120px;top:12%;animation:cloud-drift 70s linear infinite}
.cloud.c2{width:300px;height:90px;top:26%;opacity:.35;animation:cloud-drift 110s linear infinite;animation-delay:-40s}
@keyframes cloud-drift{from{transform:translateX(-30vw)}to{transform:translateX(130vw)}}
```
Durations 60s+; anything faster reads cartoonish. Vary `animation-delay` negatively so clouds start mid-sky.

## God rays / light beams ("shiny beaming")

Angled shafts of light fanning from a bright source (sun in a photo, a glow orb, top corner). The premium move over golden-hour or dark imagery.
```css
.rays{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:1}
.ray{position:absolute;top:-20%;height:150%;width:110px;will-change:opacity;   /* promote */
  background:linear-gradient(rgba(255,236,200,.26), rgba(255,236,200,0) 78%);
  filter:blur(12px);transform-origin:top center;animation:ray-breathe 9s ease-in-out infinite}
/* light color over dark imagery reads as beams without mix-blend-mode; add screen only if you need more glow AND stay within the 2-blend-layer budget */
.ray:nth-child(1){left:44%;transform:rotate(16deg)}
.ray:nth-child(2){left:52%;width:60px;transform:rotate(23deg);animation-delay:-3s}
.ray:nth-child(3){left:38%;width:80px;transform:rotate(9deg);animation-delay:-6s;opacity:.7}
@keyframes ray-breathe{0%,100%{opacity:.45}50%{opacity:.9}}
```
Anchor rays to the actual light source in the image (match `left` and rotation to the sun's position). Warm tint for sun, cool for moon/neon. 2–4 rays; breathe opacity, don't sweep position — real light doesn't wander. Conic variant for a visible sunburst: `background:conic-gradient(from 200deg at 50% 0%, transparent 0 8deg, rgba(255,236,200,.12) 10deg 14deg, transparent 16deg ...)`.

## Shimmer / glint sweep

A highlight band sweeping across a headline word, button, or card edge every few seconds. Reads as "polished object catching light."
```css
/* headline word glint */
.glint{background:linear-gradient(110deg, currentColor 42%, #fff 50%, currentColor 58%);
  background-size:280% 100%;-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;animation:glint-sweep 7s ease-in-out infinite}
@keyframes glint-sweep{0%,72%{background-position:120% 0}92%,100%{background-position:-60% 0}}
```
The long idle (0–72%) is the point — a glint every 5–8s, not a strobing loop. Card variant: absolutely-positioned skewed white gradient pseudo-element translating across on the same sparse timing.

## Aurora ribbons

Large blurred color ribbons slowly weaving — the dark-mode showpiece. **Expensive exception:** uses `filter: hue-rotate` — contain it to one positioned wrapper, never body-wide.
```css
.aurora{position:absolute;inset:-10%;pointer-events:none;opacity:.5;filter:blur(70px)}
.aurora i{position:absolute;border-radius:50%;mix-blend-mode:screen}
.aurora i:nth-child(1){width:55vw;height:32vh;left:5%;top:12%;background:#3aaf7c;animation:aur-a 21s ease-in-out infinite alternate}
.aurora i:nth-child(2){width:45vw;height:28vh;right:2%;top:28%;background:#4f7dd9;animation:aur-b 27s ease-in-out infinite alternate}
@keyframes aur-a{from{transform:translate(-4%,2%) rotate(-6deg)}to{transform:translate(6%,-4%) rotate(5deg)}}
@keyframes aur-b{from{transform:translate(3%,-2%) rotate(4deg)}to{transform:translate(-5%,3%) rotate(-7deg)}}
```

## Dust motes / fireflies (canvas)

Tiny floating particles for depth. The safe pattern (no shadowBlur, capped, pausable):
```js
(function(){
  if(matchMedia('(prefers-reduced-motion:reduce)').matches) return;
  const c=document.getElementById('motes'); if(!c) return;
  const x=c.getContext('2d'); let w,h,ps=[],run=true,raf=0;
  const size=()=>{w=c.width=c.parentElement.offsetWidth;h=c.height=c.parentElement.offsetHeight};
  const mk=()=>({x:Math.random()*w,y:Math.random()*h,r:Math.random()*1.6+.4,
    vx:(Math.random()-.5)*.16,vy:-(Math.random()*.22+.05),a:Math.random()*.4+.15,p:Math.random()*7});
  size(); for(let i=0,n=Math.min(40,w/36|0);i<n;i++) ps.push(mk());
  (function loop(t){ if(!run){raf=0;return}
    x.clearRect(0,0,w,h);
    for(const p of ps){ p.x+=p.vx; p.y+=p.vy;
      const tw=.6+.4*Math.sin(t/900+p.p);            // twinkle via alpha, not blur
      x.globalAlpha=p.a*tw; x.fillStyle='#ffe9c4';
      x.beginPath(); x.arc(p.x,p.y,p.r,0,7); x.fill();
      if(p.y<-4||p.x<-4||p.x>w+4) Object.assign(p,mk(),{y:h+4}); }
    x.globalAlpha=1; raf=requestAnimationFrame(loop); })(0);
  addEventListener('resize',size);
  new IntersectionObserver(e=>{run=e[0].isIntersecting; if(run&&!raf)requestAnimationFrame(loop=>{})||0}).observe(c.parentElement);
})();
```
(When pausing/resuming, re-enter the named loop — keep a reference as in the recipe's full form.) Warm motes for firelight, cool for night, white for dust in a sunbeam — pair with god rays.

## Heat haze / water ripple (use sparingly)

Animated `feTurbulence` + `feDisplacementMap`. **The most expensive recipe here — small contained elements only (a logo, one image card), never full-viewport.** Static image fallback for mobile.
```html
<svg width="0" height="0"><filter id="haze">
  <feTurbulence type="fractalNoise" baseFrequency="0.012 0.05" numOctaves="2" seed="3">
    <animate attributeName="baseFrequency" dur="14s" values="0.012 0.05;0.016 0.06;0.012 0.05" repeatCount="indefinite"/>
  </feTurbulence>
  <feDisplacementMap in="SourceGraphic" scale="9"/>
</filter></svg>
<style>.haze-target{filter:url(#haze)}
@media(prefers-reduced-motion:reduce){.haze-target{filter:none}}</style>
```

## Pairing guide

| Direction mood | Reach for |
|---|---|
| Golden-hour / natural / trades | god rays + low fog |
| Dark luxury / night | aurora or fireflies + subtle glint |
| Ethereal / dreamy / wellness | clouds + fog |
| Premium product / editorial | glint sweep only (restraint IS the flex) |
| Fire / energy | motes (warm) + glow orbs from backgrounds.md |

## Checklist before shipping an effect
- [ ] Under scrim, text still WCAG AA
- [ ] `prefers-reduced-motion` guard covers it (CSS keyframes AND any canvas)
- [ ] Canvas loops pause off-screen, counts capped, no per-frame shadowBlur
- [ ] Page still scrolls smoothly (if a screenshot/scroll tool times out, the effect is too heavy — fix it)
- [ ] Effect count on page ≤ 2
