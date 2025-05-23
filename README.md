# TPC Portfolio and Blog Relaunch

## TODO

- Absolute urls may not work until you have a domain or put a temporary shim in
  - cannot use relative everywhere because of tag/ summary pages
- Fix domain redirection for tomclancy.info
  - [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9645/2208/how-do-i-link-my-domain-to-github-pages/)
  - [GitHub](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- Some static assets don't show up due to absolute pathing
  - https://tclancy.github.io/pelicantpc/nexus-and-the-library.html, https://tclancy.github.io/pelicantpc/album-cover-roobarb.html, etc
- Fix theme paging links or change theme (workflow setting update!)
- Add home and other [static pages](https://docs.getpelican.com/en/latest/content.html#pages) as needed
- Footer links, imagery

### Bonus Points

- oEmbed support in importers: https://micawber.readthedocs.io/en/latest/index.html
- Search? There's a js plugin, do I really care?
- Add a tag to any post starting with "Twitter Updates" or just put a "hide" status on them

## Links

- [Pelican docs](https://docs.getpelican.com/en/latest/)
- [Plugins](https://docs.getpelican.com/en/latest/plugins.html) and [repo](https://github.com/pelican-plugins)
- [UV docs](https://docs.astral.sh/uv/): Using this as a project to get used to `uv`