Title: PHP Excel Exporter
Slug: php-excel-exporter
Date: 2009-02-23 21:06:54
Tags: 
Category: Posts
Author: Tom Clancy

# PHP Excel Exporter

A few times a year a client needs to export something from a database table to Excel. There's a simple hack to do it in most any language. There are actually a few, but having come up as a web developer, my preferred trick is to just build an HTML table and serve it as Excel by setting the mime type header. Having done this dozens of times, I finally formalized this into a simple PHP class tonight to save myself some time and figured I might as well share it.

The bad news: because I am lazy, it relies on an old data connection class I wrote years ago when I was even less bright than I am now. The thing's so ugly I posted it <a href="http://snipplr.com/view/12517/php-mysql-data-connection-class/">somewhere else</a> because I am too ashamed to host it here. You can rip that out and use whatever you prefer by just changing the logic in _get_table() below. If you do choose to use my old data-class.php, be aware it expects 4 constants, DB_SERVER, DB_USER, DB_USER_PASS, DB_NAME to create a connection to the database.

<strike>Here's the exporter code itself</strike> Update: I moved the <a href="http://snipplr.com/view/12519/excel-exporter/">code to snipplr</a> because this Wordpress plugin doesn't handle newline characters very well.

The simplest use is to instantiate an object, tell the exporter what you want to appear in the header row in the spreadsheet (by setting column_heads to an array of values) and then calling export(), passing it the SQL query that gets the data. If the number of fields in your query doesn't match the number of heads in column_heads, the resulting HTML will be a mess. You will understand if the code assumes you never make such mistakes. Here's a code example:

<pre lang="php">
$e = new ExcelExporter();
$e->column_heads = array("First Name", "Last Name");
echo $e->export("SELECT first_name, last_name FROM table");
</pre>

Quick notes:
<ul>
<li>Control the Excel filename in my example by setting $e->filename("something-else.xls")</li>
<li>Add a timestamp to every file (useful for making sure the filename is always unique) by setting $e->timestamp_file = true</li>
<li>When you're trying to implement this and it's not working and having to say yes to the popup and let the file open in Excel is driving you crazy, set $e->debug = true and it will skip the Excel headers, sending the output to the browser</li>
</ul>

The big gotcha that works well for me but might not for you: there's a hook in the code that passes every data column through _format_field(). In my current class, this looks for any field with "_date" in the column name, assumes that field is a <a href="http://www.unixtimestamp.com/index.php">Unix timestamp</a> and transforms the value into a m/d/y date. If you live in the other 99% of the world where people format their dates un-Americanly, well, you can do that like this: $e->date_format("d/m/y") or whatever other crazy date/ time format you like.

If you think that behavior stinks, rip it out. Alternatively, you can modify it or subclass this code (like "client-xyz-exporter extends ExcelExporter" for every client who lives in Excel) and change _format_field() to do whatever you want in a one-off sort of way. This is not high art, it's just a faster way of making someone happy (if you can imagine the kind of person whose life is improved by additional spreadsheets).
