# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import subprocess
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F403

# Cache busting: use the current git commit hash so browsers reload static
# assets (CSS, JS) after every deploy. Falls back to a timestamp if git
# is unavailable.
try:
    THEME_VERSION = (
        subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
        .decode()
        .strip()
    )
except Exception:
    import time

    THEME_VERSION = str(int(time.time()))

# If your site is available via HTTPS, make sure SITEURL begins with https://
# SITEURL = "https://tpcii.githubpages.io"
SITEURL = "https://tomclancy.info"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "pelican.plugins.oembed",
    "pelican.plugins.simple_footnotes",
    "pelican.plugins.deadlinks",
    "pelican.plugins.obsidian_callouts",
    "ornaments",
]

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
