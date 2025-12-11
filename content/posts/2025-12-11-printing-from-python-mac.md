Title: Printing from Python on a Mac
Slug: printing-from-python-mac
Date: 2025-12-11
Tags: python,coding
Category: Posts
Author: Tom Clancy

# Printing from Python on a Mac

I recently automated the download of one of my favorite cryptic crosswords,
both because I am nerdy and because it went behind an extravagantly high paywall.
In the process I decided I wanted Sunday mornings to be even more leisurely and
made the script print the PDF after downloading, thusly:

```python
import os
import logging
import sys
from pathlib import Path

import requests

logger = logging.getLogger(__name__)

PATH_TO_WRITE = Path("/your/file/location.pdf")
# download stuff elided for brevity

def print_pdf_from_link(pdf_link: str | None, write_to: Path = PATH_TO_WRITE):
    if not pdf_link:
        logger.error("No PDF link provided, exiting")
        sys.exit(1)
    pdf_request = requests.get(pdf_link)
    with open(write_to, "wb") as f:
        f.write(pdf_request.content)
    os.system(f"lpr -P Brother_MFC_L2750DW_series {write_to}")
    write_to.unlink()
    write_to.with_suffix(".ps").unlink()
```

The only trick is getting the name of the printer (`Brother_MFC_L2750DW_series` here) from your
machine. You can get that with `lpstat -p`. The weird side effect is you wind up with two files,
one with the `.ps` printer extension and one with the `.pdf` extension. Rather than figure out
why, I am just stomping on it at the same time, which showed me `pathlib` has that neat little
`with_suffix` method.
