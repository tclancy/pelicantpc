Title: Crew Log: Social Media Site for Boat Crews
Slug: social-media-site-boat-crews
Tags: django,social,pinax,geodata,googlemaps,geolocation
Category: Portfolio
Date: 2010-04-01
Author: Tom Clancy
Url: social-media-site-boat-crews

# Crew Log: Social Media Site for Boat Crews

## 2010-04-01

_Worked with Slim Kiwi to create a social media site for boat crews to track their friends on crews across the world._

<p>In July 2009, I began working with Slim Kiwi on an exciting social media project. Usually when I see an RFP along the lines of "It's Facebook, but for [niche market]", I'm suspicious, wondering why Facebook can't be Facebook for that market. But this project was different. It was immediately clear why boat crews could use their own site. Facebook doesn't expose a lot of geographic data and understandably so: most people wouldn't care and Facebook has enough privacy problems without exposing where users live.</p>
<p>Rather than start from scratch, we built the project on top of <a href="http://pinaxproject.com/">Pinax</a> to get the basics out of the way. That left us able to concentrate on the custom parts of this project: where you are, where your friends are and what they've been doing. The showpiece of the site is your logbook: it's a customized Google Map that allows users to log their current location by dropping a marker on the map (or searching for a location name). The marker can then be dragged to fine-tune the location and users provide a name and time associated with the location. Points can be organized into trips so users can filter their logbook down to just a given span of time. Each trip also creates an associated photo album so users can associate photos with their trips. Each photo uploaded automatically creates thumbnails for the front page of the trip's photo album and thumbnails for various icons throughout the site. Photos are managed through a drag and drop interface allowing users to sort, add and delete photos easily.</p>
<p>The other major component of the site is the Activity Log. Everything you do on the site (add a location, a trip, a photo, update your profile, etc) creates an activity entry. Going to your activity log shows you what you've been up to and what your friends have been doing (assuming their privacy permissions and relationship with you allow it) in chronological order with information about their current location. Activity can be filtered by contact type and by location so you can find friends who are active around you. Designing the activity log and performance tuning it once we had enough test data proved to be an interesting challenge; the experience left a few scars but it also earned me a quick reputation boost at Stack Overflow when I <a href="http://stackoverflow.com/questions/2835075/php-news-feed-database-design/2875875#2875875">shared my knowledge there.</a></p>
