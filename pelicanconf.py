AUTHOR = "Tom Clancy"
SITENAME = "Tom Clancy"
SITEURL = "http://localhost:8000"

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"
TYPOGRIFY = True

THEME = "themes/combined"

# fix paging navigation per - [Override templates](https://stackoverflow.com/a/61647660/7376)
THEME_TEMPLATES_OVERRIDES = ["themes/overrides"]

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "pelican.plugins.oembed",
    "pelican.plugins.simple_footnotes",
    "pelican.plugins.deadlinks",
    "pelican.plugins.obsidian_callouts",
    "ornaments",
    "css_compiler",
]

# CSS compiler — concatenates per-theme source files into a single output.
# Edit these source files to change theme styles; combined.css is generated at build time.
# To add a third theme: add its CSS path here and write [data-theme="name"] rules in that file.
CSS_SOURCES = [
    "themes/thunderbolt/static/css/thunderbolt.css",
    "themes/old-book/static/css/old-book.css",
]
CSS_OUTPUT = "theme/css/combined.css"
CSS_MINIFY = False  # set True in publishconf.py for production

# deadlinks — check external links during build (DEADLINKS_VALIDATION enables full HTTP checks)
DEADLINKS_VALIDATION = (
    False  # set to True for periodic link audits; slow on 229 articles
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blog roll
LINKS = ()

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/tclancy"),
    ("StackOverflow", "https://stackoverflow.com/users/7376/tom"),
    ("BlueSky", "https://bsky.app/profile/tclancy.bsky.social"),
)

DEFAULT_PAGINATION = 10

# Cache busting — appended as ?v=... to static asset URLs
# Set to a git hash in publishconf.py for production; 'dev' for local builds
THEME_VERSION = "dev"

# Theme switcher is work-in-progress; hide until ready for production
SHOW_THEME_SWITCHER = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
