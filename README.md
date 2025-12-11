# TPC Portfolio and Blog Relaunch

Static blogging using the Python `pelican` static site generator under the hood.
Markdown files under `/content/posts` and `/content/pages` are converted to HTML
by Pelican as part of a Github Action.

Local development settings are in `pelicanconf.py` while the live settings are in `publishconf.py`.

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