Title: Fidelity: Broker Information Site
Slug: broker-information-site
Tags: expressionengine,xml,pgp,gpg,encryption,pdf,jquery,php,python
Category: Portfolio
Date: 2010-03-01
Author: Tom Clancy
Url: broker-information-site

# Fidelity: Broker Information Site

## 2010-03-01

_Private web site that brings encrypted XML data about funds into Expression Engine which displays the information in HTML and PDF formats._

<p><em>A massive undertaking in three parts</em></p>
<h2>Fund Information</h2>
<p>This client has a large mutual fund business with a number of channels they sell the funds through. One of those channels asked Slim Kiwi to build a site that would provide news and fund information to their brokers. The site is built on Expression Engine and servers a number of "normal" content pages. The rest of the site consists of fund information in a custom Expression Engine channel. The information comes from the parent company's IT department as a set of PGP-encrypted XML files sent twice quarterly (once at the start of a new quarter and a second delivery later in the month when the fund commentary for the previous quarter has been written). The files belong to three groups (fund, benchmark, Morningstar) and then broken down by category, not by fund, so the information for each fund is split across all files.&nbsp;</p>
<p>Once the funds have been delivered, a series of Python scripts go to work. The first decrypts the data and then kicks off the parsing process. Each group (fund, benchmark, Morningstar) has a parser that inherits common functionality from a parent class. Distilling a lot of detail into a simple statement, the goal of each parser is to consume a great deal of deeply-structured XML data to find the elements we are interested in and then write that information into a flattened form we can bring into Expression Engine with one entry per fund/ benchmark/ category. In the interests of simplicity and to make it easier for less technical personnel to update what information gets consumed, all three parsers get their marching orders from a single file. The file consists of simple Python dictionaries mapping our labels to where they live in the XML files. Add a new line and it's available in Expression Engine the next time the parser runs. Remove an entry and the information gets dropped.</p>
<p>Once the fund information is in place, the site presents the data as a modern version of the fund prospectus guides that get mailed out. Users can customize the interface to focus on the data they care about: panels can be re-arranged or hidden to make funds easier to read at a glance. The site also remembers user preferences so they only have to customize the interface once.</p>
<h2>Document Packages</h2>
<p>Each fund also has three documents associated with it (two PDFs and one Excel file) that are updated on a quarterly basis. While all of the documents are available on the front of the site, brokers want to be able to get their customers just the documents they're interested in and only for the funds a given customer has. The site allows brokers to define sets of documents and receive them as a single zip file (generated on-the-fly by some PHP code). For further convenience, brokers can name the sets of documents (e.g., "Customer X Reports") so they can come back each quarter and get the updated versions of the same set of documents for delivery to their client.</p>
<h2>PDF Generation</h2>
<p>Victims of our own success, the client began comparing the pretty HTML pages we were generating to the PDF versions they had to build by hand each quarter (one of the three documents we provide per-fund). The final piece of this project was to start generating those PDFs on the fly. The process works much like the HTML version: Expression Engine provides the information about a fund and we change it into the format we want. The only difference is that the HTML version creates its content by transforming the XML via XSL whereas the PDF process sends the information to a PHP file that uses <a href="http://www.pdflib.com/" target="_blank">PDFLib</a> to generate the files. In the interests of full disclosure, if I had to do this again, it would not be with PDFLib. It was difficult to work with, hard to debug, hard to manage the licenses on the server and you have to pay for the privilege of suffering through all that. It's a lot more painful than the PDF solutions I've used in Python and there seem to be a number of better options out there.</p><img src="/images/portfolio/fund-matrix.png" alt="Fund Matrix Overview 'matrix' of funds and their related documents" style="margin: 1em 0" />
<img src="/images/portfolio/fund-detail.png" alt="Fund Detail One of the five screens of fund data, showing the ability to collapse and re-arrange panels" style="margin: 1em 0" />
<img src="/images/portfolio/fund-downloads.png" alt="Saved Downloads The 'shopping cart' of saved zip file collections. Please note the brilliant and original names I use during testing." style="margin: 1em 0" />

