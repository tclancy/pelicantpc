"""Pelican plugin: article ornaments — subheaders and inline footnotes.

Subheader
---------
If an article has a ``subheader`` metadata key, the plugin wraps it in a
rule-ornament div and prepends it to the article content::

    <div class="rule-ornament"><span>❧ SUBHEADER TEXT ❦</span></div>

Inline footnotes
----------------
Transforms ``[ref]...[/ref]`` tags in article content into an inline
superscript reference followed by an inline footnote div.  The footnote div
stays at the position it was written in the document rather than being
collected at the bottom, so CSS can place it in the right-hand gutter at the
same line height as its reference::

    Input:  Here is text[ref]my note[/ref] continuing here.
    Output: Here is text<sup class="footnote-ref" id="fnref-1">1</sup>
            <div class="footnote" id="fn-1">1. my note</div> continuing here.

The counter resets per article/page.  Notes are skipped inside
``<code>`` and ``<pre>`` blocks.

Design note
-----------
Intentionally simpler than ``pelican-simple-footnotes``: no html5lib
dependency, no DOM traversal, no end-of-body list.  That simplicity is the
point — this plugin is for decorative gutter notes, not bibliographic
endnotes.
"""

from __future__ import annotations

import re

from pelican import signals


# Matches [ref]...[/ref] including multi-line note text.
# Deliberately non-greedy so consecutive refs don't merge.
_REF_RE = re.compile(r"\[ref\](.*?)\[/ref\]", re.DOTALL)

# Blocks we do not want to process (raw content).
_SKIP_BLOCK_RE = re.compile(r"<(?:code|pre)[^>]*>.*?</(?:code|pre)>", re.DOTALL)


def _process_content(content):
    """Process a single Pelican content object (article or page)."""
    _inject_subheader(content)
    _process_footnotes(content)


def _inject_subheader(content):
    """Prepend a rule-ornament div when the article has a subheader field."""
    subheader = getattr(content, "subheader", None)
    if not subheader:
        return
    if not content._content:
        return
    ornament = f'<div class="rule-ornament"><span>❧ {subheader} ❦</span></div>\n'
    content._content = ornament + content._content


def _process_footnotes(content):
    """Replace [ref]...[/ref] markers with inline superscript + footnote divs."""
    if not content._content or "[ref]" not in content._content:
        return

    # Build a set of character ranges occupied by code/pre blocks so we can
    # skip refs that appear inside them.
    skip_ranges = [m.span() for m in _SKIP_BLOCK_RE.finditer(content._content)]

    counter = [0]

    def _in_skip_range(start: int) -> bool:
        return any(lo <= start < hi for lo, hi in skip_ranges)

    def _replace_ref(match: re.Match) -> str:
        if _in_skip_range(match.start()):
            return match.group(0)  # leave unchanged
        counter[0] += 1
        n = counter[0]
        note_text = match.group(1).strip()
        return (
            f'<sup class="footnote-ref" id="fnref-{n}">{n}</sup>'
            f'<div class="footnote" id="fn-{n}">{n}. {note_text}</div>'
        )

    content._content = _REF_RE.sub(_replace_ref, content._content)


def register():
    signals.content_object_init.connect(_process_content)
