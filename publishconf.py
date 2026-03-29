# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# SITEURL = "https://tpcii.githubpages.io"
SITEURL = "https://tomclancy.info"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

# Plugins
PLUGINS = [
    'pelican.plugins.oembed',
    'pelican.plugins.simple_footnotes',
    'pelican.plugins.deadlinks',
    'pelican.plugins.obsidian_callouts',
]

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
