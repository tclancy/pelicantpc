"""Tests for IndieWeb microformat markup (#30).

Verifies rel-me on social links, h-entry on articles, h-card in footer.
Tests render the Jinja2 templates directly with mock context rather than
running a full Pelican build.
"""

from __future__ import annotations

from pathlib import Path

import jinja2
import pytest

THEMES_DIR = Path(__file__).parent.parent / "themes"
OVERRIDES_DIR = THEMES_DIR / "overrides"

MOCK_CONTEXT = {
    "DEFAULT_LANG": "en",
    "SITENAME": "Tom Clancy",
    "SITEURL": "https://tomclancy.info",
    "AUTHOR": "Tom Clancy",
    "SOCIAL": [
        ("GitHub", "https://github.com/tclancy"),
        ("StackOverflow", "https://stackoverflow.com/users/7376/tom"),
        ("BlueSky", "https://bsky.app/profile/tclancy.bsky.social"),
    ],
    "MENUITEMS": [],
    "pages": [],
    "categories": [],
    "FEED_ALL_ATOM": None,
    "FEED_DOMAIN": "",
    "THEME_VERSION": "test",
}


def _make_env(theme: str) -> jinja2.Environment:
    """Create a Jinja2 environment for the given theme with overrides."""
    theme_dir = THEMES_DIR / theme / "templates"
    loader = jinja2.FileSystemLoader([str(OVERRIDES_DIR), str(theme_dir)])
    env = jinja2.Environment(loader=loader, autoescape=False)
    env.filters["clean_summary"] = lambda x: x
    env.filters["strip_leading_h1"] = lambda x: x
    env.filters["truncate"] = lambda x, *a, **k: x[:400]
    return env


@pytest.fixture(params=["thunderbolt", "old-book"])
def theme(request):
    return request.param


class TestRelMe:
    """Social links in the footer must have rel='me'."""

    def test_social_links_have_rel_me(self, theme):
        env = _make_env(theme)
        html = env.get_template("base.html").render(**MOCK_CONTEXT)
        for name, url in MOCK_CONTEXT["SOCIAL"]:
            assert f'rel="me"' in html
            assert url in html

    def test_github_has_rel_me(self, theme):
        env = _make_env(theme)
        html = env.get_template("base.html").render(**MOCK_CONTEXT)
        assert 'href="https://github.com/tclancy" rel="me"' in html or \
               'href="https://github.com/tclancy"' in html and 'rel="me"' in html

    def test_bluesky_has_rel_me(self, theme):
        env = _make_env(theme)
        html = env.get_template("base.html").render(**MOCK_CONTEXT)
        assert "bsky.app" in html
        assert 'rel="me"' in html


class TestHCard:
    """Footer must contain a representative h-card."""

    def test_footer_has_hcard(self, theme):
        env = _make_env(theme)
        html = env.get_template("base.html").render(**MOCK_CONTEXT)
        assert "h-card" in html

    def test_hcard_has_p_name(self, theme):
        env = _make_env(theme)
        html = env.get_template("base.html").render(**MOCK_CONTEXT)
        assert "p-name" in html
        assert "Tom Clancy" in html

    def test_hcard_has_u_url(self, theme):
        env = _make_env(theme)
        html = env.get_template("base.html").render(**MOCK_CONTEXT)
        assert "u-url" in html
        assert 'href="https://tomclancy.info/"' in html


class _MockArticle:
    """Minimal mock for Pelican Article objects used in templates."""

    def __init__(self):
        from datetime import datetime as dt

        self.title = "Test Article Title"
        self.date = dt(2026, 5, 14, 12, 0)
        self.locale_date = "May 14, 2026"
        self.content = "<p>Article body content here.</p>"
        self.url = "test-article.html"
        self.category = _MockCategory()
        self.tags = []
        self.prev_article = None
        self.next_article = None

    @property
    def description(self):
        raise AttributeError


class _MockCategory:
    def __init__(self):
        self.url = "category/test"

    def __str__(self):
        return "Test"

    def __eq__(self, other):
        return False


class TestHEntry:
    """Article pages must have h-entry microformat classes."""

    def _render_article(self, theme):
        env = _make_env(theme)
        ctx = {
            **MOCK_CONTEXT,
            "article": _MockArticle(),
            "category": None,
            "page": None,
        }
        return env.get_template("article.html").render(**ctx)

    def test_article_has_h_entry(self, theme):
        html = self._render_article(theme)
        assert "h-entry" in html

    def test_title_has_p_name(self, theme):
        html = self._render_article(theme)
        assert "p-name" in html
        assert "Test Article Title" in html

    def test_date_has_dt_published(self, theme):
        html = self._render_article(theme)
        assert "dt-published" in html

    def test_body_has_e_content(self, theme):
        html = self._render_article(theme)
        assert "e-content" in html
        assert "Article body content here." in html

    def test_has_u_url(self, theme):
        html = self._render_article(theme)
        assert "u-url" in html
        assert "test-article.html" in html

    def test_has_p_author_hcard(self, theme):
        html = self._render_article(theme)
        assert "p-author" in html
        assert "h-card" in html
        assert "Tom Clancy" in html
