Title: On Optimization
Slug: on-optimization
Date: 2010-02-25 14:50:12
Tags: 
Category: Posts
Author: Tom Clancy

# On Optimization

It's strange what you can get used to: the current social network site I'm working on has a page with 216 database queries on it. Used to be I'd get the hives if I hit a dozen queries on a page.

<strong>"216! Did you know databases let you bring back more than one row at a time nowadays?"</strong>

Yes. The project is in Django (and built on top of <a href="http://pinaxproject.com/" target="_blank">Pinax</a>), so it's the ORM making all those queries, not me. It's one of those social network site pages that aggregates activity from everyone you follow. It also shows details about them, how far they are away from you and any comments on the item, so there's only so small I can make it while coloring inside the lines of the mapping system. I've already fallen back to raw SQL for one of the elements (there are a couple of places, and sure to be more in the future, where we return a list of the database ids of all your friends so we can use them as part of " AND id in (x, y, z)" queries. Doing that through Django resulted in one query to the database for every friend you have. Given this was causing a slowdown when I'm the only user of the site and I only have 3 friends (one is another tester and the other two are dogs I know, so it's kind of a <a href="http://www.drivebytruckers.com/lyrics_btcd.html#bob" target="_blank">"Bob"</a> situation (specifically the dog part and not the rest)), I had a suspicion that wasn't going to scale. Modified that, added some caching, got smarter about some lookups (I thought I'd only hit the db once no matter how many times I referred to a model's property in a function) and things are back to running smoothly.

<strong>"216!"</strong>

Hey, it was 1066 when I started a day ago. Or something close to that. I've got 1066 on the brain because I've been thinking about William of Orange and before you say--

<strong>"Write code for a job and think about William of Orange in your spare time. You must be a hit with the ladies."</strong>

--that, let me point out it was in reference to a <a href="http://www.urbandictionary.com/define.php?term=dutch%20oven" target="_blank">Dutch Oven</a> joke. That has to count for something.

<strong>"Undoubtedly. Perhaps 'lady killer' is more literal than figurative in your case."</strong>

Regardless, given the nature of the screen, aggregating a dozen types of activities from an arbitrary number of users, I don't think the current solution is the long-term answer, so I buttoned it up as best I could.

<strong>"As best you could? Implement the long-term solution now."</strong>

That would be solving a problem I don't have (c.f., "<a href="http://www.acm.org/ubiquity/views/v7i24_fallacy.html" target="_blank">premature optimization</a>", "<a title="You Ain't Gonna Need It" href="http://en.wikipedia.org/wiki/You_ain't_gonna_need_it" target="_blank">YAGNI</a>"). Given the data for this screen is derived from other objects in the system anyway, I think the long-term solution is to move this data into a nosql store (here's an <a href="http://www.eflorenzano.com/blog/post/using-couchdb-django/" target="_blank">example of using CouchDB in Django</a> now and future updates to Django should improve support for this kind of thing). It's important to remember traffic issues fall under the title Good Problems to Have. While I'd love to spend a couple of days implementing this rightnowyespleasecani, if the overall project never takes off, it would be unfair to ask the client to pay for something they didn't ask for and never needed.

<strong>"216!"</strong>

I'm already obsessing over it on my own. Why do you think you're here?
