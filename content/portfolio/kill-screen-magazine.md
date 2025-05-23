Title: Kill Screen Magazine: Kill Screen Magazine
Slug: kill-screen-magazine
Tags: django,videogames
Category: Portfolio
Date: 2011-03-01
Author: Tom Clancy
Url: kill-screen-magazine

# Kill Screen Magazine: Kill Screen Magazine

## 2011-03-01

_Django-based site for a print-based video game publication moving online. One of the most attractive and enjoyable projects I've worked on._

<p>I used to work with <a href="http://savetherobot.com/" target="_blank">Chris Dahlen</a> at <a href="http://www.pixelmedia.com/" target="_blank">PixelMEDIA</a>. I also like video games. Lest this summary turn into a third-grader's book report, let me say that when Chris contacted me to build a web site to be a companion to the gorgeous magazine he had co-founded, I leapt at the chance.</p>
<p>The whole thing actually launched with no design whatsoever: the initial application behind the site was a poll application that allowed writers to vote for their favorite titles of the year (<a href="http://killscreendaily.com/articles/kill-screen-high-scores-best-2010" target="_blank">2010 results</a>, <a href="http://killscreendaily.com/articles/high-scores-best-2011" target="_blank">2011 results</a>) before the site launched. Poll applications aren't the toughest thing to write, but this one had some fun challenges because it had to allow for free-form entries of games no one else had heard of while still doing its level best to avoid duplicates. And because it worked much like the <em>Village Voice's</em> Pazz and Jop voting, there was a bit of logic wrapped up in making sure points were correctly alloted. And that was all tied into a friendly Ajax interface.</p>
<p>Once the poll was done, it was time to build an article &amp; review system. Again, all of this would be pretty standard, but Kill Screen always aimed to be a little bit different. A couple of months after the start of the project, i got a rush email from Chris asking if there was anyway to create a game review who's score would vary with the phases of the moon for&nbsp;Sword + Sworcery. Six days later (thanks to a little help from some <a href="http://inamidst.com/code/moonphase.py" target="_blank">Python code on the web</a>), it was <a href="http://killscreendaily.com/articles/reviews/review-superbrothers-sword-sworcery-ep" target="_blank">alive</a>.</p>
<p>There are a number of tools running behind the scenes as well to aggregate video game RSS feeds, track problems and generally make it easy to get content on the site without having to know HTML (and without breaking the gorgeous design).</p><img src="/images/portfolio/CropperCapture1.png" alt="Home Page Features a jQuery-powered scroller" style="margin: 1em 0" />
<img src="/images/portfolio/CropperCapture2.png" alt="Article " style="margin: 1em 0" />
<img src="/images/portfolio/score.png" alt="Score " style="margin: 1em 0" />

