Title: Debugging a Vue.js Error
Slug: debugging-vuejs-error
Date: 2016-10-11 11:07:14
Tags: django,vue.js
Category: Posts
Author: Tom Clancy

# Debugging a Vue.js Error

I know it's been a while and I really should write more often, but this is just a quick one for Google to index in case it happens to someone else: I recently wrote my first [vue.js](https://vuejs.org/) component and was really pleased with how easy it was to build . . . right up until I deployed it live and it didn't work. It took me about an hour of fiddling with the production version of the site, swapping to the non-minified version, shutting off the CSS and JavaScript compression from `django-compressor` and desperately staring into the (really cool) [Vue debugging panel for Chrome](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?hl=en). I thought it was a problem with the REST API data getting to the component too slowly because Vue kept complaining the rows were missing the properties I was referencing, but looking in the debugging panel I could see Vue was properly loading the data. I finally found the problem by viewing the source of local and live side-by-side which was harder than it sounds because the HTML is minfied in production. I was just about to put the two sets of HTML into a pretty-fier when I saw the difference: [`django-htmlmin`](https://pypi.python.org/pypi/django-htmlmin) doesn't just strip whitespace (I suppose it can't do that), it parses the HTML and apparently makes it "valid" which was moving my Vue templates around to places they shouldn't be. After a quick test and putting the URL in `EXCLUDE_FROM_MINIFYING` in my settings file, all was right with the world.

(Ironically, this post took about 30 minutes to get live because I had to run down another rat hole debugging what turned out to be an out-of-date version of `django-tagging` as I recently upgraded this site. That is another post though. Hopefully.)
