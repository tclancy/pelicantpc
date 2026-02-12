Title: The Effect of Gas on a Marriage
Slug: marriage-and-gas
Date: 2026-02-12
Tags: bluelink,typescript,docker,vibecoding
Category: Posts
Author: Tom Clancy

# The Effect of Gas on a Marriage

I was well into my 30s before I realized my mother's aphorism on relationships,
"Fits find each other" had a positive meaning. Because my mother and her sister
both taught in special education and because their side of the family is from the
school of "If you have nothing nice to say and it's funny, sit with us", I'd
assumed it only ever meant kids who couldn't sit still wind up together later in
life. It was the '80s, "fits" would have been one of the nicer terms that was _au
courant_ among educators back then.

I mention this because my wife and I describe this pattern (which [Plato phrased
differently, but we all know what he meant](https://www.laphamsquarterly.org/eros/platos-other-half))
pretty perfectly. A marriage counsellor (thank you Will!) described the dynamic
as "Your Dance". Michelle is the outgoing, friendly person in charge of ensuring
we do things that actually make life worth living. I am the pragmatic, paranoid,
hard-working Yankee puritan who bars the doors lest worse should befall us. Given
this dynamic, it means I often start a car which tells me, `Fuel low, would you
like to search for a nearby gas station?` The last time it happened, the Hyundai
and I had seven miles together before things would have ended. I _dread_ running
out of gas. It's happened maybe twice in a half century and neither time was my
fault, but it drives me to distraction. I got the Hyundai to a station a couple
miles away with 0.2 gallons left to my name.

Early on in my work as a developer, I decided, "There are no technological
solutions to social problems". I still believe that, but there is also no solution
to this problem. In theory, I could not fill the tank to teach a lesson, but
my daughter could be in tow at the time of the lesson and I would catch hell
from both of them. And that's assuming I could somehow endure the nearly
physical pain of knowing the car needed gas.

So. Stopped at a light in front of the gas station this week, I remembered I'd
played with a [GitHub repository](https://github.com/Hacksore/bluelinky) that
lets you talk to the Hyundai/ Kia BlueLink API but lost interest when the problem
I was sorting (automatically heating the car on winter mornings) solved itself
(broken garage door got fixed). I turned the whole thing over to Claude, showed
him there was a Docker version of the repo he could steal from if needed and we
built a notification system for low fuel so I am less likely to be surprised in
the future.

My fork [is here](https://github.com/tclancy/bluelinky). It has some of the hallmarks
of vibe-coded slop, but even those are things I am finding ok-_ish_ in these
projects. It was a good fit for the approach as the API represents a solid set
of defined options, I wrote up a light spec and then used Plan mode to elicit
questions about things that were unclear and it was grunt work I _could_ do but
would never get around to because it represents a Busman's Holiday to be doing
unfun, non-greenfield coding for something no one is paying me for. This time
around the surprise was in how quickly we were done. It's not a huge process
but I thought sending notifications would take more work. Again, here's a place
where AI shines: there's a ton of code and documentation in the wild about how
to use any notification system of even medium popularity, so steal from that
via AI. The vibe-coded slop is 95% a result of the fact sending SMS messages
programmatically got much harder (understandably given all the SMS spam) since
the last time I needed to do it for work. It's apparently ~$10-15 a month just
for the privilege of a number and the ability to send SMS in the US from it. I
tried the "email your cellphone number at the carrier address" as a workaround
but it lasted for one message and one message only.

That's probably something worth calling out about my experience in vibe coding:
because I have been doing this a long time, in a lot of languages for a lot of
different projects, some things come naturally as breathing. I worked in Django
_a lot a lot_ and came to appreciate the nature of pluggable backends. Suspecting
notifications might turn out to be a pain in the ass, plus the fact I did this
when I rebuilt the notification system at a recent job using Knock, I made the
notifications pluggable because it's a lot easier to develop with something
spitting the notifications as logs in the console immediately than having to
wait for a message to maybe show up in a dashboard seven levels deep in someone
else' site. So the commit history of my fork includes a bunch of aborted back-end
attempts. I was tempted to keep them all for posterity but then I realized how 
wildly egotistical that sounded.

May you never has gas-related issues in your relationships again.
