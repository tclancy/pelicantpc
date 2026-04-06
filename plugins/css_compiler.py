"""CSS compiler plugin for Pelican.

Reads CSS source files from their theme source directories, concatenates them
(optionally minifying), and writes the result to the output directory.

This supports the "combined" theme pattern: each theme owns its own CSS source
file, but all themes are compiled into a single output file so the HTML
template only needs one <link> tag. The active theme is switched at runtime
via the `data-theme` attribute on `<html>`.

Configuration (in pelicanconf.py / publishconf.py):

    CSS_SOURCES = [
        "themes/thunderbolt/static/css/thunderbolt.css",
        "themes/old-book/static/css/old-book.css",
    ]
    CSS_OUTPUT   = "theme/css/combined.css"   # relative to output_path
    CSS_MINIFY   = False                       # True for production builds

Defaults: CSS_OUTPUT = "theme/css/combined.css", CSS_MINIFY = False.
If CSS_SOURCES is empty or missing, the plugin is a no-op.
"""

from __future__ import annotations

from pathlib import Path

from pelican import signals


def _read_source(path: str | Path) -> str:
    """Read one CSS source file, wrapping it in a comment banner."""
    p = Path(path)
    with open(p) as f:
        content = f.read()
    banner = f"/* === {p.name} === */"
    return f"{banner}\n{content}"


def compile_css(pelican_obj) -> None:
    """Pelican signal handler — concatenate CSS sources into the output file.

    Connected to `signals.finalized` so it runs after Pelican has written
    all content and copied the theme's static files.  The combined file is
    written directly into the output tree, not into the source theme, so it
    never accidentally gets committed to version control.
    """
    settings = pelican_obj.settings
    sources: list[str] = settings.get("CSS_SOURCES", [])
    if not sources:
        return

    output_rel: str = settings.get("CSS_OUTPUT", "theme/css/combined.css")
    minify: bool = settings.get("CSS_MINIFY", False)

    parts: list[str] = []
    for src in sources:
        try:
            parts.append(_read_source(src))
        except OSError as e:
            print(f"[css_compiler] Warning: cannot read {src!r}: {e}")

    if not parts:
        return

    combined = "\n\n".join(parts)

    if minify:
        try:
            import csscompressor

            combined = csscompressor.compress(combined)
        except ImportError:
            print(
                "[css_compiler] Warning: CSS_MINIFY=True but csscompressor is not installed. "
                "Install with: uv add csscompressor"
            )

    out_path = Path(pelican_obj.output_path) / output_rel
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(combined, encoding="utf-8")


def register() -> None:
    signals.finalized.connect(compile_css)
