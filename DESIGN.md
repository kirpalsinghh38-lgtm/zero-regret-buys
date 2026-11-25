# DESIGN.md — Zero Regret Buys

Direction chosen by Kirpal: **A — Pharmacy shelf** (2026-11-25).
This file is the written authority for the redesign. Later phases build from it; anything that contradicts it needs Kirpal's say-so first.

## The world

The site looks like a good drugstore shelf: clean, clinical, everything labelled, the facts doing the talking. Nothing shouts. The verdict is the label, not a sales pitch. If a design choice does not make the site feel more checked and more honest, it does not go in.

## Palette

| Token | Hex | Use |
|---|---|---|
| `--paper` | `#faf9f6` | Page ground |
| `--ink` | `#1c1e1c` | Headings, primary text |
| `--ink-soft` | `#44463f` | Body text (kept from Phase 1's softened ink family; must stay ≥4.5:1 on paper) |
| `--shelf-green` | `#1e5c46` | The one accent: links, the "verified" mark, primary actions' emphasis |
| `--label-amber` | `#b45309` | Sparingly: "verified" / "checked" marks only, never a second accent competing with the green |
| `--line` | `#e3e0da` | Rules, hairlines, card borders |
| `--muted` | `#5c615c` | Secondary text on light surfaces (must stay ≥4.5:1 on paper) |
| `--card` | `#ffffff` | Card ground |
| `--dark` | `#171310` | Kept for the footer and the sticky buy bar only — the dark band is a shelf edge, not the site's ground |

The lime (`#b8e62e` / `#51820a`) is retired. The dark hero gradient is gone: flat grounds only.

## Type

- **Headings + body:** IBM Plex Sans (Google Fonts). It has real tabular numerals, so doses and numbers line up like a label.
- **Measurements only (mg, IU, ml, %):** IBM Plex Mono. Never for body copy, never as a "technical" costume.
- Sora + Inter are retired with the lime.
- Display max 6rem, body measure 65–75ch, tracking floor −0.04em.

## Layout concept

Products in ruled rows like a shelf with a label rail: photo, name, one job, one facts strip. One section per screen, equal left and right edges, generous separation between sections, tight groups inside them. One bold element per page — the hero — and everything else quiet.

## Rules (from the skills, not optional)

- No kickers or eyebrows above headings. The heading speaks.
- No gradient washes as decoration. Flat grounds only.
- No ghost cards: elevation is a border OR a shadow, never both. Card radii 12–16px.
- No single-word accent in a headline. No "→" on every button (decide once, apply everywhere). No middle-dot meta strings.
- Product photos big and real, never a thumbnail doing a hero's job. One dealt motion moment per page (hero entrance), everything rests under `prefers-reduced-motion`.
- Contrast floor holds: body text ≥4.5:1, large text ≥3:1, focus rings ≥3:1. Browser surfaces stay themed (selection, caret, scrollbar, focus rings).
- Every visual renders at 1440 / 1024 / 768 / 390. No horizontal scroll at 390px.

## What stays true, always

- All 30 products, all ASINs, the `zeroregretb04-20` tag, the all-30 cart URL, and the Associates disclosure survive every phase byte-for-byte.
- No prices are ever typed on the site. No new runtime dependency, framework, or build step. Static HTML + `styles.css` + one `site.js`. `build.py` is the only source of generated HTML.
- One phase = one commit = one push = one live verification.

## Roadmap

- Phase 3 — Home hero + quick picks (hero shows real product photos; kickers and gradient gone; quick-pick photos larger).
- Phase 4 — Shop grid + cards (ghost cards die; compare-table pill wrapping fixed).
- Phase 5 — Product pages (verdict hierarchy; dead gallery markup removed; PDP mobile bottom gap fixed).
- Phase 6 — Header, footer, navigation (kickers gone site-wide; header wordmark wrap at 390px fixed).
- Phase 7 — Motion + polish (hover layer, one hero entrance, reduced-motion audit).
- Phase 8 — Final gate (audit, link sweep, image sweep, disclosure sweep, screenshots at 1440/390).
