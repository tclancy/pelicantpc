Title: Autocomplete in Python Shell on Windows
Slug: autocomplete-python-shell-windows
Date: 2017-01-20 13:19:35
Tags: python,windows,frustration
Category: Posts
Author: Tom Clancy

# Autocomplete in Python Shell on Windows

Because I drive myself insane replicating this when I find I want autocomplete on Windows, here are the steps (as of January 2017 anyway):

* `pip install pyreadline`
* `pip install ipython[shell]`

Except right now step 2 fails when installing `scandir` so I grabbed it [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scandir), installed the .whl file via pip and then ran that second step.
