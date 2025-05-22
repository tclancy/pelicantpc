Title: Windows GPG Front-End
Slug: windows-gpg-front-end
Date: 2009-02-17 13:26:22
Tags: 
Category: Posts
Author: Tom Clancy

# Windows GPG Front-End

I'm doing some work with GPG encryption and I always like to have a visual/ gui front-end to use to make sure I haven't screwed something up in my command line adventures. I came across <a href="http://cryptophane.org/">Cryptophane</a> today and it seems like a nice way to keep track of my particular <a href="http://en.wikipedia.org/wiki/Alice_and_Bob">Alice and Bob</a>. The only problem I ran across was that my GPG install was in a non-standard place and Cryptophane doesn't look in the registry (I'm pretty sure GPG writes to it). The error wasn't immediately clear and there's no online help (though a .chm is provided), so I thought I'd post this for anyone else who runs into a similar problem. My shortcut target now looks like this:
"G:\Program Files\Cryptophane\Cryptophane.exe" <strong>--gpg-path "G:\Program Files\GNU\GnuPG\gpg.exe</strong>"

Your paths may vary, etc.
