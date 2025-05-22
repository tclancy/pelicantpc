Title: &quot;Life&#039;s Good&quot;, Indeed
Slug: quotlife039s-goodquot-indeed
Date: 2008-12-17 09:37:20
Tags: 
Category: Posts
Author: Tom Clancy

# &quot;Life&#039;s Good&quot;, Indeed

I am providing this post-mortem both as a public service and so I don't punch in the screen of my brand-new LG monitor. I picked up a new <a href="http://www.lge.com/products/model/detail/l227wt.jhtml" onclick="window.open(this.href); return false;">22" monitor</a> at Best Buy yesterday after losing a monitor to the power surges from the ice storm (what I ought to have done is replace the APC unit that's now cost me an external drive enclosure and a monitor, but that's another gripe). Almost 24 hours later, the monitor is actually running as expected. Let me preface this by saying I appreciate my setup might be a little different from what the folks at LG bothered to test on:
<ul>
	<li>Mac hardware running Windows</li>
	<li>it's a second monitor</li>
	<li>NVidia and <a href="http://www.realtimesoft.com/ultramon/overview/" onclick="window.open(this.href); return false;">UltraMon</a> are both fighting for control of the setup</li>
</ul>
All the same, this was a more painful hardware process than I remember going through. It's a goddamn display, not an ultrasound machine. Nothing should be more plug-and-play. And yet, when I plugged it all in with the existing VGA connection from the old monitor, none of the native resolutions were available. I installed the software and drivers, but it still couldn't figure itself out. The LG software could identify my primary monitor, but the software would not allow me to use any of the features because it could only run on an LG device. Even when it figured out there was an LG display somewhere, no dice. I'm assuming it has to be the primary display. Also, for a company that's done such a good job of becoming an international player, it's disappointing the English was as broken as the software displaying it.

I gave up on LG and updated the NVidia Control Panel, hoping newer versions would have the widescreen resolutions. Playing with the new control panel only blew things up worse: reversed the primary and the secondary and then screwed up Ultramon so badly the taskbar was displaying a box for every background process running on the box under my user account. It also saw fit to snap the resolution on both monitors to something fun. So, reboot.

My last gasp, and it included a fair bit of gasping as I've been screwing off work due to a wrenched back, was to find a DVI cable and try that. Nothing. No second monitor, no avowed knowledge of a second monitor in the control panel. For no good reason except I'm my own IT department, rebooted. Success! Sort of. Both monitors are working during bootup, both are correctly identified in the control panel, both have their proper native resolutions dialed in and programs are being popped up on the LG. Just one issue: it's power light is in orange standby mode, the screen is off and no amount of pressing the power button will convince it to turn on or off. This is when one has to say, "I can tell a convincing lie to the returns desk if need be" and show inanimate objects just who the hell runs the show around here. Out comes the power cable. The funny little capacitor manages to keep the light orange for five brave seconds before giving up the ghost. I yell, "Clear", jam the power cable back in as painfully as possible and here we are, all of us with a better understanding of the pecking order. And then I removed the startup item LG installed ("forte display manager") to keep it from doing it's infinite loop dance with NVidia for control of the display.

So, the public service announcement: if you get a new wide-screen LG monitor, get a DVI cable with it. Hook them up. Don't install the LG software (though you'll most likely need the drivers). I suppose if you just have one monitor, you'll be fine either way, but you'll only find this post if something goes wrong.
