#!/usr/bin/env node
/**
 * plan-lint — deterministic checks on a website-plan.md, BEFORE anything is built.
 * The detector's philosophy applied at plan time: slop is cheapest to kill in the plan.
 *
 * Usage: node plan-lint.mjs <path/to/website-plan.md>
 * Exit 0 = clean. Exit 1 = violations (listed). Exit 2 = can't read file.
 *
 * Stdlib only, deliberately — no parser deps, so it can never silently degrade
 * the way the static-html engine did when its node_modules were missing.
 */

import fs from 'node:fs';

const BANNED_FONTS = [
  'Inter', 'Roboto', 'Arial', 'Helvetica', 'Fraunces',
  'Instrument Serif', 'Geist', 'Plus Jakarta Sans', 'Space Grotesk',
];

// Families and openers from references/section-formats.md
const FAMILIES = new Set([
  'card-grid', 'split', 'full-bleed-band', 'editorial-column', 'stat-strip',
  'steps', 'bento', 'gallery', 'quote-monolith', 'table', 'faq', 'cta-band',
  'hero',
]);
const OPENERS = new Set(['bare-h2', 'kicker+h2', 'numeral', 'side-label', 'in-media', 'none']);
const KICKER_OPENERS = new Set(['kicker+h2', 'side-label']);

const file = process.argv[2];
if (!file) { console.error('usage: plan-lint.mjs <website-plan.md>'); process.exit(2); }
let text;
try { text = fs.readFileSync(file, 'utf8'); }
catch (e) { console.error(`cannot read ${file}: ${e.message}`); process.exit(2); }

const problems = [];
const warn = (msg) => problems.push(msg);

// ── Collect the page map's section tokens ───────────────────────────────────
// Accepted line shape (anywhere in the file, one per section):
//   <anything> — format: card-grid, opener: bare-h2
// Hyphen or em dash, any case, optional backticks.
const tokenRe = /format:\s*`?([a-z0-9+-]+)`?\s*,\s*opener:\s*`?([a-z0-9+-]+)`?/gi;
const sections = [];
let m;
while ((m = tokenRe.exec(text)) !== null) {
  sections.push({ family: m[1].toLowerCase(), opener: m[2].toLowerCase() });
}

if (sections.length === 0) {
  warn('no `format:` / `opener:` tokens found — the page map must assign one per section (see section-formats.md)');
} else {
  // Unknown tokens
  for (const s of sections) {
    if (!FAMILIES.has(s.family)) warn(`unknown format family "${s.family}" — not in section-formats.md`);
    if (!OPENERS.has(s.opener)) warn(`unknown opener "${s.opener}" — not in section-formats.md`);
  }

  const n = sections.length;

  // Quota 1 — distinct families: >=4 per 8 sections, ceil(n/2) for shorter pages.
  const distinct = new Set(sections.map(s => s.family)).size;
  const needed = n >= 8 ? 4 : Math.ceil(n / 2);
  if (distinct < needed) {
    warn(`only ${distinct} distinct format families across ${n} sections — need >= ${needed}`);
  }

  // Quota 2 — no family twice in a row (serial gallery exempt).
  for (let i = 1; i < n; i++) {
    if (sections[i].family === sections[i - 1].family && sections[i].family !== 'gallery') {
      warn(`sections ${i} and ${i + 1} share the family "${sections[i].family}" back to back`);
    }
  }

  // Quota 3 — kicker budget <= ceil(sections/3).
  const kickers = sections.filter(s => KICKER_OPENERS.has(s.opener)).length;
  const budget = Math.ceil(n / 3);
  if (kickers > budget) {
    warn(`${kickers} kicker-style openers for ${n} sections — budget is ${budget} (ceil(n/3), hero included)`);
  }

  // Quota 4 — no two adjacent sections share an opener type.
  for (let i = 1; i < n; i++) {
    if (sections[i].opener === sections[i - 1].opener) {
      warn(`sections ${i} and ${i + 1} share the opener "${sections[i].opener}" — adjacent sections must differ`);
    }
  }
}

// ── Banned fonts anywhere in the plan ───────────────────────────────────────
for (const font of BANNED_FONTS) {
  const re = new RegExp(`\\b${font.replace(/ /g, '\\s+')}\\b`, 'i');
  if (re.test(text)) {
    // Allow the plan to *mention* a ban ("never Inter") — only flag lines that
    // read as a pick: the Typography/font lines.
    const lines = text.split('\n').filter(l => re.test(l));
    const picks = lines.filter(l => /typograph|font|display:|body:|pairing/i.test(l) && !/never|banned|not |avoid/i.test(l));
    if (picks.length) warn(`banned font "${font}" appears as a pick: "${picks[0].trim().slice(0, 80)}"`);
  }
}

// ── Required plan fields ────────────────────────────────────────────────────
const requiredFields = [
  [/composition device/i, 'Composition device (the named symmetry break + carrying section)'],
  [/design read|reading this as/i, 'Design Read line (taste-skill §0 — one-line brief inference)'],
  [/entrance\s*=|entrance family/i, 'signature-motion tokens (entrance/hover/set-piece/tempo)'],
  [/register/i, 'imagery register (proud-contractor / editorial)'],
];
for (const [re, label] of requiredFields) {
  if (!re.test(text)) warn(`missing required field: ${label}`);
}

// VIDEO slot, if marked, must declare its register.
if (/\bVIDEO\b/.test(text) && !/filmed-action|designed-loop/i.test(text)) {
  warn('a VIDEO slot is marked but no register (filmed-action / designed-loop) is declared');
}

// ── Report ──────────────────────────────────────────────────────────────────
if (problems.length === 0) {
  console.log(`plan-lint: clean (${sections.length} sections, ${new Set(sections.map(s => s.family)).size} families)`);
  process.exit(0);
}
console.log(`plan-lint: ${problems.length} problem${problems.length === 1 ? '' : 's'} in ${file}\n`);
for (const p of problems) console.log(`  ✖ ${p}`);
console.log('\nFix the plan and re-run. Quotas and vocabulary: references/section-formats.md');
process.exit(1);
