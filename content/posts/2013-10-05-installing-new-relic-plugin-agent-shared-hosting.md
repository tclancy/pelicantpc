Title: Installing New Relic Plugin Agent on Shared Hosting
Slug: installing-new-relic-plugin-agent-shared-hosting
Date: 2013-10-05 10:57:13
Tags: newrelic
Category: Posts
Author: Tom Clancy

# Installing New Relic Plugin Agent on Shared Hosting

New Relic's basic agent (and the free 30 days of Pro we got up front) have been a huge help on one of my largest ongoing projects. Wanting more insight into our server after a mystery incident yesterday morning, I've started adding plugins. I started with a plugin for Postgres (because that seemed to be the source of our mystery); I had to use [this one](https://rpm.newrelic.com/accounts/230318/plugins/directory/30) because we're on a shared host with WebFaction. It all went fine after I figured out how to get Ruby's bundle/ bundler installed in a local account and then I even daemonized it with a [simple script](https://gist.github.com/tclancy/6841979). That gave me a bunch of statistics on our two databases and a number of pretty graphs. I have no idea what any of it means yet, but I'll take the info and figure out what it means (and maybe finish reading *[PostgreSQL 9.0 High Performance](http://www.amazon.com/PostgreSQL-9-0-High-Performance-ebook/dp/B0057G9RUG/ref=tmm_kin_swatch_0?_encoding=UTF8&sr=8-2&qid=1380985344)*). Plus the plugin provides alerts via New Relic so that's a handy bit of insight by itself.

Happy with that plugin, I'm now in the process of installing [a suite of plugins for New Relic](https://github.com/MeetMe/newrelic-plugin-agent). Happily those are provided in Python. Even better, it's all install-able via pip. On the downside, you hate to see a bug report like this on the front page:

>Version 1.0.12 has a SERIOUS uninstallation bug in the file manifest that **will remove all the files on your filesystem** if you try and do a pip remove newrelic_plugin_agent.

So there's that. In addition, the package assumes you own the box. Because I do not, I need to be a bit smarter and give them a hand. In my .bash_profile I have the following: `export PIP_PATH=/home/groundenergy/lib/python2.7`. This is where I want things to be installed rather than the default Python path. *In theory* that should be enough to pass in to allow `pip install newrelic-plugin-agent --install-option="--prefix=$PIP_PATH"` to work. Except this package [assumes you're either installing into a virtualenv or want to install into /opt](https://github.com/MeetMe/newrelic-plugin-agent/blob/master/setup.py#L56). I'm not doing either. I tend to be a bit lazy about virtualenvs on production servers, which I am starting to question, but that's not really relevant here. In order to get around the problem, I did the following before installing: `export VIRTUAL_ENV=/path/i/really/want`.

That's where I am right now but I figured the post might help someone and it gives me a place to add further notes.
