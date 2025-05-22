Title: CSS: min-width vs. zoom
Slug: css-min-width-vs-zoom
Date: 2013-05-22 11:00:49
Tags: css,responsive
Category: Posts
Author: Tom Clancy

# CSS: min-width vs. zoom

Ran into an interesting quirk today that I don't see a lot of search results for: if you have a min-width set on an element but then set a zoom on an element other than 100%, the min-width (and, one presumes, the max-width) is scaled by the zoom factor. In this case I was working on a responsive design that has a fixed header image for anonymous users. While the body and the header had a min-width of 480px set, when I scaled the header image down, it continued to squeeze below 480px. The fix looked like this:

<pre class="prettyprint">
#guest-bar {
    zoom: 70%;
    /* min-width of 480 but at 70% */
    min-width: 685px;
}
</pre>
