Title: New Age Software Services: Website and Bullhorn API Integration
Slug: website-and-bullhorn-api-integration
Tags: csharp,.net,api,integration,jquery
Category: Portfolio
Date: 2009-06-01
Author: Tom Clancy
Url: website-and-bullhorn-api-integration

# New Age Software Services: Website and Bullhorn API Integration

## 2009-06-01

_A new website including integration with Bullhorn, a job search database._

<p><strong>Please note: I am not currently working on Bullhorn projects. Their API has changed since this project was completed in 2009.</strong></p>
<p>thumb:1 New Age Software Services had a content author, web host and a site design, but needed someone to build the new site. The design they had purchased came in two versions, an animated Flash design and a static set of Photoshop files matching the Flash interface. The client wanted the interactivity of the Flash interface but was concerned about the search engine-friendliness of a site in Flash and whether the Flash interface would support future extensions to the site. To provide the best of both options, I built the interface in HTML/ CSS and added animation effects in jQuery to match the Flash interface. The site is built in C# with a single Master Page that controls the look and feel of all pages in the site and the navigation comes from an XML document that describes the hierarchy of the site. Between the two, this makes it very easy to add/ remove/ move pages in the site without having to edit all pages. There are also a number of forms built in C# that use a MVC-type library I wrote for building C# applications back in 2007 (i.e., before Microsoft created a nice new MVC framework for .NET that made it redundant).</p>
<p>thumb:2 This was a two-phase project. Phase One was creating a real web presence. The <a href="http://web.archive.org/web/20070128053558/http://www.newagesoft.com/">previous site</a> was created 10 years prior to generate phone calls. I worked directly with New Age Software's CEO and their content writer to integrate the new copy and branding with a web site template that had been purchased, all in anticipation of a relaunch four weeks later. In addition to creating the site's shell, New Age wanted the site to have a sense of motion. The Flash movie included in the template was both distracting and limiting: it meant content on the page could never grow taller than the movie and the movie itself was a loop of falling puzzle pieces that made the content hard to read. Rather than sacrificing content flexibility or search engine optimization (by replacing the navigation with a movie), I created animated navigation and a scrolling news ticker in JavaScript with jQuery. The news ticker was especially dear to me: it consists of nice, clean HTML and a sprinkling of jQuery, but when I started as a full-time web developer in 2000, one of our most popular offerings was a Java applet-based news ticker that was neither as attractive nor as customizable. To help customers get the information they need, I build a number of forms in C# that allow for the submission of resumes, simple contact emails and subscriptions to a Constant Contact-powered newsletter.</p>
<p>thumb:3  The second phase was the trickier bit, expanding from a single resume submission form to full integration with the <a href="http://www.bullhorn.com/">Bullhorn Software</a> tools that power New Age's business. <a href="https://www.bullhornstaffing.com/BullhornStaffing/API/default.cfm">Bullhorn's API</a>, at least as of this writing, is a series of ColdFusion forms rather than a web service/ RESTful approach. While .NET/ VisualStudio do a great job of providing a foundation for web service integration projects, much of that foundation is lost if you're not talking to web services. I encountered some complications in accepting a file upload, validating the file and passing it on to the 3rd party form in C#. The client's web host takes a serious approach to security. In Phase One, the web server (the IIS worker process) did not have access to write to the drive. Always preferring to be keep fighting with other parties to a minimum, I circumvented this restriction by streaming the file for the simple resume upload. To avoid this issue in Phase Two, I finally submitted the form directly to Bullhorn and intercepted the response.</p>
<p>The <a href="http://supportforums.bullhorn.com/viewforum.php?f=1&amp;sid=9fb56794a89c3f68862825d566567a7b">Bullhorn API forum</a> was a big help, especially the <a href="http://supportforums.bullhorn.com/viewtopic.php?t=488">sample C# code</a>. Because that was such a help, I am providing my <a href="http://snipplr.com/view/9900/c-integration-module-for-bullhorn-staffing-api/">modified version of that code.</a> A few notes on my changes:</p>
<ul>
<li>Giving in to my anal-retentive coding nature, I renamed the class to BullhornWorker to make things obvious</li>
<li>The code was provided as a class, but it's not an object, it's a set of related utilities</li>
<li>As such, any method I actually used has been marked as static because there are no common values to be initialized</li>
<li>I moved the Bullhorn private label id and API key out to Web.config variables to make the code easier to maintain</li>
<li>Added caching for the query that lists all jobs in the system and any filtered job queries: because this is easily the most often call and given the job list does not update more than daily, there's no danger to caching the list and a big performance boost</li>
<li>Added a couple of helper methods to reduce redundancy</li>
<li>The Web.config key DEVELOPMENT_DEBUGGING expects a boolean; if set to "true", the code will return any XML exception information</li>
<li>Web.config keys required: BULLHORN_PRIVATE_LABEL_ID, BULLHORN_API_KEY, CACHE_ON, DEVELOPMENT_DEBUGGING</li>
</ul><img src="images/portfolio/new-age-home.jpg" alt="Home " style="margin: 1em 0" />
<img src="images/portfolio/new-age-job-search.jpg" alt="Job Search Users no longer have to leave the New Age site to get search results from Bullhorn" style="margin: 1em 0" />
<img src="images/portfolio/new-age-contact.jpg" alt="Contact " style="margin: 1em 0" />

