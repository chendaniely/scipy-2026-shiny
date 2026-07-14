# scipy-2026-shiny
SciPy 2026 Dashboard Tutorial

## Setup

```bash
make venv
```

Creates a `.venv` with `uv`, installs dependencies from `requirements.txt`,
and installs the Playwright Chromium browser (used for testing slides/exercises).

## Building the site

```bash
make render    # render website/ to website/_site/
make preview   # live preview on port 12345
make publish   # publish to gh-pages
```

## Quarto extensions

```bash
make setup-quarto
```

Installs the Quarto extensions used by the site (shinylive, custom-callout,
revealjs chat-bubbles, pointer, include-code-files, revealjs-cascade, revealjs-a11y).
