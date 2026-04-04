"""Tests for plugins/ornaments.py — subheader injection and inline footnotes."""

from __future__ import annotations

from unittest.mock import MagicMock


# Import the plugin directly (not via pelican's loader) so we can unit-test
# the processing functions in isolation.
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "plugins"))
import ornaments


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_content(html: str, subheader: str | None = None) -> MagicMock:
    """Return a mock Pelican content object with a _content attribute."""
    obj = MagicMock(spec=[])
    obj._content = html
    if subheader is not None:
        obj.subheader = subheader
    else:
        # Make getattr(obj, 'subheader', None) return None
        del obj.subheader
    return obj


# ---------------------------------------------------------------------------
# Subheader injection
# ---------------------------------------------------------------------------


class TestSubheader:
    def test_injects_rule_ornament_when_present(self):
        content = _make_content("<p>Body text.</p>", subheader="My Section")
        ornaments._inject_subheader(content)
        assert '<div class="rule-ornament">' in content._content
        assert "❧ My Section ❦" in content._content

    def test_ornament_precedes_body(self):
        content = _make_content("<p>Body text.</p>", subheader="Intro")
        ornaments._inject_subheader(content)
        ornament_pos = content._content.index('<div class="rule-ornament">')
        body_pos = content._content.index("<p>Body text.</p>")
        assert ornament_pos < body_pos

    def test_no_subheader_leaves_content_unchanged(self):
        original = "<p>Body text.</p>"
        content = _make_content(original)
        ornaments._inject_subheader(content)
        assert content._content == original

    def test_empty_subheader_leaves_content_unchanged(self):
        original = "<p>Body text.</p>"
        content = _make_content(original, subheader="")
        ornaments._inject_subheader(content)
        assert content._content == original

    def test_none_content_not_crashed(self):
        """Static files and other objects may have _content=None; don't crash."""
        content = _make_content(None, subheader="Intro")
        ornaments._inject_subheader(content)  # should not raise
        assert content._content is None

    def test_subheader_text_appears_between_ornament_markers(self):
        content = _make_content("<p>X</p>", subheader="Fancy Title")
        ornaments._inject_subheader(content)
        assert "❧ Fancy Title ❦" in content._content

    def test_subheader_with_html_special_chars(self):
        content = _make_content("<p>Body.</p>", subheader="Bread & Butter")
        ornaments._inject_subheader(content)
        assert "Bread & Butter" in content._content


# ---------------------------------------------------------------------------
# Inline footnotes
# ---------------------------------------------------------------------------


class TestFootnotes:
    def test_single_footnote_replaced(self):
        content = _make_content("<p>Text[ref]note[/ref] after.</p>")
        ornaments._process_footnotes(content)
        assert "[ref]" not in content._content
        assert "[/ref]" not in content._content
        assert '<sup class="footnote-ref"' in content._content
        assert '<div class="footnote"' in content._content
        assert "1. note" in content._content

    def test_superscript_contains_number(self):
        content = _make_content("<p>Text[ref]note[/ref].</p>")
        ornaments._process_footnotes(content)
        assert ">1<" in content._content

    def test_ids_set_on_sup_and_div(self):
        content = _make_content("<p>Text[ref]note[/ref].</p>")
        ornaments._process_footnotes(content)
        assert 'id="fnref-1"' in content._content
        assert 'id="fn-1"' in content._content

    def test_multiple_footnotes_numbered_sequentially(self):
        content = _make_content("<p>[ref]first[/ref] and [ref]second[/ref].</p>")
        ornaments._process_footnotes(content)
        assert "1. first" in content._content
        assert "2. second" in content._content
        assert 'id="fnref-1"' in content._content
        assert 'id="fnref-2"' in content._content

    def test_no_refs_leaves_content_unchanged(self):
        original = "<p>Plain text, no refs.</p>"
        content = _make_content(original)
        ornaments._process_footnotes(content)
        assert content._content == original

    def test_none_content_not_crashed(self):
        """Static files and other objects may have _content=None; don't crash."""
        content = _make_content(None)
        ornaments._process_footnotes(content)  # should not raise
        assert content._content is None

    def test_multiline_footnote_text_preserved(self):
        content = _make_content("<p>Text[ref]line one\nline two[/ref].</p>")
        ornaments._process_footnotes(content)
        assert "line one" in content._content
        assert "line two" in content._content
        assert "[ref]" not in content._content

    def test_footnote_text_trimmed(self):
        content = _make_content("<p>Text[ref]  padded  [/ref].</p>")
        ornaments._process_footnotes(content)
        assert "1. padded" in content._content
        assert "padded  " not in content._content

    def test_refs_inside_code_block_not_processed(self):
        html = "<p>Outside.</p><code>[ref]skip me[/ref]</code>"
        content = _make_content(html)
        ornaments._process_footnotes(content)
        assert "[ref]skip me[/ref]" in content._content

    def test_refs_inside_pre_block_not_processed(self):
        html = "<pre><code>[ref]skip me[/ref]</code></pre>"
        content = _make_content(html)
        ornaments._process_footnotes(content)
        assert "[ref]skip me[/ref]" in content._content

    def test_ref_outside_code_still_processed_when_code_present(self):
        html = "<code>[ref]skip[/ref]</code><p>Text[ref]process me[/ref].</p>"
        content = _make_content(html)
        ornaments._process_footnotes(content)
        assert "[ref]skip[/ref]" in content._content
        assert "[ref]process me[/ref]" not in content._content
        assert "1. process me" in content._content


# ---------------------------------------------------------------------------
# _process_content (combined)
# ---------------------------------------------------------------------------


class TestProcessContent:
    def test_both_subheader_and_footnotes_applied(self):
        content = _make_content("<p>Text[ref]note[/ref].</p>", subheader="Chapter One")
        ornaments._process_content(content)
        assert "❧ Chapter One ❦" in content._content
        assert "1. note" in content._content
        assert "[ref]" not in content._content

    def test_subheader_before_footnote_content(self):
        content = _make_content("<p>Text[ref]note[/ref].</p>", subheader="Intro")
        ornaments._process_content(content)
        ornament_pos = content._content.index('<div class="rule-ornament">')
        fn_pos = content._content.index('<div class="footnote"')
        assert ornament_pos < fn_pos
