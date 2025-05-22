Title: VM Development
Slug: vm-development
Date: 2008-03-07 17:13:24
Tags: 
Category: Posts
Author: Tom Clancy

# VM Development

I do my Windows development on a beast* of a Bootcamp'd Mac Pro tower and that works just fine, or it would if every project I worked on were virgin territory, untouched by human hands. Unfortunately, some of what I work on has been touched by human hands, and they're all thumbs. I suppose it's coming from an agency background, but it's strange to me how many people act as though their site/ app is the only thing on a box. In celebration of my MSDN discs finally arriving (well worth the six months' wait, the 100 emails and phone calls and general frustration, thanks for asking), I built a VM in the background while I worked today. I couldn't get SQL Server 2008 to install (because I am dumb and don't understand what they mean when they describe all the account logins), but everything else is, for better or worse, current MS tech: Server 2003, VS2008, SQL 2005. I even threw IE8 and Silverlight on for laughs.

Then immediately put Firefox on as IE8 . . . I don't understand how it gets things so wrong. They've added a bunch of features from Firefox, but they can't simply copy them because then people would notice they copied them. So they copy them and screw them up. Firefox 2 added the yellow URL bar to let you know when you're on a secure URL. Firefox 3 adds a little green section to show you who owns the SSL certificate so users are (theoretically) better protected against phishing. If you like that, IE thinks you will love their idea: everthing but the actual domain in the URL bar is greyed out so it's barely legible. Given the cool kids have been talking for 3-4 years about how the URL bar is the new command line and frameworks like Rails go to great pains to make the full URL informative, this is a fantastic way to fuck that up. A+. And it just goes from there. Everything feels off-brand. All that's missing is some Engrish.

Either way, now I have a nice new VM image I can re-use for development on projects:
<ul>
	<li>SQL Server</li>
	<li>Visual Studio</li>
	<li>Tortoise SVN</li>
	<li>Launchy</li>
	<li>Taskbar Shuffle</li>
</ul>
And a little here and there. As soon as I was finished, I sent a copy up to my Amazon S3 account so I could get at that VM from any machine anywhere in the world. As it slowly ticked that 12 gigs into the cloud, I realized I'd just blown 50 cents. Where do I ever go? Stupid bloggers trying to make coding sound rock'n'roll.

<small>* A beast to me anyway. Not compared to the 4 proc, 64 gigs of memory monsters the cool Mac kids have for opening what must be some massive Youtube videos</small>
