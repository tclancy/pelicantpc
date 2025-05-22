Title: Progressive Insurance: Progressive API Conversion
Slug: progressive-api-conversion
Tags: csharp,php,api,conversion,documentation,nunit,tdd
Category: Portfolio
Date: 2008-11-06
Author: Tom Clancy
Url: progressive-api-conversion

# Progressive Insurance: Progressive API Conversion

## 2008-11-06

_Took an existing API concept written in PHP, converted it to C#, polished some of the rough edges and documented._

<p>Progressive had a proof-of-concept API for insurance price quotes written in PHP. They wanted it converted to C# for better client compatibility; the API was designed to be installed locally on customer web servers so they can integrate insurance quotes into their sites. The API needed to deliver results in both XML and JSON formats. The final deliverable included four .NET projects: the main web services solution, the class library, a web site project with front-end templates that consume the various services as a reference for client customization and a unit test project (using NUnit) as a way of checking the server was set up properly. In addition, I provided documentation on how to set up the projects and a CHM file documenting the code.</p>

<p>One challenge I encountered: while the only differences between the JSON and XML web services was the format of the code (internally they both use the same function and translate the XML into JSON via XSL if needed), .NET 2.0 insists all web services reply in XML. Newer versions make it easy to overcome this, but getting rid of the XML tags in 2.0 is torturous enough I felt it <a href="http://www.thosecleverkids.com/blog/2008/11/08/making-net-20-spit-json/">called for a good hack.</a></p>
