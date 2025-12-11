AUTHOR = "Tom Clancy"
SITENAME = "Tom Clancy"
SITEURL = "https://tomclancy.info"

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"
TYPOGRIFY = True

# fix paging navigation per - [Override templates](https://stackoverflow.com/a/61647660/7376)
THEME_TEMPLATES_OVERRIDES = ["themes/overrides"]

# Plugins
PLUGINS = ['plugins.oembed']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blog roll
LINKS = (
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/tclancy"),
    ("StackOverflow", "https://stackoverflow.com/users/7376/tom"),
    ("BlueSky", "https://bsky.app/profile/tclancy.bsky.social")
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
