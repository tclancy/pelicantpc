"""Pelican plugin: Obsidian-style callouts.

Syntax (same as Obsidian, degrades gracefully to blockquote elsewhere)::

    > [!note]
    > Body text here.

    > [!warning] Custom Title
    > Warning body.

    > [!tip]+
    > Foldable, expanded by default.

    > [!danger]-
    > Foldable, collapsed by default.

Produces::

    <div class="pelican-callout pelican-callout-note">
      <div class="pelican-callout-title">
        <img src="https://unpkg.com/lucide-static@0.483.0/icons/info.svg"
             class="pelican-callout-icon" alt="note" width="18" height="18">
        Note
      </div>
      <div class="pelican-callout-body">
        <p>Body text here.</p>
      </div>
    </div>

For foldable callouts a ``<details>``/``<summary>`` wrapper is used, and a
tiny inline ``<script>`` block is injected once per page (guarded by a check
for the ``pelican-callout-init`` variable so it only fires once even with
multiple callouts on a page).

CSS hooks:
  - ``.pelican-callout`` — outermost container
  - ``.pelican-callout-[type]`` — e.g. ``.pelican-callout-warning``
  - ``.pelican-callout-title``
  - ``.pelican-callout-icon``
  - ``.pelican-callout-body``
  - ``.pelican-callout-foldable``
  - ``.pelican-callout-expanded``
  - ``.pelican-callout-collapsed``
"""

from __future__ import annotations

import re
from html import escape

from pelican import signals
from pelican.contents import Article, Page

# ---------------------------------------------------------------------------
# Callout type → Lucide icon name
# ---------------------------------------------------------------------------

_LUCIDE_CDN = "https://unpkg.com/lucide-static@0.483.0/icons/{icon}.svg"

_TYPE_ICONS: dict[str, str] = {
    "note": "pencil",
    "tip": "flame",
    "important": "message-square-warning",
    "warning": "triangle-alert",
    "caution": "octagon-alert",
    "abstract": "clipboard-list",
    "info": "info",
    "todo": "circle-check",
    "success": "check",
    "question": "circle-help",
    "failure": "x",
    "danger": "zap",
    "bug": "bug",
    "example": "list",
    "quote": "quote",
}

_DEFAULT_TITLES: dict[str, str] = {k: k.capitalize() for k in _TYPE_ICONS}

# Match the opening line: > [!type], > [!type]+, > [!type]-, > [!type] Custom Title
_CALLOUT_RE = re.compile(
    r"^\s*>\s*\[!(?P<type>[a-z]+)\](?P<fold>[+-]?)\s*(?P<title>[^\n]*)",
    re.IGNORECASE,
)

# Match subsequent blockquote lines: > body text
_BQ_LINE_RE = re.compile(r"^\s*>\s?(?P<content>.*)")

# Minimal JS to wire foldable callouts — injected once per page
_FOLD_JS = """\
<script>
(function(){
  if(window.__pelican_callout_init)return;
  window.__pelican_callout_init=true;
  document.querySelectorAll('.pelican-callout-foldable').forEach(function(d){
    var s=d.querySelector('.pelican-callout-title');
    var b=d.querySelector('.pelican-callout-body');
    if(!s||!b)return;
    s.style.cursor='pointer';
    s.addEventListener('click',function(){
      d.classList.toggle('pelican-callout-collapsed');
      d.classList.toggle('pelican-callout-expanded');
    });
  });
})();
</script>"""


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def _icon_html(callout_type: str) -> str:
    icon = _TYPE_ICONS.get(callout_type, "info")
    url = _LUCIDE_CDN.format(icon=icon)
    return (
        f'<img src="{url}" class="pelican-callout-icon"'
        f' alt="{escape(callout_type)}" width="18" height="18">'
    )


def _render_callout(callout_type: str, fold: str, title: str, body_lines: list[str]) -> str:
    """Return the HTML for one callout block."""
    ct = callout_type.lower()
    safe_type = escape(ct)
    title = title.strip() or _DEFAULT_TITLES.get(ct, ct.capitalize())
    safe_title = escape(title)
    icon = _icon_html(ct)

    body_html = "\n".join(body_lines)

    is_foldable = bool(fold)
    classes = f"pelican-callout pelican-callout-{safe_type}"
    if is_foldable:
        classes += " pelican-callout-foldable"
        classes += " pelican-callout-collapsed" if fold == "-" else " pelican-callout-expanded"

    title_tag = (
        f'<div class="pelican-callout-title">{icon} {safe_title}</div>'
    )
    body_tag = f'<div class="pelican-callout-body">\n{body_html}\n</div>'

    if is_foldable:
        return (
            f'<div class="{classes}">\n'
            f"{title_tag}\n"
            f"{body_tag}\n"
            f"</div>"
        )
    return (
        f'<div class="{classes}">\n'
        f"{title_tag}\n"
        f"{body_tag}\n"
        f"</div>"
    )


# ---------------------------------------------------------------------------
# HTML post-processing
# ---------------------------------------------------------------------------


def _process_html(html: str) -> tuple[str, bool]:
    """Replace <blockquote> callout blocks in rendered HTML.

    Pelican/Markdown already converts blockquotes to ``<blockquote>`` HTML.
    We post-process the HTML rather than hooking into the Markdown pipeline
    so this works with any Markdown extension and remains simple.

    Returns ``(processed_html, had_foldable)`` so the caller knows whether
    to inject the fold JS.
    """
    # Match <blockquote>…</blockquote> blocks that contain a callout header
    bq_re = re.compile(
        r"<blockquote>\s*<p>\[!(?P<type>[a-z]+)\](?P<fold>[+-]?)[^\S\n]*(?P<title>[^<\n]*)"
        r"(?:<br\s*/?>|\n)?(?P<body>.*?)</p>(?P<rest>.*?)</blockquote>",
        re.IGNORECASE | re.DOTALL,
    )

    had_foldable = False

    def _replace(m: re.Match) -> str:
        nonlocal had_foldable
        callout_type = m.group("type").lower()
        fold = m.group("fold")
        title = m.group("title").strip()
        body = m.group("body").strip()
        rest = m.group("rest").strip()

        if callout_type not in _TYPE_ICONS:
            return m.group(0)  # unknown type — leave as blockquote

        if fold:
            had_foldable = True

        # Combine inline body + any remaining <p> tags from rest
        full_body = ""
        if body:
            full_body = f"<p>{body}</p>\n"
        if rest:
            full_body += rest

        return _render_callout(callout_type, fold, title, [full_body])

    processed = bq_re.sub(_replace, html)
    return processed, had_foldable


def _transform_content(content_obj) -> None:
    if not hasattr(content_obj, "_content"):
        return
    html = content_obj._content
    processed, had_foldable = _process_html(html)
    if processed != html:
        if had_foldable:
            processed += "\n" + _FOLD_JS
        content_obj._content = processed


# ---------------------------------------------------------------------------
# Pelican signal wiring
# ---------------------------------------------------------------------------


def _on_content_object_init(content_obj) -> None:
    if isinstance(content_obj, (Article, Page)):
        _transform_content(content_obj)


def register():
    signals.content_object_init.connect(_on_content_object_init)
