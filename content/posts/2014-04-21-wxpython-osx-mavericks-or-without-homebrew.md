Title: wxPython on OSX Mavericks with or without Homebrew
Slug: wxpython-osx-mavericks-or-without-homebrew
Date: 2014-04-21 13:34:26
Tags: python,osx
Category: Posts
Author: Tom Clancy

# wxPython on OSX Mavericks with or without Homebrew

Just a short note for anyone else who runs into this nonsense: I could not get the current version of wxPython to install in a useful way using homebrew. `brew install wxmac --python --devel` to install into my Homebrew-controlled Python install worked, but it missed a portion of the code. There should have been a `python` directory under `/usr/local/Cellar/wxmac/3.0.0/lib` that contained the relevant code and a `wx.pth` file I could symlink into virtualenvs. There was not. I don't know if this is a bug or an issue with my setup (some of the links mentioned Homebrew will only install it for use as a "framework" and I honestly have no idea what that means or time to investigate, but I think it may be relevant).

So I tried using the [installer provided at wxpython.org](http://www.wxpython.org/download.php) but those were all corrupt according to OSX. I had my suspicions about multiple files being corrupt and they turned out to be correct: the files aren't corrupt, [they're not signed the way Apple wants.](http://stackoverflow.com/questions/21223717/install-wxpython-on-mac-os-mavericks). Shutting off the privacy controls temporarily fixed that. Then it was a simple matter to symlink WX into a virtualenv, e.g., 

`ln -s /Library/Python/2.7/site-packages/wxredirect.pth ~/.virtualenvs/envname/lib/python2.7/site-packages/.`

Update: turns out, once again, [I am an idiot](https://github.com/Homebrew/homebrew/issues/28583#issuecomment-40958167); contrary to what I'd read, you need to install `wxpython`, which will include `wxmac`, not the other way around.
