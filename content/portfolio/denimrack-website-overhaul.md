Title: denimrack: Denimrack Website Overhaul
Slug: denimrack-website-overhaul
Tags: php,xcart,maintenance,ajax,smarty,ecommerce
Category: Portfolio
Date: 2008-11-10
Author: Tom Clancy
Url: denimrack-website-overhaul

# denimrack: Denimrack Website Overhaul

## 2008-11-10

_Updated an existing X-Cart-powered ecommerce site to improve usability, correct bugs on the front-end and add reporting to the administrative tools._

<p>Denimrack came to me with a list of edits they wanted to make to their live web site. I added tracking of abandoned purchases so Denimrack can follow up with users to find out how to better meet customer needs. The site now has an Ajax-powered feedback form so users can get in touch with the company no matter what page they're currently viewing. Similarly, users can now submit return requests from any page on the site. I dug into the interface and code to figure out how Denimrack could offer discounts to users through coupons and volume discounts. I then hooked some custom code into X-Cart so the site now watches user's shopping carts to alert them when they are close to achieving a volume discount.</p>
<p>We spent a good deal of time on the product detail screen since this is where users spend most of their time. I cleaned up a  number of display issues across browsers, made Clearance/ Sale status more prominent and added a link to allow users to consult Denimrack's stylist with questions about the pair of jeans they're currently viewing. All edits and changes I made were carefully integrated into the existing coding approach. This was my first experience working with <a href="http://www.smarty.net/">Smarty</a>, so it took some time to get used to actually having logic and presentation separation in PHP, but it was well worth it and Smarty has become part of my PHP solution toolkit.</p>
<p>On the administrative side, the client wanted more visibility into their overhead and sales. I integrated inventory and sales reports that can be filtered by date range into the existing custom administrative panel provided by the original developers.</p><img src="images/portfolio/dr-home.jpg" alt="Home Page " style="margin: 1em 0" />
<img src="images/portfolio/dr-detail.jpg" alt="Product Detail " style="margin: 1em 0" />
<img src="images/portfolio/dr-returns.jpg" alt="Returns Form You can make a return request from any page on the site without losing your place." style="margin: 1em 0" />

