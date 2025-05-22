Title: Django Command to Back Up to Amazon S3 with Python
Slug: django-command-back-amazon-s3-python
Date: 2013-06-29 17:00:13
Tags: code,boto,python
Category: Posts
Author: Tom Clancy

# Django Command to Back Up to Amazon S3 with Python

If it's of use to anyone, I wrote this [fairly thick-headed script](https://gist.github.com/5892498) to look for the most recent versions of files matching one or more patterns in a directory, zip them up and back them up to Amazon's S3 Service using [boto](http://boto.readthedocs.org/en/latest/). It also deletes *all* files in the directory that are older than a given number of days (unless the file is being backed up in the current run). Even includes a bit of progress feedback, though nothing fancy.

The script is designed to be a Django management command because I'm lazy and like to keep all site-related files under Django, but there's not much coupling: just define your keys and patterns in the file, get rid of the Django "class Command" stuff and turn it into a normal script if you like (you'll have to find a new way to send email notifications on error if you do). 

It ain't pretty and the parameter handling is crap, but it's a start.

<script src="https://gist.github.com/tclancy/5892498.js"></script>
