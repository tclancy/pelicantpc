Title: Django, Haystack & Elastic Search
Slug: django-haystack-elastic-search
Date: 2013-03-28 18:24:01
Tags: 
Category: Posts
Author: Tom Clancy

# Django, Haystack & Elastic Search

<p>(Yes, I know it's been a while.)</p>

<p>Just a quick note in case this bites someone else. I'd file a bug with Haystack, but I have a feeling I'm doing something incredibly dumb. I have a convoluted set of filters for a search running through Django's fantastic Haystack search abstraction using Elasticsearch as a back-end. All was going fine until I tried to add a filter to include/ exclude results which had a blank value in their video_id field. In the browser it just looked like an empty search result, but the console was filled with <code>ParseException[Cannot parse \'((my search string) AND NOT (video_id:))</code>. I'm sure there's a proper fix for this, but I just adjusted my search index to change the CharField to a BooleanField using the field on the model.</p>
