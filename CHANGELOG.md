# Changelog

## 2026-04-04
- Add CSS variable theme switcher (issues #18/#19): toggle button in thunderbolt nav switches between Thunderbolt & Lightfoot palette (default) and Old Book palette (parchment/ink/book fonts)
- `[data-theme="old-book"]` override block in thunderbolt.css overrides all palette CSS variables + font families for key elements
- `theme-toggle.js`: localStorage persistence with try/catch safety guards, dynamic aria-label, FOUC-prevention inline script in `<head>`
- Load both font sets (Zilla Slab/Source Sans/Source Serif + Cinzel/IM Fell English/Libre Baskerville) on all pages
- Investigated CI failure in run 23984950445: transient TLS disconnect in `actions/deploy-pages@v4`; no code changes needed
- Branch: `claude/theme-switcher-18` (PR #20)

## 2026-03-11
- Add CSS styling for all 15 Obsidian callout types (issue #4): left border, tinted background, colored title, CSS-filtered icon, foldable arrows via ::after
- Color palette matches Obsidian defaults: blue (note/info/todo), sky-blue (abstract), mint-green (tip/important/question), green (success), orange (warning/caution), red (failure/danger/bug), purple (example), gray (quote)
- Branch: `claude/callout-css`

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

## 2026-03-21
- Extracted `plugins/oembed.py` to standalone `pelican-oembed` package (tclancy/pelican-oembed)
- Updated pelicanconf.py: `plugins.oembed` → `pelican.plugins.oembed`
- Updated pelicanconf.py: `obsidian_callouts` → `pelican.plugins.obsidian_callouts`
- Removed direct `micawber` and `beautifulsoup4` deps (transitive via pelican-oembed)
