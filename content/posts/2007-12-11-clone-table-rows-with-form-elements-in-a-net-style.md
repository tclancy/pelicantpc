Title: Clone Table Rows with Form Elements in a .NET Style
Slug: clone-table-rows-with-form-elements-in-a-net-style
Date: 2007-12-11 09:50:19
Tags: 
Category: Posts
Author: Tom Clancy

# Clone Table Rows with Form Elements in a .NET Style

Using jQuery to coax .NET into cloning table rows with properly numbered id/ name attributes:

```
var MyNamespace = {
	init: function()
	{
		// attach row clone to passenger table
		$("table#tblPassengers tr:last :input").change(function() {MyNamespace.cloneRow("tblPassengers")});

		// attach row clone to contacts table
		$("table#tblContacts tr:last :input").change(function() {MyNamespace.cloneRow("tblContacts")});
	},

	cloneRow: function(sTableId)
	{
		var oRow = $("table#{0} tr:last :input".format(sTableId));
		oRow.unbind("change");

		var oNewRow = $("table#{0} tr:last".format(sTableId)).clone();

		$(":input", oNewRow).each(
			function ()
			{
				MyNamespace.cloneInput($(this));
			}
		);

		$("table#{0}".format(sTableId)).append(oNewRow);
		$("table#{0} tr:last :input".format(sTableId)).change(function() {Flights.cloneRow(sTableId)});
	},

	cloneInput: function(oInput)
	{
		oInput.val("");
		var oRegex = new RegExp(/[^"]ctl(\d+)/g);

		var sId = oInput.attr("id");
		oRegex.exec(sId);
		var iIdCount = parseInt(RegExp.$1[1]);
		var sFind = "ctl" + MyNamespace.padIntegerString(iIdCount, 2);
		var sReplace = "ctl" + MyNamespace.padIntegerString(++iIdCount, 2);
		oInput.attr("id", sId.replace(sFind, sReplace));
		oInput.attr("name", oInput.attr("name").replace(sFind, sReplace));
	},

	padIntegerString: function(iInt, iNumberOfCharacters)
	{
		var sTest = iInt + "";
		if (sTest.length &gt;= iNumberOfCharacters)
		{
			return sTest;
		}
		var sPad = "";
		for (var i = 0; i &lt; iNumberOfCharacters - 1; i++)
		{
			sPad += "0";
		}
		return sPad + iInt;
	},
};
```
