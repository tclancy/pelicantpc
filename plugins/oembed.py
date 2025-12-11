"""
Pelican oEmbed Plugin
=====================

This plugin uses Micawber to convert oEmbed URLs in markdown content
to their embedded HTML representations during the publishing process.
"""

import warnings
from pelican import signals
from micawber import Provider, ProviderRegistry, parse_html

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


def process_content(content):
    """
    Process content to replace oEmbed URLs with embedded content.
    This is called when a content object (article or page) is initialized.
    """
    if hasattr(content, '_content') and content._content:
        try:
            # Process the HTML content after markdown conversion
            processed = parse_html(
                content._content,
                providers,
                urlize_all=False,  # Don't convert all URLs, only oEmbed ones
                maxwidth=800,      # Max width for embeds
                maxheight=600      # Max height for embeds
            )
            if processed:
                content._content = processed
        except Exception as e:
            # If there's an error, keep the original content
            # You can uncomment the next line for debugging
            # print(f"oEmbed processing error: {e}")
            pass




def register():
    """
    Register the plugin's signals with Pelican.
    """
    # Process content after it's been initialized
    signals.content_object_init.connect(process_content)