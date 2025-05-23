#!/usr/bin/env python

import logging
import os
import re
import sys

import mysql.connector

logger = logging.getLogger(__name__)

PAGE_TEMPLATE = """Title: %(title)s
Slug: %(slug)s
Date: %(date)s
Tags: %(tags)s
Category: Posts
Author: Tom Clancy

# %(title)s

%(content)s
"""

def sanitize_title(title: str) -> str:
    """
    Not sure if I need to escape or not. Without escaping, pelican content shows
    
    smartypants.py:271: SyntaxWarning: invalid escape sequence '\S'
    if re.match("\S", prev_token_last_char):
    smartypants.py:277: SyntaxWarning: invalid escape sequence '\S'
    if re.match("\S", prev_token_last_char):

    but does not die as best I can tell.
    """
    return title
    # return title.replace('"', r'\"')

def sanitize_content(content: str) -> str:
    """
    Kinda, sorta deal with Django tags which break Jekyll
    Handle references to media as best we can (or not, they're fairly rare)
    oEmbed if we can find and config something that works
    :param content:
    :return:
    """
    content = re.sub(r"{%\s+(\w+)\s+%}", r"\1", content)
    return content

def repath_images(content: str) -> str:
    """
    Change some paths to pelican-friendly ones
    """
    # literally one post
    content = content.replace("/static/thoughts", "/images/legacy")
    content = content.replace("http://tkc.webfactional.com/blog/wp-content/uploads", "/images/wordpress")
    return content

def get_posts():
    try:
        conn = mysql.connector.connect(user=os.environ["MYSQL_USER"], password=os.environ["MYSQL_PASS"],
                                       host="127.0.0.1", database="tkc2")
    except mysql.connector.Error:
        logger.exception("Error connecting to MySQL database")
        sys.exit(1)
    cursor = conn.cursor()
    cursor.execute("SELECT name, slug, content, publish_date, tags, type_id FROM thoughts_post WHERE active = 1")
    for (name, slug, content, publish_date, tags, type_id) in cursor:
        filename = f"content/posts/{publish_date.strftime('%Y-%m-%d')}-{slug}.md"
        with open(filename, "w") as f:
            f.write(PAGE_TEMPLATE % {
                "title": sanitize_title(name),
                "content": sanitize_content(repath_images(content)),
                "tags": ",".join(tags.split()),
                "date": publish_date,
                "slug": slug,
            }
        )
    cursor.close()
    conn.close()


if __name__ == "__main__":
    get_posts()