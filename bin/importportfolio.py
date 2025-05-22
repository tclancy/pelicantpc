#!/usr/bin/env python

import logging
import os
import sys

import mysql.connector

logger = logging.getLogger(__name__)

PAGE_TEMPLATE = """Title: %(title)s
Slug: %(slug)s
Tags: %(tags)s
Category: Portfolio
Date: %(date)s
Author: Tom Clancy

# %(title)s

## %(date)s

%(summary)s

%(content)s
"""

def get_projects():
    try:
        conn = mysql.connector.connect(user=os.environ["MYSQL_USER"], password=os.environ["MYSQL_PASS"],
                                       host="127.0.0.1", database="tkc2")
    except mysql.connector.Error:
        logger.exception("Error connecting to MySQL database")
        sys.exit(1)
    cursor = conn.cursor()
    cursor.execute("""SELECT j.id, c.name, j.name, j.slug, j.summary, j.description, j.tags, j.date_completed
FROM portfolio_job j
INNER JOIN portfolio_company c ON j.company_id = c.id 
WHERE j.description <> '<p>x</p>'
ORDER BY j.date_completed;""")
    for (job_id, company, project, slug, summary, description, tags, date_completed) in cursor:
        title = f"{company}: {project}"
        print_summary = ""
        if summary:
            print_summary = f"_{summary}_"
        filename = f"content/portfolio/{slug}.md"
        description += get_images(job_id)
        with open(filename, "w") as f:
            f.write(PAGE_TEMPLATE % {
                "title": title,
                "summary": print_summary,
                "tags": ",".join(tags.split()),
                "date": date_completed,
                "content": description,
                "slug": slug,
            })
    cursor.close()
    conn.close()

def get_images(job_id: int) -> str:
    """
    Are there nicer ways to do this? Sure, but let's try this first
    """
    conn = mysql.connector.connect(user=os.environ["MYSQL_USER"], password=os.environ["MYSQL_PASS"],
                                   host="127.0.0.1", database="tkc2")
    cursor = conn.cursor()
    cursor.execute("SELECT name, description, screenshot FROM portfolio_jobimage WHERE job_id = %s",
                   (job_id,))
    output = ""
    for (name, description, screenshot) in cursor:
        img_url = screenshot.replace("img/", "/images/")
        description = description.replace('"', "'")
        output += f'<img src="{img_url}" alt="{name} {description}" style="margin: 1em 0" />\n'
    cursor.close()
    return output


if __name__ == "__main__":
    get_projects()
