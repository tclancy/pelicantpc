"""Tests for plugins/opengraph.py — OpenGraph and Twitter Card meta tags."""

from __future__ import annotations

import sys
import os
from datetime import datetime
from unittest.mock import MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "plugins"))
import opengraph


DEFAULT_SETTINGS = {
    "SITEURL": "https://tomclancy.info",
    "SITENAME": "Tom Clancy",
}


def _make_content(
    title: str = "Test Post",
    html: str = "<p>Hello world.</p>",
    url: str = "test-post.html",
    *,
    date: datetime | None = datetime(2026, 5, 14, 12, 0),
    description: str | None = None,
    summary: str | None = None,
    og_image: str | None = None,
    og_description: str | None = None,
    og_title: str | None = None,
    og_type: str | None = None,
    author: str | None = "Tom Clancy",
    tags: list[str] | None = None,
    modified: datetime | None = None,
    settings: dict | None = None,
) -> MagicMock:
    """Build a mock Pelican content object."""
    obj = MagicMock(spec=[])
    obj.title = title
    obj._content = html
    obj.url = url
    obj.settings = {**DEFAULT_SETTINGS, **(settings or {})}

    if date is not None:
        obj.date = date
    else:
        del obj.date

    if description is not None:
        obj.description = description
    else:
        del obj.description

    if summary is not None:
        obj._summary = summary
    else:
        del obj._summary

    if og_image is not None:
        obj.og_image = og_image
    else:
        del obj.og_image

    if og_description is not None:
        obj.og_description = og_description
    else:
        del obj.og_description

    if og_title is not None:
        obj.og_title = og_title
    else:
        del obj.og_title

    if og_type is not None:
        obj.og_type = og_type
    else:
        del obj.og_type

    if author is not None:
        obj.author = author
    else:
        del obj.author

    if tags is not None:
        obj.tags = tags
    else:
        del obj.tags

    if modified is not None:
        obj.modified = modified
    else:
        del obj.modified

    return obj


class TestBasicOGTags:
    def test_title_from_article(self):
        c = _make_content(title="My Great Post")
        opengraph.process_content(c)
        assert c.opengraph["title"] == "My Great Post"

    def test_og_title_override(self):
        c = _make_content(title="Long Title", og_title="Short")
        opengraph.process_content(c)
        assert c.opengraph["title"] == "Short"

    def test_type_article_when_dated(self):
        c = _make_content()
        opengraph.process_content(c)
        assert c.opengraph["type"] == "article"

    def test_type_website_when_no_date(self):
        c = _make_content(date=None)
        opengraph.process_content(c)
        assert c.opengraph["type"] == "website"

    def test_og_type_override(self):
        c = _make_content(og_type="profile")
        opengraph.process_content(c)
        assert c.opengraph["type"] == "profile"

    def test_url_absolute(self):
        c = _make_content(url="posts/hello.html")
        opengraph.process_content(c)
        assert c.opengraph["url"] == "https://tomclancy.info/posts/hello.html"

    def test_url_already_absolute(self):
        c = _make_content(url="https://other.com/page")
        opengraph.process_content(c)
        assert c.opengraph["url"] == "https://other.com/page"

    def test_site_name(self):
        c = _make_content()
        opengraph.process_content(c)
        assert c.opengraph["site_name"] == "Tom Clancy"

    def test_title_strips_typogrify_nbsp(self):
        c = _make_content(title="A&nbsp;Confession")
        opengraph.process_content(c)
        assert c.opengraph["title"] == "A Confession"

    def test_title_strips_html_tags(self):
        c = _make_content(title="<em>Italic</em> Title")
        opengraph.process_content(c)
        assert c.opengraph["title"] == "Italic Title"


class TestDescription:
    def test_og_description_override(self):
        c = _make_content(description="Meta desc", og_description="Social blurb")
        opengraph.process_content(c)
        assert c.opengraph["description"] == "Social blurb"

    def test_falls_back_to_description(self):
        c = _make_content(description="Article description")
        opengraph.process_content(c)
        assert c.opengraph["description"] == "Article description"

    def test_falls_back_to_summary(self):
        c = _make_content(html="<p>Body</p>", summary="<p>Summary text here</p>")
        opengraph.process_content(c)
        assert c.opengraph["description"] == "Summary text here"

    def test_falls_back_to_content_truncated(self):
        long_text = "A " * 200
        c = _make_content(html=f"<p>{long_text}</p>")
        opengraph.process_content(c)
        assert len(c.opengraph["description"]) <= 201
        assert c.opengraph["description"].endswith("…")

    def test_strips_html_from_description(self):
        c = _make_content(description="<strong>Bold</strong> and <em>italic</em>")
        opengraph.process_content(c)
        assert c.opengraph["description"] == "Bold and italic"

    def test_unescapes_entities(self):
        c = _make_content(description="Tom &amp; Jerry&#39;s place")
        opengraph.process_content(c)
        assert c.opengraph["description"] == "Tom & Jerry's place"

    def test_empty_when_nothing_available(self):
        c = _make_content(html="")
        opengraph.process_content(c)
        assert c.opengraph["description"] == ""


class TestImage:
    def test_og_image_override(self):
        c = _make_content(og_image="https://cdn.example.com/hero.jpg")
        opengraph.process_content(c)
        assert c.opengraph["image"] == "https://cdn.example.com/hero.jpg"

    def test_og_image_relative_made_absolute(self):
        c = _make_content(og_image="/images/hero.jpg")
        opengraph.process_content(c)
        assert c.opengraph["image"] == "https://tomclancy.info/images/hero.jpg"

    def test_extracts_first_img_from_content(self):
        html = (
            '<p>Text</p><img src="/images/photo.jpg" alt="photo"><img src="/other.jpg">'
        )
        c = _make_content(html=html)
        opengraph.process_content(c)
        assert c.opengraph["image"] == "https://tomclancy.info/images/photo.jpg"

    def test_site_default_image(self):
        c = _make_content(
            html="<p>No images here</p>",
            settings={"OG_DEFAULT_IMAGE": "/images/default-og.jpg"},
        )
        opengraph.process_content(c)
        assert c.opengraph["image"] == "https://tomclancy.info/images/default-og.jpg"

    def test_none_when_no_image_available(self):
        c = _make_content(html="<p>No images</p>")
        opengraph.process_content(c)
        assert c.opengraph["image"] is None


class TestArticleMetadata:
    def test_published_time(self):
        dt = datetime(2026, 3, 15, 10, 30)
        c = _make_content(date=dt)
        opengraph.process_content(c)
        assert c.opengraph["article_published_time"] == dt.isoformat()

    def test_modified_time(self):
        dt = datetime(2026, 3, 15, 10, 30)
        mod = datetime(2026, 4, 1, 8, 0)
        c = _make_content(date=dt, modified=mod)
        opengraph.process_content(c)
        assert c.opengraph["article_modified_time"] == mod.isoformat()

    def test_no_modified_key_when_absent(self):
        c = _make_content()
        opengraph.process_content(c)
        assert "article_modified_time" not in c.opengraph

    def test_author(self):
        c = _make_content(author="Tom Clancy")
        opengraph.process_content(c)
        assert c.opengraph["article_author"] == "Tom Clancy"

    def test_tags(self):
        c = _make_content(tags=["python", "pelican", "web"])
        opengraph.process_content(c)
        assert c.opengraph["article_tags"] == ["python", "pelican", "web"]

    def test_no_article_fields_for_pages(self):
        c = _make_content(date=None)
        opengraph.process_content(c)
        assert "article_published_time" not in c.opengraph
        assert "article_author" not in c.opengraph


class TestTwitterCard:
    def test_summary_large_image_when_image_present(self):
        c = _make_content(og_image="https://example.com/img.jpg")
        opengraph.process_content(c)
        assert c.opengraph["twitter_card"] == "summary_large_image"

    def test_summary_when_no_image(self):
        c = _make_content(html="<p>no images</p>")
        opengraph.process_content(c)
        assert c.opengraph["twitter_card"] == "summary"

    def test_twitter_username(self):
        c = _make_content(
            settings={"OG_TWITTER_USERNAME": "@tclancy"},
        )
        opengraph.process_content(c)
        assert c.opengraph["twitter_site"] == "@tclancy"

    def test_no_twitter_site_by_default(self):
        c = _make_content()
        opengraph.process_content(c)
        assert "twitter_site" not in c.opengraph


class TestHelpers:
    def test_strip_tags(self):
        assert opengraph._strip_tags("<p>Hello <b>world</b></p>") == "Hello world"

    def test_strip_tags_collapses_whitespace(self):
        assert (
            opengraph._strip_tags("<p>Line one</p>\n<p>Line two</p>")
            == "Line one Line two"
        )

    def test_strip_tags_with_entities(self):
        assert opengraph._strip_tags("&amp; &lt;tag&gt;") == "& <tag>"

    def test_truncate_short(self):
        assert opengraph._truncate("short") == "short"

    def test_truncate_long(self):
        text = "word " * 100
        result = opengraph._truncate(text, 50)
        assert len(result) <= 51
        assert result.endswith("…")

    def test_truncate_empty(self):
        assert opengraph._truncate("") == ""
        assert opengraph._truncate(None) == ""

    def test_make_absolute_none(self):
        assert opengraph._make_absolute(None, "https://x.com") is None

    def test_make_absolute_already(self):
        assert (
            opengraph._make_absolute("https://cdn.com/img.jpg", "https://x.com")
            == "https://cdn.com/img.jpg"
        )

    def test_make_absolute_relative(self):
        assert (
            opengraph._make_absolute("images/photo.jpg", "https://x.com")
            == "https://x.com/images/photo.jpg"
        )

    def test_make_absolute_leading_slash(self):
        assert (
            opengraph._make_absolute("/images/photo.jpg", "https://x.com")
            == "https://x.com/images/photo.jpg"
        )

    def test_first_image_src(self):
        html = '<p>Text</p><img src="photo.jpg" alt="x"><img src="other.jpg">'
        assert opengraph._first_image_src(html) == "photo.jpg"

    def test_first_image_src_double_quotes(self):
        assert opengraph._first_image_src('<img src="a.png">') == "a.png"

    def test_first_image_src_single_quotes(self):
        assert opengraph._first_image_src("<img src='b.png'>") == "b.png"

    def test_first_image_src_none(self):
        assert opengraph._first_image_src("<p>no img</p>") is None

    def test_first_image_src_empty(self):
        assert opengraph._first_image_src("") is None
