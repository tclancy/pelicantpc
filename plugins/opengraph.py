"""Pelican plugin: OpenGraph and Twitter Card meta tags.

Attaches an ``opengraph`` dict to each content object (article or page)
during ``content_object_init``.  A shared template partial
(``_opengraph.html``) reads this dict and renders the ``<meta>`` tags.

Supported front-matter overrides (all optional)::

    og_image: https://example.com/hero.jpg
    og_description: Custom social-sharing blurb
    og_title: Custom social title
    og_type: website

Fallback chain:
    og:title       ← og_title → article.title
    og:description ← og_description → description → truncated summary
    og:image       ← og_image → first <img> in content → OG_DEFAULT_IMAGE
    og:type        ← og_type → "article" (if dated) / "website" (pages)

Site-level settings (pelicanconf.py)::

    OG_DEFAULT_IMAGE = "/images/default-og.jpg"   # fallback image
    OG_TWITTER_USERNAME = "@handle"                # twitter:site
"""

from __future__ import annotations

import html
import re

from pelican import signals

_IMG_SRC_RE = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
_TAG_RE = re.compile(r"<[^>]+>")


_MULTI_WS_RE = re.compile(r"\s+")


def _strip_tags(text: str) -> str:
    """Remove HTML tags, unescape entities, and collapse whitespace."""
    cleaned = html.unescape(_TAG_RE.sub(" ", text or ""))
    return _MULTI_WS_RE.sub(" ", cleaned).strip()


def _truncate(text: str, max_length: int = 200) -> str:
    """Truncate to *max_length* chars, breaking at a word boundary."""
    if not text or len(text) <= max_length:
        return text or ""
    truncated = text[:max_length].rsplit(" ", 1)[0]
    return truncated.rstrip(".,;:!? ") + "…"


def _make_absolute(url: str | None, siteurl: str) -> str | None:
    """Ensure *url* is absolute, prepending *siteurl* if needed."""
    if not url:
        return None
    if url.startswith(("http://", "https://", "//")):
        return url
    return f"{siteurl.rstrip('/')}/{url.lstrip('/')}"


def _first_image_src(content_html: str) -> str | None:
    """Return the ``src`` of the first ``<img>`` tag, or *None*."""
    m = _IMG_SRC_RE.search(content_html or "")
    return m.group(1) if m else None


def _resolve_description(content) -> str:
    """Build a plain-text description from the best available source."""
    desc = getattr(content, "og_description", None)
    if desc:
        return desc

    desc = getattr(content, "description", None)
    if desc:
        return _strip_tags(desc)

    summary = getattr(content, "_summary", None)
    if summary:
        return _truncate(_strip_tags(summary))

    raw = getattr(content, "_content", None)
    if raw:
        return _truncate(_strip_tags(raw))

    return ""


def _resolve_image(content, siteurl: str) -> str | None:
    """Pick the best image: front-matter → first in-content → site default."""
    og_image = getattr(content, "og_image", None)
    if og_image:
        return _make_absolute(og_image, siteurl)

    first = _first_image_src(getattr(content, "_content", ""))
    if first:
        return _make_absolute(first, siteurl)

    default = content.settings.get("OG_DEFAULT_IMAGE")
    if default:
        return _make_absolute(default, siteurl)

    return None


def process_content(content):
    """Attach an ``opengraph`` dict to *content*."""
    settings = content.settings
    siteurl = settings.get("SITEURL", "")
    sitename = settings.get("SITENAME", "")

    raw_title = getattr(content, "og_title", None) or getattr(content, "title", "")
    og_title = _strip_tags(raw_title)
    og_type = getattr(content, "og_type", None)
    if not og_type:
        og_type = "article" if hasattr(content, "date") else "website"

    og_description = _resolve_description(content)
    og_image = _resolve_image(content, siteurl)
    og_url = _make_absolute(getattr(content, "url", ""), siteurl)

    og = {
        "title": og_title,
        "type": og_type,
        "url": og_url,
        "description": og_description,
        "image": og_image,
        "site_name": sitename,
    }

    if og_type == "article" and hasattr(content, "date"):
        og["article_published_time"] = content.date.isoformat()
        modified = getattr(content, "modified", None)
        if modified:
            og["article_modified_time"] = modified.isoformat()
        author = getattr(content, "author", None)
        if author:
            og["article_author"] = str(author)
        tags = getattr(content, "tags", None)
        if tags:
            og["article_tags"] = [str(t) for t in tags]

    og["twitter_card"] = "summary_large_image" if og_image else "summary"
    twitter_user = settings.get("OG_TWITTER_USERNAME")
    if twitter_user:
        og["twitter_site"] = twitter_user

    content.opengraph = og


def register():
    signals.content_object_init.connect(process_content)
