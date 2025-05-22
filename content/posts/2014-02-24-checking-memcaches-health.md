Title: Checking on memcache's health
Slug: checking-memcaches-health
Date: 2014-02-24 13:21:53
Tags: django,memcache,webfaction
Category: Posts
Author: Tom Clancy

# Checking on memcache's health

From time to time a client on WebFaction will experience a hiccup in their memcache process. It's not obvious at first unless the site is under heavy load (New Relic is a huge help in diagnosing the problem); this post is just a central dumping ground for links related to fixing the issue.

 * [Setting up memcache to a sock file](https://docs.webfaction.com/software/memcached.html)
 * [Figuring out how much memory you have available](https://community.webfaction.com/questions/8553/how-to-determine-memory-consumption)
 * [Webfaction script to check memory use by process](https://community.webfaction.com/questions/2749/script-to-view-memory-usage-and-running-proccess)
 * [Checking if memcache is running on a port](http://stackoverflow.com/questions/1690882/how-do-i-see-if-memcached-is-already-running-on-my-chosen-port)
 * [Checking whether Django is actually using the cache](http://stackoverflow.com/a/6989742/7376)

