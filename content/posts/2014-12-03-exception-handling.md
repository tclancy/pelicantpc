Title: Exception Handling
Slug: exception-handling
Date: 2014-12-03 16:01:19
Tags: coding
Category: Posts
Author: Tom Clancy

# Exception Handling

I've been thinking about exception handling a lot recently. A., because I'm stultifying and B., because it's been a source of contention in the codebase I'm responsible for. I wrote some formal documentation last week to try to normalize our approach, but I'm not happy with it. I'm not good at writing formal documentation&mdash; it always comes out stiffer than I want and feels like all nuance is lost. Also, I'm in the middle of listening to [this podcast](http://5by5.tv/changelog/100) about the Go Language and they've just touched on exceptions and I think it's helped me crystalize my thoughts. This post will tell if that's true. 

## Exception Enlightenment

### Step One: complete newbie

No exception handling happens here. The second your code works once, you're done. "No one touch anything, it works." You push the baby bird out of the nest, ask a coworker to try it out and hold your breath. In the worst case, they're a friend and try to use the program the way you think it should work. In the best case, they're a prick and put in numbers where you ask for text and text where you ask for numbers and try to divide everything by zero.

### Step One Point Five: "I've got to do _something_"

You add checks for everything your tester tried and everything else you can think of. You quickly learn you can't think of much because you think like the program (or, more accurately, the program is laid out the way you think through problems). Someone puts in a floating point number for their name and you're right back where you started. Maybe you hear about fuzz testing, maybe you know a lot of assholes. The inevitable conclusion: you can't possibly think of everything and prevent it.

### Step Two: exception handling

Holy shit! You can prevent everything that could ever go bad. It's as simple as this:

<code><pre>
try:
    answer = a / b
except:
    # suck it haters!
    answer = 0
</pre></code>

My guess is this is where a lot of people give up on programming, stop growing as a programmer or relegate programming to a hobby or something they do only when they have to because this approach makes life so much harder.

### Step Three: a little bit of light

It turns out "naked" try/ catch blocks where you don't bother to specify what kind of exception you're handling are much worse than not doing anything. You learn this after smashing your head against your monitor for a day trying to figure out why something doesn't work but doesn't blow up only to finally see the `try/ catch` your eyes normally skim past without noticing. "Couldn't be. Nah. Well, maybe . . . " and you rip out the block and there it is: you thought you were catching a type error to stop users passing in strings and maybe handling divide-by-zero while you were at it, but it turns out it's also swallowing a whole host of floating point ugliness, missing variables, an import you forgot and hey, it looks like your network connection is in the crapper.

So now you need to do some reading and it turns out exception handling is a microcosm of programming. There are multiple styles, opinions about how to use exceptions, whether to use exceptions, whether to expect exceptions (?!) . . . like choosing a language or a platform or anything else in programming, exception handling is one more bar brawl to stick your face into.

### Step Four: I don't know what step four is yet

One of the things I like about Python is for a language whose [founding principles](https://www.python.org/dev/peps/pep-0020/) include "There should be one&mdash;  and preferably only one&mdash; obvious way to do it", it's pretty unopinionated about how you use exceptions. We're told exceptions are inexpensive in Python (maybe said with a bit of a sneer and a knowing look in the direction of statically-typed languages), so much so they're used idiomatically in places you would otherwise be using an `if/ else` test. That inexpensiveness is a bit misleading and [you should think about which is the most common case](http://stackoverflow.com/questions/5589532/try-catch-or-validation-for-speed/5591737#5591737) in the code you're writing when deciding between `if/ else` and `try/ catch` but unless you're inside a loop inside a bit of code that gets called an awful lot, there are more important things in your code to worry about.

All of which brings me to today and that podcast wherein one of the maintainers of the Go language at Google turns up his nose at exception handling in general (Go doesn't have it) and Python in particular. My immediate reaction was typical fanboy: start assembling arguments in favor of your chosen gang instead of listening to the other side. When I stopped and thought about it, I realized what they were discussing was probably really close to how I think of exceptions. 

There's a line of argument in the Exception Handling bar fight that goes something like this: "How can you handle exceptions when they're, by definition, _exceptional_?" This typically comes from a Theoretical Asshole (somehow they're always assholes in real life too) who took some Comp Sci classes without ever hearing anything. The name means different things to different people: for some they're exceptions like when it rains in summer, for others they're Exceptions like when it rains in the desert. I fall into the former camp: I use exceptions interchangeably with `if/ else` tests, most likely because I've been working in Python for too long. But whichever approach you prefer, let's agree you use an exception because you want to log something weird so you can stop it from happening in the future. What was argued against in the podcast is something I'd like to dismiss as a straw man because it's madness, but I've seen enough of it to know better. Whether `try/ catch` or `if/ else`, the code should look like:

<code><pre>
try:
    return a / b
except ThisOneWierdException:
    logging.exception("WTF?")
    return error_message("You really are an asshole, you know that?")
</code></pre>

Never like this:

<code><pre>
try:
    answer = a / b
except ThisOneWierdException:
    answer = default
keep_doing_stuff_like_nothing_is_wrong_like_you_always_DO_mom()
</code></pre>

At this point I do have to pick nits about the word: it's an exception. You're not supposed to keep soldiering on. There are things like "Try to find the user's old data in a file on disk, if that doesn't exist, try looking in the database, if that doesn't exist start with a blank data set." You can use `if/ else` or `try/ catch` for that kind of thing, I don't care. But if you expect the thing to happen, it's not exceptional. When something exceptional does happen, get out, log everything you can and try to patch the hole tomorrow.
