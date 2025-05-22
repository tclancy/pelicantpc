Title: Greener Development
Slug: greener-development
Date: 2013-06-24 15:35:51
Tags: green,environment,webdev
Category: Posts
Author: Tom Clancy

# Greener Development

A local experience designer, [James Christie](https://twitter.com/JC_UX) has been writing about what he calls ["Clean UX"](http://jcux.co.uk/cleanux/cleanux.html): designers and developers starting to make conscious choices about code and design that reduce the carbon footprint of web sites. As developer tools and frameworks get better and easier, the risk of bloat increases. The best example may be the military officer wall of badges that every site provides in hopes you will share their article on Latest Hot Site. Including that teeny little bit of JavaScript that ties them all into the page can have [heavy consequences](http://jcux.co.uk/cleanux/buttons.html): the little bit of code includes a lot more code. Each individual site is mainly concerned with making their buttons look good across platforms and devices, so they have little incentive to keep their code lean. What's the net effect? Christie estimates a million page views (not accounting for caching, admittedly) results in *4 Transatlantic flights' worth of carbon.*

I've been fascinated with the concept and keep bothering him on Twitter with random thoughts. As I've transitioned over the years, becoming less of a front-end developer and more of a back-end dev, I tend to think I've fallen behind on front-end development, but helping new clients with old sites is a regular reminder that as far back as I am from the cutting-edge, I'm still well in the vanguard. So I think I see an opportunity to improve the situation. There are lots of developers who are pure front-end developers, who either don't know or don't feel comfortable with scripting their deployments. Lots of shops are still working with a deployment process that consists of two steps:

1. Make changes locally
2. Upload changes (or the whole site folder)

There's nothing wrong with this and with the proliferation of JavaScript APIs and new devices, "pure" front-end development (defined here as HTML + CSS + JavaScript) is probably experiencing a comeback. Improving deployment for this kind of development would be an easy place to improve the "green-ness" of the development and provide an entry point for additional improvements everyone should make<sup><a href="#foot1">1</a></sup>. In the most basic form, I see this as a simple executable script (with an optional configuration file in the root of the project) that does the following:

* Run [PNGCRUSH](http://en.wikipedia.org/wiki/Pngcrush) or similar over the image files found in or below the root, but don't die if the executable doesn't exist because PNGCRUSH could mess up some images and the user might want to skip it or define which folders to run it on (first reason for a configuration file)
* Compress all JavaScript and CSS files, maybe save them with timestamps in the filenames to make sure the old versions are dumped out of viewers' caches
* Optionally or smartly (imagine a lot of hand-waving here), combine CSS/ JavaScript files into one large file each. I'm torn on doing this globally on a project. I still create multiple CSS/ JS files when they logically belong to sub-sections of a site and it depends on the site whether it's more efficient to join them all into one file or to provide a few grouped files (personally I let [django-compressor](http://django-compressor.readthedocs.org/en/latest/) do the heavy lifting here).
* The last step in the process would be a simple one, but maybe the most valuable: print out a list of all the files changed in the folder since the script last ran. If nothing else, we can encourage users to only upload their changes (while they may also have set their FTP clients to do the same, there's no harm in providing the info).

Given that setup, version two should provide the ability to upload from the script. It's an easy thing to do, it ensures we only upload the altered files and it gives us a wedge to start encouraging better deployment: now that you're using this script to do "smarter" deployments, why not set up an SSH key(s) on the relevant servers so your deployment is easier and more secure? I'm not interested in building something that metastasizes into something that [reads mail](http://en.wikipedia.org/wiki/Jamie_Zawinski#Zawinski.27s_law_of_software_envelopment), but it would be fun to build something that provides hooks for smarter people than me to come up with better ideas here.

<small id="foot1">1. While the Road to Hell may be paved with the best of intentions, I think there's a long way to go before we start making things worse.</small>
