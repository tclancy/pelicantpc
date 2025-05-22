Title: Django Profiling Bug
Slug: django-profiling-bug
Date: 2014-04-18 14:00:51
Tags: django,python,profiling
Category: Posts
Author: Tom Clancy

# Django Profiling Bug

I'm doing some work profiling a large Django application and I was running into this weird error when I tried to aggregate the stats with gather_profile_stats.py which comes with Django. It kept throwing `TypeError: zip argument #1 must support iteration` if there were two profile files for the same bit of code. Searching for matching results was a ghost town and I was starting to think no one actually used gather_profile_stats.py because it was broken. Turns out there's a [regression bug](http://bugs.python.org/issue7372) in early versions of Python 2.7. I applied the patch provided in the link and everything works. Posting this little note so it's not such a ghost town for the next person.
