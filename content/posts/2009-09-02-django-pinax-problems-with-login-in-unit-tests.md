Title: Django/ Pinax: Problems With Login() in Unit Tests
Slug: django-pinax-problems-with-login-in-unit-tests
Date: 2009-09-02 16:01:29
Tags: 
Category: Posts
Author: Tom Clancy

# Django/ Pinax: Problems With Login() in Unit Tests

This is the first in what promise to be a number of "Stupid Django Tricks" where the "stupid" is me and not Django. I was having a good deal of trouble creating unit tests for authenticated views (i.e., pages that require a user to be logged in) for the <a href="http://pinaxproject.com/">Pinax</a> project I've been working on. I dug up two problems, one of which is on Pinax and one that's entirely on me:
<ol>
	<li>Pinax's settings.py file does not provide a setting for <a href="http://docs.djangoproject.com/en/dev/topics/auth/#authentication-backends">AUTHENTICATION_BACKENDS</a>, so the test client's login method doesn't know how to log your user in. Specify "AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)" in your settings file. Actually, I lied. That's the default value for the setting; having gone back and re-run my tests without it specified, everything works, which means the only idiot here is the guy who . . .</li>
	<li>Don't create users by specifying the password directly in the declaration (e.g., user = User(username='Dummy', password='goodluck')). Use the set_password() User method to properly set the password.</li>
</ol>

I've run into a fair number of issues working in Django where Google wasn't helpful. I think 90% of those issues were because no one else was dumb enough to make such an obvious mistake. The other 10% were typos.
