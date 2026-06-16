# AGENTS.md

Project-specific instructions and pending customizations for the SciPy 2026 Shiny workshop site.

---

## Pending Customizations

All items below were intentionally stripped from the PyCon 2026 version and need to be filled in with SciPy 2026 branding/content before the workshop.

### Website Branding (`website/_quarto.yml`)

The website theme currently uses only `darkly` (Bootstrap). Two brand layers were removed and need to be restored:

1. **`website/_brand.yml`** — does not exist yet. When created, add `- brand` back to the theme list:
   ```yaml
   format:
     html:
       theme:
         - darkly
         - brand
   ```
2. **`website/styles.css`** — does not exist yet. When created, add `css: styles.css` back under `format.html`.

### Slide Theme (`website/slides/_metadata.yml`)

The slides currently use `theme: default`. Three things need to be restored once SciPy branding is decided:

1. **`website/slides/slides-theme.scss`** — deleted. When recreated, switch back to:
   ```yaml
   theme: [default, slides-theme.scss]
   ```
2. **`background-color`** — removed. Add the SciPy brand dark background color:
   ```yaml
   background-color: "<scipy-brand-color>"
   ```
3. **`title-slide-attributes`** — removed. Add a SciPy background image (place the image in `website/img/`) and restore:
   ```yaml
   title-slide-attributes:
     data-background-image: "../img/<scipy-bg-image>"
     data-background-size: cover
     data-background-opacity: "0.7"
   ```

### Mermaid Diagram Colors (`website/slides/04-reactivity.qmd`)

All Mermaid `classDef` blocks currently use neutral placeholder colors. Update to match SciPy brand palette once decided:

| Class | Current (neutral) | Replace with |
|---|---|---|
| `default` | `fill:#f0f0f0,color:#333333,stroke:#999999` | SciPy body/default node color |
| `active` | `fill:#1976D2,color:#FFFFFF,font-weight:bold` | SciPy accent/highlight color |
| `invalid` | `fill:#D32F2F,color:#FFFFFF,font-weight:bold` | can keep red or match brand |
| `cached` | `fill:#7B1FA2,color:#FFFFFF,font-weight:bold` | SciPy secondary color |

There are 8 diagram blocks in `04-reactivity.qmd`, each with the same 3–4 `classDef` lines.

### About Page Photo (`website/about.qmd`)

Currently uses `img/placeholder.png` (a flat gray square). Replace with:

```markdown
![](img/<your-headshot-filename>){width="90%"}
```

Place the actual photo in `website/img/`.

### Content Placeholders

These are marked with `<!-- TODO: -->` comments in the source files and will be surfaced by a TODO extension:

| File | What's needed |
|---|---|
| `website/index.qmd` | SciPy 2026 session date, time, and room |
| `website/_schedule.qmd` | Confirmed schedule times |
| `website/slides/01-welcome.qmd` | Venue wifi SSID and password |
| `website/slides/10-wrap_up.qmd` | SciPy session feedback survey link |
| `website/about.qmd` | Names and roles of Posit Shiny team members attending SciPy 2026 |
