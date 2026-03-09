# Changelog

## 2026-03-09
- Install `pelican-simple-footnotes` plugin (PyPI); activate in PLUGINS (issue #1)
- Install `pelican-deadlinks` plugin from GitHub (no PyPI release); activate in PLUGINS with `DEADLINKS_VALIDATION = False` default (issue #2)
- Add Plugins section to README documenting all 3 active plugins with install instructions and link-audit workflow
- Post clarifying questions to GitHub issue #3 (callouts plugin) before building
- Branch: `claude/phase4-plugins` (2 commits)

## 2026-03-03
- Swap header title text → SVG metallic logotype (Interstate '76 inspired lettering with gradient + distress filter)
- Add Thunderbolt & Lightfoot movie photo as washed-out header background (82% blue overlay, non-distracting)
- Replace Playfair Display with Zilla Slab across all headings, nav, sidebars, page titles
- Add burn/char CSS effect to article titles and in-body headings (layered dark warm text-shadow)
- Portfolio category page: 3-column card grid (responsive: 2-col tablet, 1-col mobile)
- README: add "Running Locally" section with pelican commands and conf file explanation table
- Fix `pelicanconf.py` SITEURL → localhost (was accidentally set to production URL)
- Add thunderbolt movie stills to `assets/thunderbolt/` and `themes/thunderbolt/static/img/`
- Build: 228 articles, 0 errors

## 2026-03-02
- Add `themes/thunderbolt/` — full Pelican theme with '70s Thunderbolt & Lightfoot aesthetic
- Write `themes/thunderbolt/static/css/thunderbolt.css` (640+ lines) with CSS variables for burnt orange/denim blue/newsprint palette
- Implement 15 Jinja2 templates: base, index, article, page, tag, category, archives, author, authors, categories, tags, sidebar, pagination, 404
- Update `pelicanconf.py`: add `THEME = "themes/thunderbolt"`
- Fix class name mismatch in 404.html (BEM names → flat names matching CSS)
- Build: 228 articles processed with no errors
