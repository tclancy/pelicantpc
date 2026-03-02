# Changelog

## 2026-03-02
- Add `themes/thunderbolt/` — full Pelican theme with '70s Thunderbolt & Lightfoot aesthetic
- Write `themes/thunderbolt/static/css/thunderbolt.css` (640+ lines) with CSS variables for burnt orange/denim blue/newsprint palette
- Implement 15 Jinja2 templates: base, index, article, page, tag, category, archives, author, authors, categories, tags, sidebar, pagination, 404
- Update `pelicanconf.py`: add `THEME = "themes/thunderbolt"`
- Fix class name mismatch in 404.html (BEM names → flat names matching CSS)
- Build: 228 articles processed with no errors
