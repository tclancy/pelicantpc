import re
from html.parser import HTMLParser


_VOID_ELEMENTS = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }
)


class _SummaryCleaner(HTMLParser):
    """Strip headings (h1-h6) and pelican-callout blocks from summary HTML."""

    _SKIP_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.output = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if self._skip_depth > 0:
            # Void elements have no closing tag so must not increment depth
            if tag not in _VOID_ELEMENTS:
                self._skip_depth += 1
            return
        attrs_dict = dict(attrs)
        classes = set(attrs_dict.get("class", "").split())
        if tag in self._SKIP_TAGS or "pelican-callout" in classes:
            self._skip_depth = 1
            return
        attr_str = "".join(f' {k}="{v}"' for k, v in attrs)
        self.output.append(f"<{tag}{attr_str}>")

    def handle_endtag(self, tag):
        if self._skip_depth > 0:
            self._skip_depth -= 1
            return
        self.output.append(f"</{tag}>")

    def handle_data(self, data):
        if self._skip_depth == 0:
            self.output.append(data)

    def handle_entityref(self, name):
        if self._skip_depth == 0:
            self.output.append(f"&{name};")

    def handle_charref(self, name):
        if self._skip_depth == 0:
            self.output.append(f"&#{name};")


def _clean_summary(html):
    """Remove headings and callout blocks from article summary HTML."""
    cleaner = _SummaryCleaner()
    cleaner.feed(html or "")
    return "".join(cleaner.output).strip()


def _strip_leading_h1(html):
    """Remove the first <h1> from article content (it duplicates the title metadata)."""
    return re.sub(
        r"^\s*<h1[^>]*>.*?</h1>\s*",
        "",
        html or "",
        count=1,
        flags=re.DOTALL | re.IGNORECASE,
    )


AUTHOR = "Tom Clancy"
SITENAME = "Tom Clancy"
SITEURL = "http://localhost:8000"

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"
TYPOGRIFY = True

THEME = "themes/thunderbolt"

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
]

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

# Custom Jinja2 filters
JINJA_FILTERS = {
    "clean_summary": _clean_summary,
    "strip_leading_h1": _strip_leading_h1,
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
