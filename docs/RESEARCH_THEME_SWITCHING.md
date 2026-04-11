# Pelican Theme Switching Research

**Research Date:** 2026-04-04  
**Status:** Complete

---

## Executive Summary

- **No existing Pelican plugin** for client-side theme switching (toggling between themes in the browser)
- **One theme found with prefers-color-scheme support** (simplenice) but no manual toggle
- **CSS custom properties approach is proven & pragmatic** for Pelican—multiple static site generators use this pattern successfully
- **Recommended:** CSS variables + localStorage + JS toggle gives best UX with minimal complexity
- **Implementation estimate:** 2-4 hours for your two-theme setup (thunderbolt + old-book)

---

## Part 1: Existing Solutions (What's Available)

### 1.1 Official Pelican Plugin Ecosystem

**Status:** No theme-switching plugin exists  
**Source:** [GitHub - pelican-plugins organization](https://github.com/pelican-plugins)

The official `pelican-plugins` organization maintains 48 community plugins. Comprehensive search of repository names, descriptions, and documentation reveals:

**Plugins that exist:**
- sitemap, search, image-process, similar-posts, series, webring, photos, SEO, simple-footnotes, i18n-subsites, fediverse, markdown-include, tailwindcss, webassets, injector, and 33 others

**Plugins that do NOT exist:**
- No theme-switcher, theme-toggle, or dark-mode plugin
- No color-scheme or appearance-switching plugin
- Most plugins focus on content processing, SEO, and site functionality rather than visual presentation

**Related Plugin:** `pelican-theme-config` (allows themes to adjust Pelican's configuration via themeconf.py, but this is build-time config, not runtime switching)

### 1.2 Pelican Theme Analysis

**Search Results:** Examined [official Pelican themes repository](https://github.com/getpelican/pelican-themes) and PyPI packages

**m.css Theme:**
- Supports two **static** themes (light/dark) selectable at build time via `M_CSS_FILES` config
- No runtime switching mechanism
- User must rebuild site to change theme
- Source: [m.css Pelican theme](https://mcss.mosra.cz/themes/pelican/)

**simplenice Theme:**
- Implements **prefers-color-scheme** (automatic OS detection)
- Includes manual or automatic selection "via prefers-color-scheme and prefers-contrast modes"
- Supports 3 schemes: default/light, dark, high-contrast/greyscale
- Does NOT expose a user-facing toggle button in README
- Source: [smeso/simplenice on GitHub](https://github.com/smeso/simplenice)

**Other Themes:**
- plumage, seafoam, pelican-theme-smallweb, and others focus on static styling
- None explicitly advertise runtime theme switching capability

**PyPI Packages Checked:**
- No "pelican-theme-switcher" or "pelican-dark-mode" package exists on PyPI
- Packages like `pelican-custom-css` (for per-article CSS) and `pelican-webassets` exist but serve different purposes

### 1.3 GitHub Search for Community Implementations

**Search:** `"pelican" + "theme switcher"/"theme toggle"` across GitHub  
**Result:** No dedicated third-party Pelican theme switcher repository found

Only general Pelican theme repository discussions appear, mostly about build-time theme selection, not runtime toggling.

---

## Part 2: Feasible Approaches for Runtime Theme Switching

### 2.1 CSS Custom Properties (Variables) + JavaScript

**Complexity:** LOW  
**Browser Support:** Excellent (CSS variables: 95%+ modern browsers)  
**Persistence:** localStorage  
**FOUC (Flash of Unstyled Content) Risk:** Low if initialization script placed in `<head>`

**How it works:**

1. **Define CSS variables for each theme** in your stylesheet:
   ```css
   :root {
     --text-color: #222126;
     --bg-color: #ffffff;
     --primary: #665df5;
   }
   
   [data-theme="dark"] {
     --text-color: #f5f5f5;
     --bg-color: #1a1a1a;
     --primary: #382cf1;
   }
   ```

2. **Use variables throughout CSS:**
   ```css
   body {
     color: var(--text-color);
     background-color: var(--bg-color);
   }
   ```

3. **Add toggle button in template** (e.g., in header):
   ```html
   <button id="theme-toggle">Toggle Theme</button>
   ```

4. **JavaScript for switching:**
   ```javascript
   const themeToggle = document.getElementById('theme-toggle');
   const currentTheme = localStorage.getItem('theme') || 'light';
   document.documentElement.setAttribute('data-theme', currentTheme);
   
   themeToggle.addEventListener('click', () => {
     const theme = document.documentElement.getAttribute('data-theme');
     const newTheme = theme === 'light' ? 'dark' : 'light';
     document.documentElement.setAttribute('data-theme', newTheme);
     localStorage.setItem('theme', newTheme);
   });
   ```

**Advantages:**
- Single HTTP request (CSS + JS bundled)
- Instant toggle (no page reload)
- Works entirely client-side; no server changes needed
- Survived as standard approach across 11ty, Jekyll, Hugo, and other SSGs
- Easy to extend with prefers-color-scheme detection

**Disadvantages:**
- Requires refactoring both themes' CSS to use CSS variables
- Not all CSS properties can use variables (e.g., `@media` queries need separate definitions)

**Proven In:** 11ty, Jekyll, Hugo, and documented in [FreeCodeCamp SSG theming guide](https://www.freecodecamp.org/news/design-a-themeable-static-website/)

### 2.2 Multiple Stylesheets + JS Link Switcher

**Complexity:** MEDIUM  
**Browser Support:** Universal (works everywhere)  
**Persistence:** localStorage  
**FOUC Risk:** Medium (second stylesheet may load after page renders)

**How it works:**

1. Keep themes completely separate as separate CSS files:
   ```html
   <link id="theme-link" rel="stylesheet" href="/theme-light.css">
   ```

2. JavaScript swaps the `href`:
   ```javascript
   const themeLink = document.getElementById('theme-link');
   const currentTheme = localStorage.getItem('theme') || 'light';
   themeLink.href = `/theme-${currentTheme}.css`;
   ```

3. On toggle, change the href and save preference

**Advantages:**
- No CSS refactoring needed; works with existing theme files
- Clear separation between themes
- Works even if CSS variables aren't supported

**Disadvantages:**
- Extra HTTP request per theme load
- Potential flash of unstyled content while CSS loads
- Theme file duplication makes maintenance harder
- Slower toggle experience due to stylesheet loading

### 2.3 Prefers-Color-Scheme Media Query (Browser-Driven)

**Complexity:** MINIMAL  
**Browser Support:** 90%+ modern browsers  
**Persistence:** Built into OS/browser (no coding needed)  
**FOUC Risk:** None

**How it works:**

```css
@media (prefers-color-scheme: light) {
  body { color: #222; background: #fff; }
}

@media (prefers-color-scheme: dark) {
  body { color: #f5f5f5; background: #1a1a1a; }
}
```

Browser automatically applies theme based on OS setting (System Preferences → Dark Mode, etc.)

**Advantages:**
- Zero JavaScript required
- Respects user's OS preference
- Very low implementation overhead
- Already implemented in simplenice theme

**Disadvantages:**
- **No user toggle in browser** (respects OS setting only)
- Not suitable if you want to offer manual override without changing OS settings
- Less control over exact theme appearance

**Best For:** Accessibility-first sites where user OS preference is sufficient

### 2.4 Jinja2 Template-Based Theme Switching (Server-Side)

**Complexity:** LOW (at build time)  
**Implementation Time:** During `pelican build`, not runtime  
**Persistence:** Not applicable (user doesn't choose at runtime)

**How it works:**

Use Pelican's `THEME_STATIC_PATHS` or theme inheritance to generate multiple HTML variants with different CSS, one per theme. User must configure their site at build time which theme to use.

**Disadvantages:**
- Not client-side switching
- No toggle button for end users
- Requires separate site builds or content duplication
- Not suitable for "switch themes in the browser" requirement

---

## Part 3: Your Specific Situation (thunderbolt + old-book)

### Current Setup
- Two existing themes: **thunderbolt** and **old-book**
- Blog already built with Pelican
- Want users to toggle between themes in-browser

### Analysis of Your Themes

**To determine best approach, you need to check:**

1. How different are the two theme CSS files?
   - If they use completely different color schemes and typography → CSS variables refactor needed
   - If they share similar structure but different colors → CSS variables ideal

2. Do the themes already share any CSS structure?
   - If yes, CSS variables approach is cleanest
   - If no, stylesheet switching might be faster initially

3. What's your maintenance preference?
   - Prefer keeping theme CSS completely separate? → Stylesheet switching
   - Prefer unified CSS with variable overrides? → CSS custom properties

### Recommended Approach: CSS Custom Properties + localStorage

**Why this is best for your case:**

1. **Minimal code changes** — Only refactor CSS to use variables, don't modify templates
2. **Fast switching** — No HTTP requests, no FOUC
3. **Proven pattern** — Used by 11ty, Jekyll, Hugo communities
4. **Extensible** — Can add more themes later by adding more variable sets
5. **Accessible** — Can layer prefers-color-scheme detection on top

**Implementation for thunderbolt + old-book:**

```
Current structure:
  thunderbolt/
    static/
      css/
        theme.css
  old-book/
    static/
      css/
        theme.css

New structure:
  your-theme/ (unified)
    static/
      css/
        base.css (structure, layouts, typography)
        theme.css (all color + styling via CSS variables)
        toggle.js (theme switching logic)
    templates/
      base.html (add toggle button + initialize script)
```

**Migration path:**

1. Analyze thunderbolt's CSS → extract colors to variables
2. Analyze old-book's CSS → extract colors to variables
3. Create unified `theme.css` with `:root` defaults + `[data-theme="old-book"]` overrides
4. Add 5-line toggle button to `base.html`
5. Add 10-line initialization script to `<head>` to prevent FOUC
6. Test in browser with toggle

**Estimated effort:** 2–4 hours depending on CSS complexity

---

## Part 4: Decision Matrix

| Approach | Complexity | Speed | Maintenance | Best For |
|----------|-----------|-------|-------------|----------|
| **CSS Variables + JS** | Low | Instant | Medium (unified CSS) | Your setup ✓ |
| **Stylesheet Switching** | Medium | Slower (FOUC) | Easy (separate files) | If CSS very different |
| **Prefers-Color-Scheme** | Minimal | Automatic | Easy | Accessibility-first |
| **Multiple Builds** | Medium | N/A | Hard | Advanced multi-theme sites |

---

## Recommended Next Steps

1. **Audit your theme CSS:**
   - Clone both thunderbolt and old-book
   - Compare their CSS files side-by-side
   - Identify: shared structure? Or completely different?

2. **Choose approach based on audit:**
   - If 60%+ CSS is reusable → CSS variables
   - If CSS completely separate → Stylesheet switching (faster initial implementation)
   - If accessibility is priority → Add prefers-color-scheme on top of your choice

3. **Prototype the toggle:**
   - Start with a test in `base.html`
   - Verify localStorage persistence works
   - Test FOUC prevention (script in `<head>`)

4. **Integrate with Pelican build:**
   - Decide: create new unified theme or modify existing?
   - Update `pelicanconf.py` to point to new theme
   - Test build output

---

## Sources

- [GitHub - pelican-plugins organization](https://github.com/pelican-plugins) — Official plugin collection
- [pelican-plugins/theme-config](https://github.com/pelican-plugins/theme-config) — Build-time theme configuration plugin
- [m.css Pelican theme](https://mcss.mosra.cz/themes/pelican/) — Static theme selection at build time
- [smeso/simplenice Pelican theme](https://github.com/smeso/simplenice) — prefers-color-scheme implementation
- [FreeCodeCamp: Design a Themeable Static Website](https://www.freecodecamp.org/news/design-a-themeable-static-website/) — CSS variables + localStorage pattern for 11ty
- [GitHub - getpelican/pelican-themes](https://github.com/getpelican/pelican-themes) — Official theme repository
- [MDN: prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme) — Browser color scheme detection
- [DEV Community: Dark Mode Toggle and prefers-color-scheme](https://dev.to/abbeyperini/dark-mode-toggle-and-prefers-color-scheme-4f3m) — Implementation patterns
- [Smashing Magazine: Setting Persisting Color Scheme Preferences](https://www.smashingmagazine.com/2024/03/setting-persisting-color-scheme-preferences-css-javascript/) — Current best practices (2024)
