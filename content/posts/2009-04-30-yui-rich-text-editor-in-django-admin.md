Title: YUI Rich Text Editor in Django Admin
Slug: yui-rich-text-editor-in-django-admin
Date: 2009-04-30 16:49:23
Tags: 
Category: Posts
Author: Tom Clancy

# YUI Rich Text Editor in Django Admin

This ain't exactly rocket science, but it took me an embarrassing amount of time to get there, so I'm posting the code for next time. This will turn a given textarea in your admin area into a WYSIWYG. It's got a fairly small feature set, but that's only because I've stripped most of them out. You can add them back in by <a href="http://developer.yahoo.com/yui/editor/">taking a look at the documentation</a>. Per the <a href="http://docs.djangoproject.com/en/dev/ref/contrib/admin/#overriding-admin-templates">Django docs</a>, create an admin folder under one of your templates directories, then add subfolders for the app and model (though you can do just one if you want it to apply to all forms in the app or do neither to apply to all apps and models in your site) and add this as "change_form.html" (it took me an extra 10 minutes to get this done because I was sure it should be named "change_form.py" in spite of copious amounts of documentation that said otherwise):

```
{% extends "admin/change_form.html" %}

{% block extrahead %}{{ block.super }}
<!-- Skin CSS file -->
<link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/2.5.1/build/assets/skins/sam/skin.css">
<!-- Utility Dependencies -->
<script type="text/javascript" src="http://yui.yahooapis.com/2.5.1/build/yahoo-dom-event/yahoo-dom-event.js"></script>
<script type="text/javascript" src="http://yui.yahooapis.com/2.5.1/build/element/element-beta-min.js"></script>
<!-- Needed for Menus, Buttons and Overlays used in the Toolbar -->
<script src="http://yui.yahooapis.com/2.5.1/build/container/container_core-min.js"></script>
<script type="text/javascript" src="http://yui.yahooapis.com/2.5.1/build/menu/menu-min.js"></script>
<script type="text/javascript" src="http://yui.yahooapis.com/2.5.1/build/button/button-min.js"></script>
<!-- Source file for Rich Text Editor-->
<script src="http://yui.yahooapis.com/2.5.1/build/editor/editor-beta-min.js"></script>
<script type="text/javascript">
		// YUI editor
		var editor = new YAHOO.widget.Editor("id_content", {
			handleSubmit: true,
			toolbar: {
        buttonType: 'advanced',
        buttons: [
            { group: 'fontstyle', label: 'Font',
                buttons: [
                    { type: 'select', label: 'Arial', value: 'fontname',
disabled: true,
                        menu: [
                            { text: 'Arial', checked: true },
                            { text: 'Verdana' }
                        ]
                    },
                    { type: 'spin', label: '10', value: 'fontsize', range: [
10, 16 ], disabled: true },
					{ type: 'color', label: 'Font Color', value: 'forecolor', disabled: true }
                ]
            },
            { type: 'separator' },
            { group: 'textstyle', label: 'Font Style',
                buttons: [
                    { type: 'push', label: 'Bold CTRL + SHIFT + B', value: 'bold' },
                    { type: 'push', label: 'Italic CTRL + SHIFT + I', value: 'italic' },
					{ type: 'push', label: 'Underline CTRL + SHIFT + U', value: 'underline' }
                ]
            },
			{ type: 'separator' },
            { group: 'indentlist', label: 'Indenting and Lists',
                buttons: [
                    { type: 'push', label: 'Indent', value: 'indent',
disabled: true },
                    { type: 'push', label: 'Outdent', value: 'outdent',
disabled: true },
                    { type: 'push', label: 'Create a Bulleted List', value:
'insertunorderedlist' },
                    { type: 'push', label: 'Create a Numbered List', value:
'insertorderedlist' }
                ]
            },
            { type: 'separator' },
            { group: 'insertitem', label: 'Link',
                buttons: [
                    { type: 'push', label: 'HTML Link CTRL + SHIFT + L',
value: 'createlink', disabled: true }
                ]
            }
        ]
}
			}
			);
		editor._defaultToolbar.buttonType = 'advanced';
		editor.render();
</script>
endblock

{% block bodyclass %}{{ block.super }} yui-skin-samendblock
```

Like I said, not rocket science. It adds some CSS & JavaScript includes (which are remotely-hosted, so you don't even have to worry about media roots or how it works locally vs. live) and then a bit to add a class to the body tag for the YUI skin.
