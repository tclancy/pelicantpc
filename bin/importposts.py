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
    return title.replace('"', r'\"')

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
                "content": sanitize_content(content),
                "tags": ",".join(tags.split()),
                "date": publish_date,
                "slug": slug,
            }
        )
    cursor.close()
    conn.close()


if __name__ == "__main__":
    get_posts()