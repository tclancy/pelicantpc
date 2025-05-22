Title: Microformat Proposal: Coding Experience
Slug: microformat-proposal-coding-experience
Date: 2009-09-19 09:13:29
Tags: 
Category: Posts
Author: Tom Clancy

# Microformat Proposal: Coding Experience

When I'm working, even in a language I know well, I often search for how to do something; either because I don't know or because I feel there's a better way (as <a href="http://twitter.com/ed_atwell">@ed_atwell</a> says, "I don't know, but I bet my friends <a href="http://www.google.com/">Larry and Sergei</a> do). My personal system for filtering code search results looks something like:
<ol>
	<li>Blogs I trust</li>
	<li>Personal blogs</li>
	<li>Development sites (e.g., 4guysfromrolla.com, etc.)</li>
	<li>Mailing lists and newsgroups<sup><a href="#foot1">1</a></sup></li>
	<li>Forums</li>
	<li>Expert Sexchange</li>
</ol>

Regardless of where it comes from, there's no way to know if it's right. It's human nature to use the first thing that works (if under deadline, even the first thing that kinda works will do). As Jeff Atwood has <a href="http://www.codinghorror.com/blog/archives/001257.html">pointed out</a> (<a href="http://www.codinghorror.com/blog/archives/001268.html">twice</a>) , the danger is you might be copying off the paper of someone dumber than you<sup><a href="#foot2">2</a></sup>. Because of this, I'd like to propose a <a href="http://microformats.org/">microformat</a> (assuming one doesn't already exist, given I didn't bother to check with Larry and Sergei) to indicate an author's experience with a language.

<em>Immediate disclaimer</em>: I realize this is a programming solution to a human nature problem and those never work, but bear with me, because my hope isn't to fix the problem, but to provide some metadata that will let machines do the work for us so we can stay lazy. Given that is in line with <a href="http://en.wikipedia.org/wiki/Newton%27s_first_law#Newton.27s_first_law">Newton's First Law</a>, this will obviously be a huge success.

The format doesn't need to be very complicated. In fact, I'd prefer if it just provided a few bits of raw data that could be remixed by search engines however they see best. The data provided would stay the same but the algorithms could be tweaked for better results (though that would require feedback), providing an incentive for search engines to consume the format. Make the data something rough, broad and quick to fill out, like years of experience with the language and a simple measure of number of lines written (e.g., none, 10, 100, 1,000, 10,000, a whole bunch). There are any <a href="http://en.wikipedia.org/wiki/Source_lines_of_code#Disadvantages">number of issues</a> with using Lines of Code (LoC) as a metric (mainly that an idiot can say in 1,000 lines what a smarter person can say in 10), but if the ranges are broad enough, it should dampen the effect.

Bolt this format onto syntax highlighting engines; this blog, for example, uses <a href="http://wordpress.org/extend/plugins/wp-syntax/">WP-Syntax</a> to format the few, poor code samples I provide&mdash; one more panel in the plugin admin that allowed me to store a hash of [language name, years, lines of code] would allow the plugin to provide that information in any page using the languages and output a visible box on the page so inexperienced users who come to the page and see my code could know it was terrible without <em>knowing</em> it was terrible. Add it into the syntax formatters for popular forum software (and allow users to specify their experience) and every code argument in a forum post becomes a little easier to follow.

The format doesn't tell you if a snippet is correct, it just gives you some background information (assuming the author is honest in their self-reporting). The danger would be users trusting a snippet blindly because the author has 10 (bad) years of experience (a sort of <a href="http://en.wikipedia.org/wiki/Argument_from_authority">"Appeal to authority"</a>) while better code from "newer" users goes ignored. That's a human nature problem and obviously you can't solve those with programming (/broad wink).

<small><span id="foot1"></span>1. I'd rank these higher, especially official groups for languages and systems except for two reasons:
<ol type="a">
	<li>They tend to be so ill-formatted and the ability to follow threads varies wildly from site to site</li>
	<li>The advice can be good but dated: it's easy to find perfectly legitimate Python answers from 2000 or so. While the answer is fine, it's possible there's a newer idiom and in a language like Python, where there's <a href="http://www.python.org/dev/peps/pep-0020/">"one right way"</a>, the right way will be the way that the language has been optimized to work. </li>
</ol>

<span id="foot2"></span>2. Basically unrelated story that I've crammed in because I always tell it because it cracks me up: in high school, we had to go to the local public high to take the SATs. The person sitting next to me scribbled furiously throughout the test and was always the first one finished (which frustrated me to no end). When we were walking out, he turned to us and said, "Dude, I just made pretty pictures with the bubbles."
</small>
