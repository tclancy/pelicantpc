Title: Frontline/ PBS: Frontline: God in America
Slug: frontline-god-america
Tags: django,social,pinax,geodata,oauth
Category: Portfolio
Date: 2010-10-01
Author: Tom Clancy
Url: frontline-god-america

# Frontline/ PBS: Frontline: God in America

## 2010-10-01

_A social website for viewers of the Frontline program "God in America" to come together and discuss their religious views._

<p><em>God in America</em> is a 2010 episode of PBS' Frontline. As part of the reporting for the show, Frontline wanted a social networking site to invite Americans to discuss their opinions on religion and how they practice their faiths. I built a site based on Pinax, a collection of Django applications that work together as a foundation for social networks. User management for the site is handled by PBS' OAuth service which provides a Django library for plugging into projects. This means members of existing Frontline/ PBS sites don't have to bother with signing up before they can use the site.</p>
<p>The focus of the site is user profiles. The profiles consist of standard user information plus responses to a series of "prompts", questions about their faith. Users can respond in text, with links to photographs or links to video responses. The site provides checks to allow administrators to review responses for questionable content. Text is reviewed for signs of spam and photographs and videos are approved by administrators. Video responses are sent through django-oembed, an application that turns links into videos on the page, so users can simply paste in a link to a Youtube (or similar video site) page and have it display as an embedded movie with no further action.</p>
<p>Users can indicate they like other responses or flag responses as offensive. Both types of flags are throttled so users cannot game the system to help or hurt other users' responses (or affect their own). You can search all responses with a fuzzy text search via Haystack and Whoosh or filter responses by specific prompts. The site also allows members to create public or private events and other users can RSVP to indicate if they are attending. Events include the local zip code so users can search for events within a certain distance of their location through a zip code database and longitude/ latitude radius search.</p><img src="images/portfolio/Faithbook_Home_1.png" alt="Homepage " style="margin: 1em 0" />
<img src="images/portfolio/Faithbook_Profile_1.png" alt="Your Profile Editing your information and responses" style="margin: 1em 0" />
<img src="images/portfolio/Faithbook_Browse_1.png" alt="Browse Browse user profiles by name, date, number of views or celebrities only" style="margin: 1em 0" />

