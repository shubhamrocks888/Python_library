import requests
from bs4 import BeautifulSoup

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source,'lxml')


articles = soup.find_all('article')


##Self-made method:
for article in articles:
    title  = article.find('h2',class_="entry-title")
    summary = article.find('div',class_="entry-content")
    print (title.text)
    print (summary.text)

    try:
        src = article.find('iframe')['src'].split("/")
#Example of src:https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent 
        j=0
        for i in src:
            
            if i=='?':
                break
            j+=1
        
        link = src[2]+"/watch?v="+src[4][:j]

   
        print (link)

    except:
        pass
   
    print ("------------")

##Corey method:
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()




##Output:
Python Tutorial: Zip Files – Creating and Extracting Zip Archives

In this video, we will be learning how to create and extract zip archives.
We will start by using the zipfile module, and then we will see how to do
this using the shutil module. We will learn how to do this with single files
and directories, as well as learning how to use gzip as well. Let’s get startedâ€¦


www.youtube.com/watch?v=z0ggu
------------
Python Data Science Tutorial: Analyzing the 2019 Stack Overflow Developer Survey

In this Python Programming video, we will be learning how to download and analyze
real-world data from the 2019 Stack Overflow Developer Survey. This is terrific
practice for anyone getting into the data science field. We will learn different
ways to analyze this data and also some best practices. Let’s get startedâ€¦

..........


www.youtube.com/watch?v=_P7X8
------------    
