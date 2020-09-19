import requests
from bs4 import BeautifulSoup

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')
    # lxml is a parser like html5lib

#similar to r.text
print (soup)


<!DOCTYPE html>
<html class="no-js" lang="">
<head>
<title>Test - A Sample Website</title>
<meta charset="utf-8"/>
<link href="css/normalize.css" rel="stylesheet"/>
<link href="css/main.css" rel="stylesheet"/>
</head>
<body>
<h1 id="site_title">Test Website</h1>
<hr/>
<div class="article">
<h2><a href="article_1.html">Article 1 Headline</a></h2>
<p>This is a summary of article 1</p>
</div>
<hr/>
<div class="article">
<h2><a href="article_2.html">Article 2 Headline</a></h2>
<p>This is a summary of article 2</p>
</div>
<hr/>
<div class="footer">
<p>Footer Information</p>
</div>
<script src="js/vendor/modernizr-3.5.0.min.js"></script>
<script src="js/plugins.js"></script>
<script src="js/main.js"></script>
</body>
</html>


#for proper indentation
print (soup.prettify())


<!DOCTYPE html>
<html class="no-js" lang="">
 <head>
  <title>
   Test - A Sample Website
  </title>
  <meta charset="utf-8"/>
  <link href="css/normalize.css" rel="stylesheet"/>
  <link href="css/main.css" rel="stylesheet"/>
 </head>
 <body>
  <h1 id="site_title">
   Test Website
  </h1>
  <hr/>
  <div class="article">
   <h2>
    <a href="article_1.html">
     Article 1 Headline
    </a>
   </h2>
   <p>
    This is a summary of article 1
   </p>
  </div>
  <hr/>
  <div class="article">
   <h2>
    <a href="article_2.html">
     Article 2 Headline
    </a>
   </h2>
   <p>
    This is a summary of article 2
   </p>
  </div>
  <hr/>
  <div class="footer">
   <p>
    Footer Information
   </p>
  </div>
  <script src="js/vendor/modernizr-3.5.0.min.js">
  </script>
  <script src="js/plugins.js">
  </script>
  <script src="js/main.js">
  </script>
 </body>
</html>

    ##To print the tag
    ##basically tag is acting like a attribute for soup object
    ##soup object has only one attribute i.e, tags.

match = soup.title
print (match)
#Output:
<title>Test - A Sample Website</title>

print (type(match))
<class 'bs4.element.Tag'>

match = soup.head
print (match)
#Output:
<head>
<title>Test - A Sample Website</title>
<meta charset="utf-8"/>
<link href="css/normalize.css" rel="stylesheet"/>
<link href="css/main.css" rel="stylesheet"/>
</head>


    ##NOTE: for example,if we have many tags of same name,then it will print the only first one like script.

match = soup.script
print (match)
#Output:
<script src="js/vendor/modernizr-3.5.0.min.js"></script>

'NOTE':If you want to access the attribute under tag,u can access them just like a dictionary

print (match['src'])
#Output:
js/vendor/modernizr-3.5.0.min.js


    #To print the text of tags

match = soup.title.text
print (match)
#Output:        
Test - A Sample Website

                                    #####soup.find()

It is noticed that all the quotes are inside a div container whose id is ‘all_quotes’.
So, we find that div element (termed as table in above code) using find() method :

->table = soup.find('div', attrs = {'id':'all_quotes'})


##
match = soup.find('div')
print (match)
#It will print the first div
<div class="article">
<h2><a href="article_1.html">Article 1 Headline</a></h2>
<p>This is a summary of article 1</p>
</div>

    ##To print the div of class footer

match = soup.find('div',class_='footer')
#class is a keyword,thatswhy we use class_
print (match)
#Output:
<div class="footer">
<p>Footer Information</p>
</div>

            ##Use of soup.find()
#Print out the first article
article = soup.find('div',class_="article")
print (article)

#Output:
<div class="article">
<h2><a href="article_1.html">Article 1 Headline</a></h2>
<p>This is a summary of article 1</p>
</div>

#print out the first article's h2 tag
article = soup.find('div',class_="article")
print (article.h2)

#Output:
<h2><a href="article_1.html">Article 1 Headline</a></h2>

#print out the first article's h2 tag's anchor tag
article = soup.find('div',class_="article")
print (article.h2.a)

#Output:
<a href="article_1.html">Article 1 Headline</a>


#print out the first article's h2 tag's anchor tag's text
article = soup.find('div',class_="article")
print (article.h2.a.text)

#Output:
Article 1 Headline

#print out the first article whole text

article = soup.find('div',class_="article")
print (article.text)

#Output:
Article 1 Headline
This is a summary of article 1

    #Want to scrape first article's headline and summary of the page

article = soup.find('div',class_='article')

headline = article.h2.a.text
summary  = article.p.text

print (headline)
print (summary)

#Output:
Article 1 Headline
This is a summary of article 1


                        ######soup.find_all()
-> It basically gives the list of all the tags that we wanna looking for.

article = soup.find_all('div',class_='article')
print (article)

#Output:
[
    <div class="article">
    <h2><a href="article_1.html">Article 1 Headline</a></h2>
    <p>This is a summary of article 1</p>
    </div> ,
    <div class="article">
    <h2><a href="article_2.html">Article 2 Headline</a></h2>
    <p>This is a summary of article 2</p>
    </div>
]

    ### Want to get all the articles headline and summary

articles = soup.find_all('div',class_='article')

for article in articles:
    headline = article.h2.a.text
    summary  = article.p.text

    print (headline)
    print (summary)

#Output:
Article 1 Headline
This is a summary of article 1
Article 2 Headline
This is a summary of article 2











