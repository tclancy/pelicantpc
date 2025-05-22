Title: Those Clever Kids: Since You've Been Gone
Slug: since-youve-been-gone
Tags: backbone,javascript,django,apis,mongodb,rest,tastypie,facebook,mooc,webfaction,newrelic
Category: Portfolio
Date: 2014-03-04
Author: Tom Clancy
Url: since-youve-been-gone

# Those Clever Kids: Since You've Been Gone

## 2014-03-04

_What I've been up to since last I posted an entry_

<p>I'm coming to the end of another contract and realizing just how out-of-date this portfolio is. Rather than try to catch up with an endless series of posts, here's a summary of things I've been doing:</p>
<h3>JavaScript</h3>
<ul>
<li>Used Backbone.js in a credit card fraud detection system to allow users to drag and drop one or more suspicious transactions into a sort of shopping cart and then review and act on the transactions.</li>
<li>I'm currently using Backbone.js and D3 to create interactive elements for a MOOC system at an Ivy League graduate school. The objects are written in Coffeescript and styled via SASS. Each interactive is designed to be a reusable element that can be plugged into any course to illustrate the relevant concept.</li>
</ul>
<h3>Responsive Design</h3>
<ul>
<li>Used <a href="https://github.com/gregmuellegger/django-mobile" target="_blank">django-mobile</a> and various thumbnail packages to create responsive sites for clients including <a href="http://smallarmy.net/" target="_blank">Small Army's new site.</a></li>
<li>Integrated Django's <a href="https://github.com/philippWassibauer/templated-emails" target="_blank">templated-emails</a> package with django-notifications to send responsive emails (with a plain text fallback) to clients in a Pinterest-clone site (that also features a responsive design). I created a custom backend for notifications that has been <a href="https://github.com/philippWassibauer/templated-emails/pull/10" target="_blank">integrated into the templated-emails package.</a></li>
</ul>
<h3>APIs and Data</h3>
<ul>
<li>Used django-tastypie to create a REST API on top of the existing site logic to power <a href="http://killscreendaily.com/" target="_blank">Killscreen's new design.</a>&nbsp;I added <a href="https://github.com/dstegelman/django-tastypie-cache" target="_blank">this package</a> for caching tastypie responses and patched it support the DEFAULT_FORMATS setting (<a href="https://github.com/dstegelman/django-tastypie-cache/pull/1" target="_blank">pull request</a>) because it bugs me to always have to add "format=json" to the API URLs when testing :)</li>
<li>Working with django-tastypie along with this <a href="https://github.com/wlanslovenija/django-tastypie-mongoengine" target="_blank">mongoengine add-on</a>&nbsp;in the MOOC site to power student interaction and to track metrics and user state. I'm currently neck-deep in MongoDB learning how to aggregate and filter what promises to be massive amounts of data on each interactive element described above. The project has been a great introduction to MongoDB and where it works well in Django. I've been hesitant about NoSQL up until this and still have my suspicions about developers who see it as a panacea (which is apparently ancient Greek for "not having to worry about the data model at all"), but I can see a number of places on existing projects where it would be an improvement.</li>
<li>Built the site and product for <a href="http://groundenergysupport.com/" target="_blank">Ground Energy</a>. This has been a huge and hugely rewarding job starting in March of 2010 that deserves its own post. Relevant to this section, the product has 5 tables with millions of rows each representing responses from client installations on a minute-by-minute basis. In spite of the size of the data and the growth rate, I've tuned the PostgreSQL back-end and Django to deliver real-time reporting to JavaScript-powered graphs.</li>
<li>Integrated the Ecobee API to make Ecobee thermostats a first-class citizen in <a href="http://groundenergysupport.com/" target="_blank">Ground Energy</a>, allowing owners to track their geothermal efficiency.</li>
<li>A fun "glue" job for <a href="http://www.mycoldfront.com/" target="_blank">Coldfront</a>, integrating with <a href="https://developer.bigcommerce.com/api/" target="_blank">BigCommerce's API</a>&nbsp;on one side to find new orders and then sending the orders to the shipping company by POSTing XML to an endpoint. The shipping company's tech is, as you can surmise, a bit old-school, so checking the order status means polling a mailbox for responses on a regular basis using Python's <a href="http://docs.python.org/2/library/mailbox.html" target="_blank">mailbox</a>&nbsp;and parsing the results.</li>
<li>Various jobs to integrate with Facebook and Twitter's APIs, including a (since deceased) Django-powered Facebook application for Solidworks called <a href="http://files.solidworks.com/Education_Europe/SolidWorks-email-20Jul12_ENG.html" target="_blank">"Professor Cadmore's Challenge".</a></li>
</ul>
<h3>Sites, Deployment and Performance</h3>
<ul>
<li>A series of related beer sites (and don't think I didn't smile typing "startapp beer" in Django's management console) for <a href="http://www.nhdist.com/" target="_blank">NH Distributors</a>, <a href="http://www.bellavancebev.com/" target="_blank">Bellavance Beverage</a> and <a href="http://www.clarkedistributors.com/" target="_blank">Clarke Distributors</a> with <a href="http://microarts.com/" target="_blank">Microarts</a>.</li>
<li>Worked directly with the founders of <a href="http://convenientmd.com/" target="_blank">ConvenientMD</a>&nbsp;to deliver their launch site with a content management system and tools for managing locations and other business information.</li>
<li>Moved <a href="https://www.ctbonline.com/" target="_blank">Community Trust Bank</a>&nbsp;to a three-server-plus-load-balancer setup at Rackspace which meant learning how to modify my typical Fabric deployment script to manage separate web servers and a database server.</li>
<li>Used New Relic on a number of client sites to help identify bottlenecks and areas performance could be improved. New Relic has become an indispensable tool in a such a short time, especially the short time when you get full access for free and are able to step down into slow running queries, look at EXPLAIN statements and figure out how to get huge wins for little investment.</li>
<li>I've become the "Django guy" at my host of choice (<a href="https://www.webfaction.com/" target="_blank">WebFaction</a>). What this has meant in practice is clients with ancient Django sites who have lost touch with their developer (either over time or on purpose in some cases) come to me after they already have a bit of an emergency. WebFaction upgraded a number of servers in 2013 which caused a problem for anyone still running on a pre-1.0 version of Django. Another topic worthy of its own post; for now let's just say I learned a lot about spelunking and how to dig up old versions of Django for local testing.</li>
<li>Started using <a href="http://www.vagrantup.com/" target="_blank">Vagrant boxes</a> to replicate the live environment on a project. I'm not ready to give up my current virtualenv-based Python development process for most projects because it does a good job of replicating the important stuff and because I feel like being able to swap project development from Mac to Windows without a hitch is a decent indicator that I've done a good job of keeping things loosely-coupled, but Vagrant is a good solution for cases when the live environment is important or hard to replicate. I also would like to investigate using Vagrant plus <a href="http://www.ansible.com/home" target="_blank">Ansible</a> (or something similar) to be able to deploy projects directly to AWS and spin up additional resources as needed with a minimum of sysadmin work.</li>
</ul>
