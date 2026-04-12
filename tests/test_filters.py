"""Tests for custom Jinja2 filters defined in pelicanconf.py."""

from __future__ import annotations

import sys
import os

# Ensure pelicanconf is importable from the project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pelicanconf import _clean_summary, _strip_leading_h1


# ─── _strip_leading_h1 ────────────────────────────────────────────────────────


class TestStripLeadingH1:
    def test_strips_h1_at_start(self):
        html = "<h1>Me and .NET</h1><p>We get along so well.</p>"
        assert _strip_leading_h1(html) == "<p>We get along so well.</p>"

    def test_strips_h1_with_attributes(self):
        html = '<h1 class="title" id="top">Hello</h1><p>Body.</p>'
        result = _strip_leading_h1(html)
        assert "<h1" not in result
        assert "Hello" not in result
        assert "<p>Body.</p>" in result

    def test_strips_only_first_h1(self):
        html = "<h1>First</h1><p>Para.</p><h1>Second</h1>"
        result = _strip_leading_h1(html)
        assert "First" not in result
        assert "<h1>Second</h1>" in result

    def test_leaves_content_without_h1_unchanged(self):
        html = "<p>No heading here.</p>"
        assert _strip_leading_h1(html) == "<p>No heading here.</p>"

    def test_leading_whitespace_trimmed(self):
        html = "\n  <h1>Title</h1>\n<p>Body.</p>"
        result = _strip_leading_h1(html)
        assert "<h1>" not in result
        assert "Title" not in result

    def test_handles_none(self):
        assert _strip_leading_h1(None) == ""

    def test_handles_empty_string(self):
        assert _strip_leading_h1("") == ""

    def test_does_not_strip_h2(self):
        html = "<h2>Section</h2><p>Body.</p>"
        result = _strip_leading_h1(html)
        assert "<h2>Section</h2>" in result

    def test_multiline_h1_stripped(self):
        html = "<h1>\n  Long Title\n  Spanning Lines\n</h1><p>Body.</p>"
        result = _strip_leading_h1(html)
        assert "<h1>" not in result
        assert "<p>Body.</p>" in result


# ─── _clean_summary ───────────────────────────────────────────────────────────


class TestCleanSummary:
    def test_strips_h1(self):
        html = "<h1>Title</h1><p>First paragraph.</p>"
        result = _clean_summary(html)
        assert "<h1>" not in result
        assert "Title" not in result
        assert "First paragraph." in result

    def test_strips_h2_through_h6(self):
        for level in range(2, 7):
            html = f"<h{level}>Section</h{level}><p>Para.</p>"
            result = _clean_summary(html)
            assert f"<h{level}>" not in result, f"h{level} not stripped"
            assert "Section" not in result, f"h{level} text not stripped"

    def test_strips_pelican_callout_block(self):
        html = (
            "<p>Before.</p>"
            '<div class="pelican-callout pelican-callout-note">'
            '<div class="pelican-callout-title">Note</div>'
            '<div class="pelican-callout-body"><p>Inside callout.</p></div>'
            "</div>"
            "<p>After.</p>"
        )
        result = _clean_summary(html)
        assert "Inside callout." not in result
        assert "pelican-callout" not in result
        assert "Before." in result
        assert "After." in result

    def test_preserves_regular_paragraphs(self):
        html = "<p>First paragraph.</p><p>Second paragraph.</p>"
        result = _clean_summary(html)
        assert "First paragraph." in result
        assert "Second paragraph." in result

    def test_preserves_inline_formatting(self):
        html = "<p>Some <em>italic</em> and <strong>bold</strong> text.</p>"
        result = _clean_summary(html)
        assert "<em>italic</em>" in result
        assert "<strong>bold</strong>" in result

    def test_preserves_links(self):
        html = '<p>Click <a href="/foo">here</a>.</p>'
        result = _clean_summary(html)
        assert '<a href="/foo">here</a>' in result

    def test_handles_none(self):
        assert _clean_summary(None) == ""

    def test_handles_empty_string(self):
        assert _clean_summary("") == ""

    def test_strips_heading_including_inner_tags(self):
        html = "<h1><em>Fancy</em> Title</h1><p>Body.</p>"
        result = _clean_summary(html)
        assert "Fancy" not in result
        assert "Title" not in result

    def test_strips_nested_callout_content(self):
        # Nested divs inside the callout should all be removed
        html = (
            '<div class="pelican-callout pelican-callout-warning">'
            '<div class="pelican-callout-title"><span>⚠</span> Watch out</div>'
            '<div class="pelican-callout-body">'
            "<p>Line one.</p><p>Line two.</p>"
            "</div>"
            "</div>"
            "<p>Safe text.</p>"
        )
        result = _clean_summary(html)
        assert "Watch out" not in result
        assert "Line one." not in result
        assert "Safe text." in result

    def test_h1_before_callout_both_stripped(self):
        html = (
            "<h1>Title</h1>"
            '<div class="pelican-callout pelican-callout-note">'
            '<div class="pelican-callout-title">Note</div>'
            '<div class="pelican-callout-body"><p>Callout body.</p></div>'
            "</div>"
            "<p>Normal para.</p>"
        )
        result = _clean_summary(html)
        assert "Title" not in result
        assert "Callout body." not in result
        assert "Normal para." in result
