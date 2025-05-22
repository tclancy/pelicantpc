Title: Upgrading Django
Slug: upgrading-django
Date: 2016-10-14 10:13:09
Tags: django
Category: Posts
Author: Tom Clancy

# Upgrading Django

For the second time in a few years I've found myself doing a number of Django upgrades. It's a good thing: I'm happy the framework I chose to base most of my work on when I went solo has stayed relevant. But this time I wanted to document some of the pain points to make things easier on anyone else going through the same.

First off, this round of updates has been a lot easier than the first: back then I was the point of contact for [WebFaction](https://www.webfaction.com/) clients who had a Django app but no longer had a developer and those orphaned projects trended *ancient*. I started working with Django in 2009 with [Django 1.1](https://www.djangoproject.com/weblog/2009/jul/29/1-point-1/) and that was modern compared to most of the WebFaction projects. The biggest challenge in that group was a project running on 0.96 and using `psycopg`. I'd been installing `psycopg2` for so long at that point it never occurred to me there was a version before it. And the Internet felt the same way: obtaining a version of Django that old was a challenge (see [this thread](http://stackoverflow.com/questions/19179881/how-do-i-get-an-older-version-of-django-pip-says-could-not-find-version) for how to get versions no longer listed in Pypi). Obtaining a copy of `psycopg` proved impossible (I cheated and wound up downloading the folder from the client's `site-packages` directory and using that to replicate the issue they were seeing-- definitely not a recommended approach).

## General Guidelines

* Use a [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/) or similar concept. If you're already doing so, great. If you are not, now is definitely the time to start. If you're doing anything more than a minor upgrade/ working on a project with no 3rd party libraries, you are going to run into some "dependency hell" where you've updated to Django 1.NEW and updated all your code to be compatible and then find out some libraries you use aren't compatible. The best case scenario is where you just need to update the libraries to their latest versions too, but you may have to play around with the versions to make it all work. Otherwise you need to figure out how to replace the library or [fork it](https://bitbucket.org/tclancy/django_openid_provider).
* Implicit in my `virtualenv` suggestion is that you also use `pip` to install packages and `pip freeze` to create a requirements file *with the exact versions* of the libraries your project uses. 
* If you are updating from a truly old version of Django, try not to get too hung up on updating to the latest and greatest. You might have to shoot for something a little bit older because the incompatibilities are just too great or there isn't enough time right now to make it all work. In updating my old site from 1.2 to 1.10 I actually stopped at 1.6 for a while instead. This is another place `virtualenv` is your friend: at one point I had three local environments for my site, `tkc` (live), `tkc16` and `tkc110`. Once I finished the upgrade process, I deleted the first two and renamed `tkc110` to `tkc` and it was like nothing ever happened. Be aware of the [long-term release versions and the deprecation schedule](https://www.djangoproject.com/download/#supported-versions) when targeting a new version.
* If you are jumping from a really old version, do some reading on the release notes to see what new features are available to you. I'm focusing on problems you may run into and backwards-incompatible changes, but one of the major reasons to upgrade are all the improvements you get. Be aware of things like [`select_related`, `prefetch_related` and `only`](https://docs.djangoproject.com/en/1.10/ref/models/querysets/#select-related) for making queries faster.
* Change from [`render_to_response`](https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#render-to-response) to [`render`](https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.render). It will make things easier and the former is soon to be removed.
* If you get stuck because the changes to project layout or syntax have changed so much, try creating a new `virtualenv` and project with 1.10 (or similar) and then dragging your apps into the project. You will still need to update a bunch of stuff but it may make things a lot easier and help with your future-proofing.

## Version-Specific Notes

### [1.10](https://docs.djangoproject.com/en/1.10/releases/1.10/)

* [Major changes to middleware](https://docs.djangoproject.com/en/1.10/releases/1.10/#new-style-middleware)
* If you are using MySQL (don't start now), [Django recommends](https://code.djangoproject.com/ticket/15940) you turn on strict mode. See [project note](https://github.com/django/django/commit/b2aab09fe99b0e6e2e0357a7a794355a631c3039) about why and [this answer for how](http://stackoverflow.com/a/23023015/7376)
* `django.conf.urls.patterns` is gone and all view references in `urls.py` need to be imported views, not string names.

### [1.9](https://docs.djangoproject.com/en/1.10/releases/1.9/)

* The admin got a facelift!
* [Password validation options](https://docs.djangoproject.com/en/1.10/releases/1.9/#password-validation)
* `django.contrib.sites` is no longer included by default, which can cause a `RuntimeError: Model class django.contrib.sites.models.Site doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS`. Just add it back to `INSTALLED_APPS`.
* `django.utils.log.NullHandler` was removed, [replace the references with logging.NullHandler](http://stackoverflow.com/questions/34348360/cannot-resolve-django-utils-log-nullhandler-in-django-1-9)

### [1.8](https://docs.djangoproject.com/en/1.10/releases/1.8/)

* Major settings change: [the new `TEMPLATES` setting replaces all `TEMPLATE_*` settings](https://docs.djangoproject.com/en/1.10/ref/templates/upgrading/#the-templates-settings). This is a bit of PITA as you have to move a bunch of things into their new home in that setting.
* `select_related` actually checks that the fields exist on the model you are querying. Previously this just silently ignored the error and you were left thinking you'd improved performance when you weren't doing anything.
* `django.contrib.formtools` is replaced by an [external app](https://github.com/django/django-formtools/)
* The syntax of `urls.py` files changed: you now have to have `url(regex, view)` instead of just `(regex, view)`, otherwise you will get `AttributeError 'tuple' object has no attribute 'regex'`. Make note of the changes in 1.10 to `urls.py` files if you're going to be updating all of them anyway.
* [`request.REQUEST` was removed](https://code.djangoproject.com/ticket/18659), but you weren't using that anyway, were you?
* Drops support for Postgres < 9.0 (and then 9.0 and 9.1 are dropped in .9 and .10) and MySQL < 5.5

### [1.7](https://docs.djangoproject.com/en/1.10/releases/1.7/)

* Major update which makes [database migrations](https://docs.djangoproject.com/en/1.10/topics/migrations/) a built-in part of Django instead of relying on 3rd party apps (usually South). See the [differences here](https://realpython.com/blog/python/django-migrations-a-primer/).
* [App loading changes](https://docs.djangoproject.com/en/1.10/releases/1.7/#app-loading-changes) may mean needing to reorder or [move some stuff.](http://stackoverflow.com/questions/34114427/django-upgrading-to-1-9-error-appregistrynotready-apps-arent-loaded-yet)
* If you are using South, there's a [guide to changing over](https://docs.djangoproject.com/en/1.7/topics/migrations/#upgrading-from-south). One thing that's not obvious: in addition to removing `'south'` from your `INSTALLED_APPS`, you actually need to uninstall it from your `virtualenv` or you will get errors like [`There is no South database module 'south.db.postgresql_psycopg2' for your database.`](http://stackoverflow.com/questions/29647602/there-is-no-south-database-module-south-db-postgresql-psycopg2-for-your-databa)
* [Default middleware changed](https://docs.djangoproject.com/en/1.10/releases/1.7/#contrib-middleware-removed-from-default-middleware-classes)
* The syntax/ imports of the `.wsgi` file project use changed. You may run into `AppRegistryNotReady: Apps aren't loaded yet`. See this [StackOverfloew thread](http://stackoverflow.com/questions/26276397/django-1-7-upgrade-error-appregistrynotready-apps-arent-loaded-yet).
* `RuntimeError: populate() isn't reentrant` - there are a [number of possible causes for this](http://stackoverflow.com/questions/27093746/django-stops-working-with-runtimeerror-populate-isnt-reentrant) (and I'm not sure if there are all 1.7-specific). In my case it was a dumb error where I had an app listed twice in `INSTALLED_APPS`.

### [1.6](https://docs.djangoproject.com/en/1.10/releases/1.6/)

* Not much new, simplified setup, swapped a couple of defaults in settings. At least that's how I remember it and its why I chose this as a halfway step in my own update.
* Actually there's one change that will bite you if you have any custom managers: `get_query_set` is now `get_queryset`.
* `django.contrib.localflavor` is gone, replaced by a [3rd-party app](https://django-localflavor.readthedocs.io/en/latest/). Update your requirments file and your references.
* `django.contrib.markup` is gone. You will need a [replacement.](https://github.com/trentm/django-markdown-deux)
* There no longer is a `.raw_post_data` attribute on Request objects. Use `.body` instead.


### [1.5](https://docs.djangoproject.com/en/1.10/releases/1.5/)

* Introduces a [configurable `User` model](https://docs.djangoproject.com/en/1.10/releases/1.5/#configurable-user-model). A user in the [reddit discussion](https://www.reddit.com/r/django/comments/57gu0e/django_version_upgrade_guide/) of this post said it caused them [problems due to a subclassed `User` model in their project.](https://www.reddit.com/r/django/comments/57gu0e/django_version_upgrade_guide/d8t30o3)
* The syntax of the [`url`](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#url) tag changed and now the url name has to be quoted. If you use an editor that supports multi-file search-and-replace, you can [update all your templates](http://jpadilla.com/post/47025152553/shifting-to-new-style-url-tag-in-django-15) easily. Pro-tip: do this in its own branch or similar for safety's sake.
* Introduces the [`ALLOWED_HOSTS` setting](https://docs.djangoproject.com/en/1.10/ref/settings/#allowed-hosts). **Make sure to do this** because it will bite you: the setting only applies if `DEBUG = False`, so you won't run into errors locally but then your brand-new, updated site will not respond when you post it live.
* Deprecates `django.utils.simplejson`. Can do a search and replace to `import json` instead. Unrelated to any upgrade stuff, if you do a lot of JSON processing or a little bit of JSON processing on very big pieces of JSON, take a look at [`ujson`](http://artem.krylysov.com/blog/2015/09/29/benchmark-python-json-libraries/). I've gotten a lot of free performance improvements from it.
* `direct_to_template` is gone. Use [this solution in its place](http://stackoverflow.com/questions/15621048/how-can-i-satisfy-an-import-of-direct-to-template)

### [1.4](https://docs.djangoproject.com/en/1.10/releases/1.4/)

* Lots of good new stuff introduced in this version, the biggest being [timezone support](https://docs.djangoproject.com/en/1.10/topics/i18n/timezones/).
* The concept of `ADMIN_MEDIA` is replaced by static files app from 1.3
* [`django.conf.urls.defaults` is replaced by `django.conf.urls`](https://docs.djangoproject.com/en/1.10/releases/1.4/#django-conf-urls-defaults). Update your `urls.py` files accordingly.
* Error: `"No modules named six"` - this is an annoying one I ran into with a couple 3rd party libraries. I was testing which versions I could easily update to by updating to 1.2.0, 1.3.0, 1.4.0, etc. The problem is `six` was introduced in Django 1.4.2 so don't update to anything less than that if you're going to use 1.4.

### [1.3](https://docs.djangoproject.com/en/1.10/releases/1.3/)

* The big thing here is the introduction of `staticfiles`. If you've never dealt with that, it's a sea change and you will need to [read the documentation](https://docs.djangoproject.com/en/1.10/howto/static-files/) about how to change things. Essentially, this was splitting up the idea of media (user-generated uploads) from your site's static assets.
* [Class-based views](https://docs.djangoproject.com/en/1.10/topics/class-based-views/) are also added here. You're not obligated to use them but if you rely on a lot of generic views, you're going to need to update those.
* CSRF protection now applies to Ajax views as well.
