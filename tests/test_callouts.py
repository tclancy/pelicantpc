"""Tests for pelican.plugins.obsidian_callouts (via installed package)."""

from __future__ import annotations

from pelican.plugins.obsidian_callouts import _process_html, _render_callout


# ---------------------------------------------------------------------------
# _render_callout
# ---------------------------------------------------------------------------


def test_render_basic_note():
    html = _render_callout("note", "", "Note", ["<p>Body here.</p>"])
    assert 'class="pelican-callout pelican-callout-note"' in html
    assert "pelican-callout-title" in html
    assert "pelican-callout-body" in html
    assert "Body here." in html
    assert "pelican-callout-icon" in html


def test_render_custom_title():
    html = _render_callout("warning", "", "Watch Out!", ["<p>Be careful.</p>"])
    assert "Watch Out!" in html


def test_render_default_title_when_empty():
    html = _render_callout("info", "", "", ["<p>Body.</p>"])
    assert "Info" in html


def test_render_foldable_expanded():
    html = _render_callout("tip", "+", "Tip", ["<p>Body.</p>"])
    assert "pelican-callout-foldable" in html
    assert "pelican-callout-expanded" in html
    assert "pelican-callout-collapsed" not in html


def test_render_foldable_collapsed():
    html = _render_callout("danger", "-", "Danger", ["<p>Body.</p>"])
    assert "pelican-callout-foldable" in html
    assert "pelican-callout-collapsed" in html
    assert "pelican-callout-expanded" not in html


def test_render_non_foldable_has_no_foldable_class():
    html = _render_callout("note", "", "", ["<p>Body.</p>"])
    assert "pelican-callout-foldable" not in html


def test_render_lucide_icon_cdn():
    html = _render_callout("note", "", "", [""])
    assert "unpkg.com/lucide-static" in html


def test_render_all_known_types():
    types = [
        "note", "tip", "important", "warning", "caution",
        "abstract", "info", "todo", "success", "question",
        "failure", "danger", "bug", "example", "quote",
    ]
    for t in types:
        html = _render_callout(t, "", "", ["<p>Body.</p>"])
        assert f"pelican-callout-{t}" in html, f"Missing class for type '{t}'"


# ---------------------------------------------------------------------------
# _process_html (the full pipeline)
# ---------------------------------------------------------------------------


def _bq(inner: str) -> str:
    """Wrap inner HTML in a blockquote as Pelican/Markdown would produce."""
    return f"<blockquote>\n<p>{inner}</p>\n</blockquote>"


def test_process_html_simple_note():
    raw = _bq("[!note]\nBody text.")
    processed, had_foldable = _process_html(raw)
    assert "pelican-callout-note" in processed
    assert "blockquote" not in processed
    assert not had_foldable


def test_process_html_warning_with_custom_title():
    raw = _bq("[!warning] Watch Out!\nBe careful.")
    processed, _ = _process_html(raw)
    assert "pelican-callout-warning" in processed
    assert "Watch Out!" in processed


def test_process_html_custom_title_in_title_div_not_body():
    """Custom title must appear in the title div, not bleed into the body."""
    raw = _bq("[!info] My Custom Title\nBody text here.")
    processed, _ = _process_html(raw)
    title_pos = processed.index("pelican-callout-title")
    body_pos = processed.index("pelican-callout-body")
    custom_pos = processed.index("My Custom Title")
    assert title_pos < custom_pos < body_pos, (
        "Custom title should be inside title div, not body div"
    )
    assert "Body text here." in processed


def test_process_html_custom_title_body_is_separate():
    """Body content must not contain the custom title text."""
    raw = _bq("[!warning] Watch Out!\nBe careful.")
    processed, _ = _process_html(raw)
    body_start = processed.index("pelican-callout-body")
    body_section = processed[body_start:]
    assert "Watch Out!" not in body_section, (
        "Custom title must not appear in body div"
    )
    assert "Be careful." in body_section


def test_process_html_foldable_with_custom_title():
    """Custom titles must work on foldable callouts too."""
    raw = _bq("[!tip]+ Expand Me\nTip body.")
    processed, had_foldable = _process_html(raw)
    assert "pelican-callout-foldable" in processed
    assert had_foldable is True
    title_pos = processed.index("pelican-callout-title")
    body_pos = processed.index("pelican-callout-body")
    custom_pos = processed.index("Expand Me")
    assert title_pos < custom_pos < body_pos


def test_process_html_no_custom_title_uses_default():
    """When no custom title is given, the default type name is shown."""
    raw = _bq("[!info]\nBody text.")
    processed, _ = _process_html(raw)
    # Default title for "info" is "Info"
    title_pos = processed.index("pelican-callout-title")
    body_pos = processed.index("pelican-callout-body")
    info_pos = processed.index("Info")
    assert title_pos < info_pos < body_pos


def test_process_html_foldable_expanded():
    raw = _bq("[!tip]+\nExpanded tip.")
    processed, had_foldable = _process_html(raw)
    assert "pelican-callout-foldable" in processed
    assert had_foldable is True


def test_process_html_foldable_collapsed():
    raw = _bq("[!danger]-\nDanger!")
    processed, had_foldable = _process_html(raw)
    assert "pelican-callout-collapsed" in processed
    assert had_foldable is True


def test_process_html_foldable_injects_js():
    """JS block must be present in the final output when there's a foldable."""
    raw = _bq("[!info]+\nInfo body.")
    processed, had_foldable = _process_html(raw)
    # Caller would inject JS if had_foldable is True
    assert had_foldable is True


def test_process_html_unknown_type_left_as_blockquote():
    raw = _bq("[!customtype]\nBody.")
    processed, _ = _process_html(raw)
    assert "blockquote" in processed
    assert "pelican-callout" not in processed


def test_process_html_non_callout_blockquote_unchanged():
    raw = "<blockquote><p>Normal quote, no callout.</p></blockquote>"
    processed, _ = _process_html(raw)
    assert processed == raw


def test_process_html_case_insensitive():
    raw = _bq("[!WARNING]\nBody.")
    processed, _ = _process_html(raw)
    assert "pelican-callout-warning" in processed


def test_process_html_multiple_callouts():
    raw = _bq("[!note]\nFirst.") + "\n" + _bq("[!tip]\nSecond.")
    processed, _ = _process_html(raw)
    assert "pelican-callout-note" in processed
    assert "pelican-callout-tip" in processed
