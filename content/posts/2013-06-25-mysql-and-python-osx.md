Title: MySQL and Python on OSX
Slug: mysql-and-python-osx
Date: 2013-06-25 17:11:01
Tags: mysql,python,osx
Category: Posts
Author: Tom Clancy

# MySQL and Python on OSX

Because I rarely use MySQL nowadays and because how often do you set up a new machine, this is a reminder to myself on how to get mysql-python installed in a virtualenv

1. Add /usr/local/mysql/bin to your path (permanently in your .profile)
2. If "pip install mysql-python" fails, try [this version](http://stackoverflow.com/a/6853460/7376): 'sudo ARCHFLAGS="-arch $(uname -m)" pip install mysql-python'
3. Realize none of that made much of a difference and then [blindly copy & paste from here](http://learninglamp.wordpress.com/2010/02/21/mysqldb-python-mysql-and-os-x-a-match-made-in-satans-bum/)
4. Discover that's still not quite everything and make [this symbolic link](http://stackoverflow.com/a/6967816/7376) (unless the paths change between now and when you find this)
