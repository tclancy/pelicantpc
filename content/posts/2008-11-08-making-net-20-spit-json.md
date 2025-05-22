Title: Making .NET 2.0 Spit JSON
Slug: making-net-20-spit-json
Date: 2008-11-08 09:56:23
Tags: 
Category: Posts
Author: Tom Clancy

# Making .NET 2.0 Spit JSON

I just finished translating a set of PHP web services into C# for a national car insurer and came across two things worth mentioning, if only for my future reference.

Each service needed an XML and a JSON version. I knew I didn't want to write code to hand-roll duplicate sets of responses, but I also didn't think it was worth knocking up a formatter class for two response formats. I created the XML responses and decided I'd transform them to JSON via XSL. Just before I got started on that, I remembered anything halfway smart I think of has already been done. Thus, <a href="http://code.google.com/p/xml2json-xslt/" target="_blank">xml2json</a>.

Sinfully proud of myself, I wired up the JSON responses and pointed the pre-existing test site at my new services. And: nothing. Knowing I'm perfect, I fiddled with the site's JavaScript for an embarrassingly long time before looking at the output of my JSON services. I'd created a bunch of web services that returned a string type and the JSON looked gorgeous in the unit tests, so where was the problem? Oh yeah:
<pre lang="xml">
<string>{json:"help, i'm trapped in here"}</string></pre>
There's a lot I love about .NET's web services, mainly how the busywork is taken care of behind the scenes. Except there's no easy way to get back there and change the plumbing (to mix a metaphor) so it spits out strings instead of XML. .NET 3.5 has native JSON serialization, but this had to be 2.0-compatible. I found a <a href="http://delicious.com/yerfatma/json+dotnet" target="_blank">number of possible solutions</a>, most of which relied on the <a href="http://www.asp.net/ajax/ajaxcontroltoolkit/samples/" target="_blank">Ajax toolkit</a>. Having worked with it, I have two objections to the toolkit:
<ol>
	<li>It's really heavy, so you'd better need it</li>
	<li>It feels like black magic: include the proper fake files, say the incantations just right, things may work</li>
</ol>
The toolkit was too much of an elephant gun for this ant. But the alternative was to create my own custom response handler, which felt both egotistical and like a good way to make a mess. While weighing the various options, all of them ugly, it hit me:
<pre lang="csharp">
[WebMethod]
public void MyJSONService()
{
  Context.Response.Write(myJsonString);
  Context.Response.Flush();
  Context.Response.End();
}</pre>
A hack can be something that works even though you don't understand it, something you do because you're too lazy to do it correctly or something less than beautiful that solves the problem with a minimum of fuss. I'd like to think this was a #3. It's not ideal and it's not a good solution for a large system, but if you're just trying to get .NET 2.0 to send back strings without it wrapping everything in an XML safety envelope, this works without requiring two tons of library or chicken blood + a full moon.
