Title: Piscataqua Bank: Piscataqua Savings Bank Website
Slug: piscataqua-savings-bank-website
Tags: banks,csharp,dotnet,sqlserver
Category: Portfolio
Date: 2008-08-05
Author: Tom Clancy
Url: piscataqua-savings-bank-website

# Piscataqua Bank: Piscataqua Savings Bank Website

## 2008-08-05

_New Hampshire bank website with tools to manage loan and deposit products and rate display. to manage_

<p>This was the first bank website I built with Lightfin. The .NET site is driven by a Master Page and an XML document that controls the navigation for a web site of about 40 pages. The site also includes .NET tools to present interest rates for loan and deposit products as well as feedback tools for users.</p>

<p>XML-driven navigation has been a solution I've used for static web sites (that is, sites not driven by a CMS) since we came up with it at PixelMEDIA in 2001 or so. It makes it much easier, especially on larger sites, for clients to change their mind about the structure of a site during development (or even after launch). When I started at Pixel, that was one of our biggest pain points. A change in structure on a large enough site would lead to the job going on hold, the client being billed for additional time and general unhappiness. Once we figured out a way to control the navigation on all pages with an edit to one file (I'd originally done it as an ugly series of nested PHP arrays until someone suggested XML as a cross-platform way of solving the problem, doubly important since ASP didn't have a structure as easy to work with as PHP's array), the problem went away and development times sped up considerably.</p>

<p>As with every .NET site in the portfolio (at least as of mid-2010), this uses my home-grown MVC framework. Written before anyone at Microsoft bothered to let me know they were going to provide much the same thing, I still like working with it. It's not because it's the best possible approach ever, but because it does exactly what I want it to and gets out of the way for the rest. Whatever its relative merits, it makes it rapid development much easier or me in .NET. The client recently came back to us to extend the content management tools and the fact I could turn around the changes in under a day reinforced my belief in the approach.</p><img src="images/portfolio/ps-home.jpg" alt="Home " style="margin: 1em 0" />
<img src="images/portfolio/ps-rates.jpg" alt="Rates Rates are pulled by product & product type for display to users" style="margin: 1em 0" />

