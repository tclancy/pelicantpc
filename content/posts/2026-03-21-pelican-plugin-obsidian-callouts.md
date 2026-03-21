Title: New Pelican Plugin: Obsidian-Style Callouts
Slug: pelican-obsidian-callouts
Date: 2026-03-21
Tags: blogging,vibecoding,pelican,python,obsidian
Category: Posts
Author: Tom Clancy

# New Pelican Plugin: Obsidian-Style Callouts

> [!caution] Vibe-Coded Slop
> It should be noted, per the anti-clanker movement, there was little to no thought
> involved in this process. I had learned to use [Obsidian callouts](https://obsidian.md/help/callouts),
> found I liked them and wanted to use them here.

I write all my notes and drafts in [Obsidian](https://obsidian.md/) these days
and one of the things I like about it is the callout syntax, which lets you drop
little admonition boxes into your notes with `> [!note]` or `> [!warning]` or
whatever. They're genuinely useful for flagging things I want to remember without
burying them in prose. The problem is Pelican doesn't know what to do with them;
they just render as regular blockquotes and you lose the whole point.

So I built [pelican-obsidian-callouts](https://github.com/tclancy/pelican-obsidian-callouts),
a plugin that converts the Obsidian callout syntax into proper styled HTML with
icons and everything. It supports all 14 of the standard Obsidian callout types
(note, tip, warning, danger, etc.) plus foldable variants where you can collapse
content with a `+` or `-` after the type. Custom titles work too. Basically if
you write callouts in Obsidian and publish with Pelican, this does what you'd
expect without you having to think about it, which is all I really wanted.

The interesting part of how it happened: I started with a local plugin jammed
directly into this site's codebase because that's the fastest way to see if an
idea is even worth pursuing. Claude and I iterated on it over maybe a week —
got the regex parsing working, styled the CSS for all 15 types (there are 14
distinct ones plus `quote` which aliases to `cite`), added the foldable
`<details>`/`<summary>` behavior, and debugged custom title rendering. Once it
actually worked, I opened [an issue](https://github.com/tclancy/pelicantpc/issues/6)
to extract it into a proper standalone package because leaving it inline felt
like the kind of thing that would rot quietly and then bite me six months later
when I inevitably forgot how it worked.

The extraction itself was the kind of task that vibe coding handles well: it's
not creative work, it's moving code from point A to point B while adding the
boilerplate a proper Python package needs (pyproject.toml, test suite, CI, the
whole song and dance). The actual plugin is a post-processor — it runs on the
rendered HTML rather than intercepting the Markdown pipeline, which means it
doesn't care what Markdown parser you're using. That was a deliberate choice
because I didn't want to be fighting with whatever extension system the parser
du jour has going on. Find blockquotes that match the pattern, replace them
with semantic divs, inject one small script per page for the fold toggles, done.

The icons come from [Lucide](https://lucide.dev/) via their static CDN, so there's
no JavaScript framework dependency for what amounts to a few SVGs. Each callout
type gets its own icon and accent color through CSS classes like
`.pelican-callout-warning`, which means you can restyle them however you want
without touching the plugin. Unknown callout types degrade gracefully back to
regular blockquotes, which is the right thing to do because I don't want my
publishing pipeline to explode because I typo'd `> [!nope]` in a draft at
midnight.

> [!info] Oh one other thing
> I didn't write this post either. For giggles, I fed Claude a bunch of my
> writing and extracted a voice skill for screwing around with.

It's [on GitHub](https://github.com/tclancy/pelican-obsidian-callouts) if you
want it. Uses `uv` for dependency management because I'm not an animal. Not on
PyPI yet because I wanted to live with it a bit longer before inflicting it on
anyone who might `pip install` it without reading the source first, but that's
probably coming once I'm confident I haven't missed something embarrassing.
