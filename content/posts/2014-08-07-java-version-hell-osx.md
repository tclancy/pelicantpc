Title: Java Version Hell on OSX
Slug: java-version-hell-osx
Date: 2014-08-07 15:33:27
Tags: java,osx,bugs
Category: Posts
Author: Tom Clancy

# Java Version Hell on OSX

In one of those "Why did I even look at the terminal" moments, I noticed Solr stopped working properly in a local Django setup. Initially I ignored a slew of 404 errors when Haystack tried to reindex because . . . well because who the hell cared? I'm not trying to find anything, I'm trying to build stuff. Which means I immediately got a feature request related to searching. Not only was Solr not reindexing, but trying to visit the Solr console at http://127.0.0.1:8983/solr returned a 404 error page saying

```
No context on this server matched or handled this request. Contexts known to this server are . . .
``` 

Now actually looking at the ream of text going by on Solr startup I noticed `UnsupportedClassVersionError` was the root problem. This happens when you're trying to run Java code that was compiled for a newer version than you are running. Annoying given I don't actually work with the language so why is it given me such a hassle and strange because I installed Solr with [homebrew](http://brew.sh/) and homebrew doesn't make mistakes like that (especially since it all worked for a long time after install). Distant bells started ringing about something I installed* that let me know it needed an older version of Java. I said yes because like everyone else, dev or non-dev, I pretty much agree to prompts to get them to leave me alone and who the hell would suspect the thing not only installed an older version of Java but then went on to make it the system version? The nicest thing I can say about a mind that reaches such a solution is there's a reason people crap on Java projects.

To add a little extra spice to make life extra nice, Apple and Oracle hate each other and so you have to run between the trenches in No Man's Land of their war to get Java installed. Looking for Java 1.7, I started [with this Stack Overflow thread](http://stackoverflow.com/questions/6267392/how-do-i-use-jdk-7-on-mac-osx) and installed the linked DMG and everything was all better. 

No of course it wasn't, don't be silly. 

Nothing happened as far as I could see. `java -version` (BTW, it's awesome Java can't follow the convention of a single dash for shorthand command line switches and a double dash for full name switches) still returned 1.6 and looking in `/System/Library/Frameworks/JavaVM.framework/Current/` still showed `CurrentJDK` pointing to `/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents`. Looking in `/System/Library/Java/JavaVirtualMachines/` did not reveal a 1.7 folder waiting there to be found because that would mean any old idiot could solve this mystery instead of requiring a special kind of thickheaded idiot. I renamed the `CurrentJDK` symlink to `JDK16` for later on in life when this all bites me in the ass the other way 'round and then created a new symlink to the 1.7 version with this: `sudo ln -s /Library/Java/JavaVirtualMachines/jdk1.7.0_67.jdk/Contents CurrentJDK`. Problem solved, at least until I have to use another piece of Java.

<sub>\* For the curious, I think it was when I installed 12 different versions of jMeter via homebrew in the hopes of getting an old jMeter script to actually open instead of throwing errors about bad counts. If you ever want to know about installing older homebrew formulae, [here's a good start](http://stackoverflow.com/questions/3987683/homebrew-install-specific-version-of-formula). `brew` even has a `brew edit` command so you can easily open the formula to repoint download links when the mirror it wants to use no longer has a copy of the ancient piece of crap you're trying to install.</sub>
