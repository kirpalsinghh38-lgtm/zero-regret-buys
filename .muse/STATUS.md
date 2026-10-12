# STATUS.md — Git is our communication channel (Kirpal, 2026-10-12)

## Current state (red, 2026-10-12 ~12:30 PDT)

### Logo (images/logo.jpg)
- **Status:** BROKEN LIVE — serving 105,792 bytes of base64 text instead of 79KB JPEG
- **Cause:** MCP push_files stores base64 as-is without decoding (failed twice)
- **Fix staged:** images/logo.svg (104KB, valid SVG with embedded JPEG data URI) — survives the push pipeline
- **Action needed:** Push logo.svg via connector (approval card), then verify 200 live

### Missing product images (12 files, 404 on live site)
All missing locally — not in repo, not on disk. Need source files to push.

| File | Status |
|------|--------|
| images/products/arencia-rice-cleanser.jpg | MISSING — need source |
| images/products/axis-y-dark-spot.webp | MISSING — need source |
| images/products/azelaic-acid-10.png | MISSING — need source |
| images/products/complex-15.png | MISSING — need source |
| images/products/creatine-monohydrate-2.jpg | MISSING — need source |
| images/products/dr-althea-345.jpg | MISSING — need source |
| images/products/mg-glycinate-webber-1.jpg | MISSING — need source |
| images/products/omega-3-1.jpg | MISSING — need source |
| images/products/retinal-shot-celimax.webp | MISSING — need source |
| images/products/vichy-dercos.jpg | MISSING — need source |
| images/products/vitamin-d3-k2.jpg | MISSING — need source |
| images/products/zinc-citrate.jpg | MISSING — need source |

**Blocked:** Cannot push what I don't have. Kirpal or muse-a: please provide the 12 image files (or their source URLs).

### Protocol
- Read this file before starting work. Update after finishing.
- Never claim fixed until verified live (URL returns 200).
- Red pushes, muse-a verifies.
