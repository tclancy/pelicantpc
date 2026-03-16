"""
Pelican oEmbed Plugin
=====================

This plugin uses Micawber to convert oEmbed URLs in markdown content
to their embedded HTML representations during the publishing process.

It works as a Markdown preprocessor extension, replacing bare oEmbed URLs
in the markdown source with embedded HTML before typogrify or other
post-processing can mangle the URLs.
"""

import re
import warnings
import markdown
from pelican import signals
from micawber import Provider, ProviderRegistry, bootstrap_basic

# Filter BeautifulSoup warnings about URLs
from bs4 import MarkupResemblesLocatorWarning
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

# Create a provider registry with popular oEmbed providers
providers = ProviderRegistry()

# Twitter/X
providers.register(r'https://twitter.com/\S+/status/\d+', Provider('https://publish.twitter.com/oembed'))
providers.register(r'https://x.com/\S+/status/\d+', Provider('https://publish.twitter.com/oembed'))

# YouTube
providers.register(r'https://www\.youtube\.com/watch\?v=\S+', Provider('https://www.youtube.com/oembed'))
providers.register(r'https://youtu\.be/\S+', Provider('https://www.youtube.com/oembed'))

# Vimeo
providers.register(r'https://vimeo\.com/\d+', Provider('https://vimeo.com/api/oembed.json'))
providers.register(r'https://player\.vimeo\.com/video/\d+', Provider('https://vimeo.com/api/oembed.json'))

# Instagram
providers.register(r'https://www\.instagram\.com/p/\S+', Provider('https://api.instagram.com/oembed'))
providers.register(r'https://instagram\.com/p/\S+', Provider('https://api.instagram.com/oembed'))

# SoundCloud
providers.register(r'https://soundcloud\.com/\S+', Provider('https://soundcloud.com/oembed'))

# Spotify
providers.register(r'https://open\.spotify\.com/\S+', Provider('https://embed.spotify.com/oembed'))

# TikTok
providers.register(r'https://www\.tiktok\.com/\S+/video/\d+', Provider('https://www.tiktok.com/oembed'))

# Bare URL on its own line (not inside markdown link syntax)
BARE_URL_RE = re.compile(r'^(https?://\S+)$')


class OEmbedPreprocessor(markdown.preprocessors.Preprocessor):
    """Replace bare oEmbed URLs in markdown source with HTML embeds."""

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = BARE_URL_RE.match(line.strip())
            if match:
                url = match.group(1)
                try:
                    result = providers.request(url, maxwidth=800, maxheight=600)
                    html = result.get('html', '')
                    if html:
                        # Wrap in raw HTML markers so markdown passes it through
                        new_lines.append(html)
                        continue
                except Exception:
                    pass
            new_lines.append(line)
        return new_lines


class OEmbedExtension(markdown.Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(OEmbedPreprocessor(md), 'oembed', 30)


def add_oembed_extension(readers):
    """Register the markdown extension via Pelican's readers_init signal."""
    settings = readers.settings
    extensions = settings.get('MARKDOWN', {}).get('extension_configs', {})
    # We can't easily inject an Extension instance through config, so we
    # monkey-patch the reader's markdown extensions after init.
    for reader in readers.readers.values():
        if hasattr(reader, 'extensions') and isinstance(reader.extensions, list):
            reader.extensions.append(OEmbedExtension())


def pelican_init(pelican_obj):
    """Inject the OEmbed markdown extension into Pelican's markdown config."""
    md_settings = pelican_obj.settings.setdefault('MARKDOWN', {})
    extensions = md_settings.setdefault('extensions', [])
    extensions.append(OEmbedExtension())


def register():
    """Register the plugin's signals with Pelican."""
    signals.initialized.connect(pelican_init)
