# TPC Portfolio and Blog Relaunch

## TODO

- Remove escaped quotes, e.g., http://localhost:8000/rich-get-richer-play-one-act.html
- Absolute urls may not work until you have a domain or put a temporary shim in
- Fix domain redirection
  - [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9645/2208/how-do-i-link-my-domain-to-github-pages/)
  - [GitHub](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- Look at history of other project to see edits to posts for static assets (after everything is set)
- Some static assets don't show up due to absolute pathing
  - Wordpress links? search for http://tkc.webfactional.com/blog/wp-content/uploads/ and /wp-content/uploads/
  - find and replace on to /legacy may be a trick (http://localhost:8000/dear-josie-weasel-words.html)
  - https://tclancy.github.io/pelicantpc/nexus-and-the-library.html, https://tclancy.github.io/pelicantpc/album-cover-roobarb.html, etc
- Fix theme paging links or change theme (workflow setting update!)
- Add home and other [static pages](https://docs.getpelican.com/en/latest/content.html#pages) as needed
- Figure out URL this will live at when done
- Footer links, imagery

### Bonus Points

- oEmbed support in importers: https://micawber.readthedocs.io/en/latest/index.html
- Search? There's a js plugin, do I really care?
- Add a tag to any post starting with "Twitter Updates" or just put a "hide" status on them

## Links

- [Pelican docs](https://docs.getpelican.com/en/latest/)
- [Plugins](https://docs.getpelican.com/en/latest/plugins.html) and [repo](https://github.com/pelican-plugins)
- [UV docs](https://docs.astral.sh/uv/): Using this as a project to get used to `uv`