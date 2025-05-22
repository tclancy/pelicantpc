Title: Setting Up Server SSH Access
Slug: setting-server-ssh-access
Date: 2013-10-04 11:55:21
Tags: ssh,notes
Category: Posts
Author: Tom Clancy

# Setting Up Server SSH Access

Because I always forget and because I am getting into the good habit of connecting via SSH for everything, here's a note to myself on how to get SSH deployment keys running in my typical process:

* [Use or generate a key](https://help.github.com/articles/generating-ssh-keys)
* Add the key as a read-only deployment key on the Bitbucket repository
* [Register the key locally](https://help.github.com/articles/error-permission-denied-publickey#make-sure-you-have-a-key-and-ssh-is-using-it)
* When the registration fails, [turn on the SSH agent first](http://stackoverflow.com/a/17848593/7376)
* Set up a ~/.ssh/config file and run `chmod 600` on it
* Alternatively, just use [this solution](http://stackoverflow.com/a/11832171/7376) to brute force it: `ssh-add ~/.ssh/my_private_key &>/dev/null`
* Probably need to add ``eval `ssh-agent -s`  &>/dev/null`` in the profile right before it (I think it depends on whether the key file has a default file name like "id_rsa")

Edited again because apparently I'm an idiot and that's a bad idea:

```
trap '[ -n "$SSH_AGENT_PID" ] && eval $(/usr/bin/ssh-agent -k)' 0
eval $(ssh-agent -s)
ssh-add ~/.ssh/bitbucket_read
```

>The 'trap' line will kill the ssh-agent when you log out.
>You can also feel free to add "&>/dev/null" to the end of those lines to silence them, once you are sure they are working.
