# Josiah05230.github.io

Public GitHub Pages portfolio for Josiah Holder (https://josiah05230.github.io).
Static site, no framework, no JS build toolchain. Keep everything committed here
technical and public-safe: no secrets, contact details beyond what the site already
shows, or private project data.

## Layout

- `template.html` - the page source (hand-edited). Contains `{{NAME}}` placeholders for
  images.
- `build.py` - reads `images/*`, base64-encodes each into a data URI, substitutes the
  placeholders into `template.html`, and writes `index.html` (the single self-contained
  file GitHub Pages serves).
- `index.html` - GENERATED output; never edit by hand, edit `template.html` and rebuild.
- `resume.html` / `resume.pdf` - printable resume (Letter, 0.55in/0.65in margins, serif).
  The PDF is the downloadable copy; regenerate it whenever `resume.html` changes.
- `images/` - source photos and logos referenced by `build.py`.

## Build / publish

- `python3 build.py` regenerates `index.html` (prints the byte size).
- Commit `template.html` and `index.html` together, then `git push` to `main`; Pages
  deploys from the branch with no CI.
- To add an image: put it in `images/`, add a `"KEY": b64("file", mime)` entry in
  `build.py`, and use `{{KEY}}` in `template.html`.

## Rules

- Never hand-edit `index.html`. Why: the next `build.py` run overwrites it.
- No em or en dashes in site copy; use plain hyphens. Why: house style of the owner.
- Commit and push after each meaningful edit. Why: uncommitted work is easy to lose.

## Gotchas

- Images are inlined, so `index.html` is large; keep source images compressed.
- A second local clone of this repo may exist; work only
  in one clone to avoid divergent histories.
