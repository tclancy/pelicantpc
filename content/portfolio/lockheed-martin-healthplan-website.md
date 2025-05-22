Title: Lockheed Martin: Lockheed Martin Healthplan Website
Slug: lockheed-martin-healthplan-website
Tags: django,pdf,pisa,jquery
Category: Portfolio
Date: 2009-06-19
Author: Tom Clancy
Url: lockheed-martin-healthplan-website

# Lockheed Martin: Lockheed Martin Healthplan Website

## 2009-06-19

_A site for Aetna health plan customers at Lockheed Martin_

<p>My first Django project and first work with <a href="http://projectevolution.com/">Project Evolution</a> was a site for Aetna health plan. The bulk of the site is driven by a Django-powered content management system with the rest of the content from a series of applications. thumb:1</p>
<p>The <a href="http://www.lmhwplan.com/faqs">FAQ</a> section does double-duty as a set of frequently asked questions and a message board for users to ask questions of site administrators. Questions are answered in the Django administrator panel which forwards the response to the user by email. If the question is general enough, the administrator can promote the question and answer into the FAQ list.</p>
<p>The glossary application generates a standard <a href="http://www.lmhwplan.com/glossary/A">Glossary of Terms page</a>, but building the application was anything but standard.&nbsp;thumb:2&nbsp;The first time I built a glossary tool, it was in ASP and Access, probably around 2002. Just to generate the list of letters at the top of the page required creating an array and typing every letter of the alphabet (the smarter me, a couple of years later, learned to write them out as a string and then split it into letters, but it's still typing and there weren't keen list sites all over the Internet where you could cut and paste from). So you'll have to imagine how pleased I was to be working in Python, where I could just loop over <a href="http://docs.python.org/library/string.html">string.uppercase</a> (or .lowercase if you prefer). The bit of the glossary I'm most proud of is harder to find: I built a template tag that looks through any piece of content, finds phrases and words that exist in the glossary and marks them up so users can find out what a term means without leaving the page (you can see an example by hover over "HealthPlan" in the fourth bullet point <a href="http://www.lmhwplan.com/page/basics-of-the-plan/fast-facts-about-the-plan">here</a>). The tag is smart enough that it only marks a word once, doesn't mark up a word inside certain HTML tags (so it doesn't pop up and prevent you from clicking on a link) and looks for the longest matching phrase in each case (so phrases that contain other glossary terms get properly marked).</p>
<p>Aetna provides Lockheed Martin employees with an <a href="http://www.lmhwplan.com/page/your-action-plan">Action Plan</a> to help them improve their health.&nbsp;&nbsp;thumb:3&nbsp;The application allows administrators to provide a plan, tips and hints for every month. It's available as a series of HTML pages, print-friendly pages or as a PDF for downloading. To make the PDF version easy to maintain and update, it's generated as a standard Django view with an HTML template that is turned into a PDF using <a href="http://www.xhtml2pdf.com/">Pisa</a>.</p><img src="/images/portfolio/LM_Home.png" alt="Home Page " style="margin: 1em 0" />
<img src="/images/portfolio/Rendered_glossary.png" alt="Glossary The full glossary that powers the content page tooltips" style="margin: 1em 0" />
<img src="/images/portfolio/LM_Action_Plan.png" alt="Action Plan One month of the action plan in the HTML version" style="margin: 1em 0" />

