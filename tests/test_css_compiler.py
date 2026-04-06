"""Tests for plugins/css_compiler.py — CSS concatenation and minification."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "plugins"))
import css_compiler


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_pelican(settings: dict, output_path: str) -> MagicMock:
    """Build a minimal mock of the Pelican object passed to finalized handlers."""
    obj = MagicMock()
    obj.settings = settings
    obj.output_path = output_path
    return obj


# ---------------------------------------------------------------------------
# _read_source
# ---------------------------------------------------------------------------


class TestReadSource:
    def test_returns_content_with_banner(self, tmp_path: Path):
        css = tmp_path / "theme.css"
        css.write_text("body { color: red; }")
        result = css_compiler._read_source(css)
        assert "/* === theme.css === */" in result
        assert "body { color: red; }" in result

    def test_banner_contains_filename_only_not_full_path(self, tmp_path: Path):
        css = tmp_path / "deep" / "path" / "my-theme.css"
        css.parent.mkdir(parents=True)
        css.write_text("p { font-size: 16px; }")
        result = css_compiler._read_source(css)
        assert "my-theme.css" in result
        assert "deep" not in result  # full path should not appear in banner

    def test_raises_on_missing_file(self, tmp_path: Path):
        with pytest.raises(OSError):
            css_compiler._read_source(tmp_path / "nonexistent.css")


# ---------------------------------------------------------------------------
# compile_css — no-op cases
# ---------------------------------------------------------------------------


class TestCompileCssNoOp:
    def test_no_css_sources_key_is_noop(self, tmp_path: Path):
        pelican = _make_pelican({}, str(tmp_path))
        css_compiler.compile_css(pelican)
        # Nothing should be written
        assert not any(tmp_path.rglob("*.css"))

    def test_empty_css_sources_is_noop(self, tmp_path: Path):
        pelican = _make_pelican({"CSS_SOURCES": []}, str(tmp_path))
        css_compiler.compile_css(pelican)
        assert not any(tmp_path.rglob("*.css"))


# ---------------------------------------------------------------------------
# compile_css — happy path
# ---------------------------------------------------------------------------


class TestCompileCssOutput:
    def test_writes_combined_css_to_default_output(self, tmp_path: Path):
        src = tmp_path / "src"
        src.mkdir()
        (src / "a.css").write_text("a { color: blue; }")
        (src / "b.css").write_text("b { color: red; }")

        output_dir = tmp_path / "output"
        output_dir.mkdir()
        settings = {
            "CSS_SOURCES": [str(src / "a.css"), str(src / "b.css")],
        }
        pelican = _make_pelican(settings, str(output_dir))
        css_compiler.compile_css(pelican)

        out = output_dir / "theme" / "css" / "combined.css"
        assert out.exists()
        content = out.read_text()
        assert "a { color: blue; }" in content
        assert "b { color: red; }" in content

    def test_respects_custom_css_output_path(self, tmp_path: Path):
        src = tmp_path / "src"
        src.mkdir()
        (src / "style.css").write_text("h1 { font-size: 2rem; }")

        output_dir = tmp_path / "output"
        output_dir.mkdir()
        settings = {
            "CSS_SOURCES": [str(src / "style.css")],
            "CSS_OUTPUT": "assets/all.css",
        }
        pelican = _make_pelican(settings, str(output_dir))
        css_compiler.compile_css(pelican)

        out = output_dir / "assets" / "all.css"
        assert out.exists()

    def test_creates_output_parent_directories(self, tmp_path: Path):
        src = tmp_path / "style.css"
        src.write_text("p { margin: 0; }")
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        settings = {
            "CSS_SOURCES": [str(src)],
            "CSS_OUTPUT": "very/deep/nested/combined.css",
        }
        pelican = _make_pelican(settings, str(output_dir))
        css_compiler.compile_css(pelican)
        assert (output_dir / "very" / "deep" / "nested" / "combined.css").exists()

    def test_files_separated_by_blank_line(self, tmp_path: Path):
        a = tmp_path / "a.css"
        b = tmp_path / "b.css"
        a.write_text("a{}")
        b.write_text("b{}")
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        settings = {"CSS_SOURCES": [str(a), str(b)]}
        pelican = _make_pelican(settings, str(output_dir))
        css_compiler.compile_css(pelican)
        content = (output_dir / "theme" / "css" / "combined.css").read_text()
        # Two source sections should be separated by at least one blank line
        assert "\n\n" in content


# ---------------------------------------------------------------------------
# compile_css — minification
# ---------------------------------------------------------------------------


class TestCompileCssMinify:
    def test_minify_false_preserves_whitespace(self, tmp_path: Path):
        src = tmp_path / "style.css"
        src.write_text("body {\n  color: red;\n}\n")
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        settings = {"CSS_SOURCES": [str(src)], "CSS_MINIFY": False}
        pelican = _make_pelican(settings, str(output_dir))
        css_compiler.compile_css(pelican)
        content = (output_dir / "theme" / "css" / "combined.css").read_text()
        assert "\n" in content  # whitespace preserved

    def test_minify_true_requires_csscompressor(self, tmp_path: Path):
        """With CSS_MINIFY=True, csscompressor must be called if available."""
        src = tmp_path / "style.css"
        src.write_text("body { color: red; margin: 0; }")
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        settings = {"CSS_SOURCES": [str(src)], "CSS_MINIFY": True}
        pelican = _make_pelican(settings, str(output_dir))

        mock_compress = MagicMock(return_value="body{color:red;margin:0}")
        mock_csscompressor = MagicMock()
        mock_csscompressor.compress = mock_compress

        with patch.dict("sys.modules", {"csscompressor": mock_csscompressor}):
            css_compiler.compile_css(pelican)

        mock_compress.assert_called_once()
        out = (output_dir / "theme" / "css" / "combined.css").read_text()
        assert out == "body{color:red;margin:0}"

    def test_minify_true_without_csscompressor_falls_back_to_unminified(
        self, tmp_path: Path, capsys
    ):
        """If csscompressor is not installed, a warning is printed and output is written."""
        src = tmp_path / "style.css"
        src.write_text("body { color: blue; }")
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        settings = {"CSS_SOURCES": [str(src)], "CSS_MINIFY": True}
        pelican = _make_pelican(settings, str(output_dir))

        with patch.dict("sys.modules", {"csscompressor": None}):
            css_compiler.compile_css(pelican)

        out = output_dir / "theme" / "css" / "combined.css"
        assert out.exists()
        captured = capsys.readouterr()
        assert "csscompressor" in captured.out


# ---------------------------------------------------------------------------
# compile_css — error handling
# ---------------------------------------------------------------------------


class TestCompileCssErrorHandling:
    def test_missing_source_file_prints_warning_and_continues(
        self, tmp_path: Path, capsys
    ):
        """A missing CSS source must not abort the run — warn and skip."""
        real_src = tmp_path / "real.css"
        real_src.write_text("p { color: green; }")
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        settings = {
            "CSS_SOURCES": [str(tmp_path / "missing.css"), str(real_src)],
        }
        pelican = _make_pelican(settings, str(output_dir))
        css_compiler.compile_css(pelican)

        captured = capsys.readouterr()
        assert "missing.css" in captured.out or "Warning" in captured.out

        out = output_dir / "theme" / "css" / "combined.css"
        assert out.exists()
        assert "p { color: green; }" in out.read_text()

    def test_all_sources_missing_writes_nothing(self, tmp_path: Path):
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        settings = {"CSS_SOURCES": [str(tmp_path / "ghost.css")]}
        pelican = _make_pelican(settings, str(output_dir))
        css_compiler.compile_css(pelican)
        assert not any(output_dir.rglob("*.css"))


# ---------------------------------------------------------------------------
# register
# ---------------------------------------------------------------------------


class TestRegister:
    def test_register_connects_to_finalized(self):
        """register() must connect compile_css to pelican's finalized signal."""
        connected: list = []

        mock_signals = MagicMock()
        mock_signals.finalized.connect.side_effect = lambda fn: connected.append(fn)

        with patch.object(css_compiler, "signals", mock_signals):
            css_compiler.register()

        assert css_compiler.compile_css in connected
