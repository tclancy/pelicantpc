Title: Community Trust Bank: Community Trust Bank Site
Slug: community-trust-bank-site
Tags: django,google,googlemaps,geodata,geolocation
Category: Portfolio
Date: 2010-04-01
Author: Tom Clancy
Url: community-trust-bank-site

# Community Trust Bank: Community Trust Bank Site

## 2010-04-01

_CMS and Django tools for a Louisiana bank web site. Tools allow the bank to manage multiple product lines with different details from state to state._

<p>Community Trust Bank is based in Louisiana but has expanded into Mississippi and Texas. In order to better serve their expanding customer base and to better reflect their growing size, they contracted <a href="http://www.lightfin.com/">Lightfin Studios</a> to build a new site. The site is powered by a custom Django CMS that brings together a number of applications. Page content is edited in a friendly WYSIWYG interface in the Django administration tools. Products (e.g., checking accounts, loans, CDs) and rates are also managed in the administrative tools and the relevant pages pull in the information as needed. Additionally, the pages customize the products and rates listed based on the user's selected state (and require the user to select a location before displaying any content). thumb:1</p>
<p>In order to help existing customers find the branch or ATM location closest to them, the site provides a <a href="https://www.ctbonline.com/pages/locations">Google Map listing branches and ATMs</a> with custom icons on the map. A search form is provided so users can filter the map and location list down to just locations near their zip code. All of this is powered by a Django application that stores locations, zip codes and the longitude/ latitude pairs for each. Rather than force non-technical administrators to look up the longitude and latitude for their locations, locations are looked up for them via an API provided by&nbsp;<a href="http://tinygeocoder.com/">TinyGeocoder</a>.</p><img src="images/portfolio/ctb-home.jpg" alt="Homepage Community Trust Bank has locations in Louisiana, Mississippi and Texas." style="margin: 1em 0" />
<img src="images/portfolio/ctb-locations.jpg" alt="Locations Tool Google Map with radius search based on a user's zip code." style="margin: 1em 0" />
<img src="images/portfolio/ctb-rates.jpg" alt="Rates Display Current rate information is based on the user's location" style="margin: 1em 0" />

