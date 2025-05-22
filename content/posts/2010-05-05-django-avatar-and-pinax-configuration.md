Title: django-avatar and Pinax Configuration
Slug: django-avatar-and-pinax-configuration
Date: 2010-05-05 11:35:04
Tags: 
Category: Posts
Author: Tom Clancy

# django-avatar and Pinax Configuration

Noting this here for the sanity of my future self. When using <a href="http://github.com/ericflo/django-avatar">django-avatar</a> (which is included in Pinax), you need to add at least one of the avatar settings, AVATAR_STORAGE_DIR, to your settings.py file. The important thing to note is this needs to be a relative path to a folder under your MEDIA_ROOT as the path will be used both to create a file system path and to build the urls when serving the avatar images.

For local development, I had trouble getting the avatars (or anything under /media) to appear. The patterns in Pinax's staticfiles.urls include one for everything under /media, but not only didn't I see files under that folder, the server didn't even attempt to serve them. I tried explicitly putting the pattern into my main urls.py at the top of the list, but nothing changed. As a fix, I changed my local MEDIA_URL to '/includes/' and added that pattern to my urls.py, which fixed things. The production server should not be affected since the files won't be served by Django.
