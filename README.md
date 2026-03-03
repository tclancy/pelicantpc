# TPC Portfolio and Blog Relaunch

Static blogging using the Python `pelican` static site generator under the hood.
Markdown files under `/content/posts` and `/content/pages` are converted to HTML
by Pelican as part of a Github Action.

Local development settings are in `pelicanconf.py` while the live settings are in `publishconf.py`.

`publishconf.py` imports everything from `pelicanconf.py` and overrides the production-specific values
(live `SITEURL`, feeds enabled, `DELETE_OUTPUT_DIRECTORY = True`). You should never need to edit
`publishconf.py` for local dev.

Deployment consists of committing changes to main and pushing up to GitHub.

## Running Locally

### Quick start (recommended)

```bash
cd ~/Documents/work/pelicantpc

# Build once and serve on http://localhost:8000
uv run pelican content -s pelicanconf.py
python -m http.server 8000 --directory output
```

### Auto-rebuild on file changes

```bash
# In one terminal: watch and rebuild on every content/template/CSS change
uv run pelican --autoreload -s pelicanconf.py

# In another terminal: serve the output
python -m http.server 8000 --directory output
```

Or with the Makefile (if `pelican` is on your PATH):

```bash
make devserver  # starts both watcher + HTTP server together
```

### Config files explained

| File | Purpose |
|------|---------|
| `pelicanconf.py` | Local dev — `SITEURL = "http://localhost:8000"`, feeds off |
| `publishconf.py` | Production — imports pelicanconf, sets `SITEURL = "https://tomclancy.info"`, feeds on |

The GitHub Action runs `pelican content -s publishconf.py` on push to `main`.

## TODO

- [ ] Markdown linter for consistency between writing environments?

### Bonus Points

- oEmbed support in importers: https://micawber.readthedocs.io/en/latest/index.html
  - Not sure if I need it; if so, here's an example content/posts/2013-06-12-parochialism.md
    - problem is there are lots of embedded youtube and similar in things, so it would need some testing
  - Swap ://twitter.com to ://x.com?
  - Add requirement to hook
- Add a tag to any post starting with "Twitter Updates" or just put a "hide" status on them
- Music blogging for favorites -- create a landing page

## Portfolio

- Do it in sync with A-Team portfolio rebuild
- Automatically add media from Django if possible, remove things like `thumb:1`

## Improve Blog Posts

- Media consumed posts: podcasts, books, etc

## Links

- [Pelican docs](https://docs.getpelican.com/en/latest/)
- [Plugins](https://docs.getpelican.com/en/latest/plugins.html) and [repo](https://github.com/pelican-plugins)
- [UV docs](https://docs.astral.sh/uv/): Using this as a project to get used to `uv`