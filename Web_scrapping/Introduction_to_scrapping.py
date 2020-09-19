            ##Implementing Web Scraping in Python with BeautifulSoup

There are mainly two ways to extract data from a website:

->  Use the API of the website (if it exists).
    For example, Facebook has the Facebook Graph API which allows retrieval of data posted on Facebook.

->  Access the HTML of the webpage and extract useful information/data from it.
    This technique is called web scraping or web harvesting or web data extraction.
    This article discusses the steps involved in web scraping using the implementation of a Web Scraping
    framework of Python called Beautiful Soup.

    
This article discusses the steps involved in web scraping using the implementation of a Web Scraping-
framework of Python called Beautiful Soup.

'Steps involved in web scraping:'

->  Send an HTTP request to the URL of the webpage you want to access.
    The server responds to the request by returning the HTML content of the webpage.
    For this task, we will use a third-party HTTP library for python-requests.

->  Once we have accessed the HTML content, we are left with the task of parsing the data.
    Since most of the HTML data is nested, we cannot extract data simply through string processing.
    One needs a parser which can create a nested/tree structure of the HTML data.
    There are many HTML parser libraries available but the most advanced one is html5lib.

->  Now, all we need to do is navigating and searching the parse tree that we created, i.e. tree traversal.
    For this task, we will be using another third-party python library, Beautiful Soup.
    It is a Python library for pulling data out of HTML and XML files.


'Step 1: Installing the required third-party libraries'
Installing the required third-party libraries
->  pip install requests
->  pip install html5lib
->  pip install bs4


'Step 2: Accessing the HTML content from webpage'
import requests 
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL) 
print(r.content) 

Let us try to understand this piece of code.

First of all import the requests library.
Then, specify the URL of the webpage you want to scrape.
Send a HTTP request to the specified URL and save the response from server in a response object called r.
Now, as print r.content to get the raw HTML content of the webpage. It is of ‘string’ type.


'Step 3: Parsing the HTML content'
#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
print(soup.prettify()) 


A really nice thing about the BeautifulSoup library is that it is built on the top of the HTML parsing libraries like html5lib,
lxml, html.parser, etc. So  BeautifulSoup object and specify the parser library can be created at the same time.

In the example above,

##We create a BeautifulSoup object by passing two arguments:
soup = BeautifulSoup(r.content, 'html5lib')


r.content : It is the raw HTML content.
html5lib : Specifying the HTML parser we want to use.
Now soup.prettify() is printed, it gives the visual representation of the parse tree created from the raw HTML content.

