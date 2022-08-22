# https://www.youtube.com/watch?v=zo7yzIVpIJo

from bs4 import BeautifulSoup
import requests

#create a header 
headers = {'User-agent': 'Mozilla/5.0'}

#Requet the website 
request = requests.get('https://www.project-syndicate.org', headers=headers)
html = request.content

#Create some soup
soup = BeautifulSoup(html, 'html.parser')

#Used to easliy read the HTML that we scraped 
#print(soup.prettify())

def bbc_news_scraper(keyword):
    news_list = []

    #Find all the headers in BBC Home 
    for h in soup.findAll('h2'):
        news_title = h.contents[0].lower()
        if news_title not in news_list:
            if 'bbc' not in news_title:
                news_list.append(news_title)
    
    no_of_news = 0 
    keyword_list = []
    for i, title in enumerate(news_list):
        text = ''
        if keyword.lower() in title:
            text = " <--------------------------- KEYWORD"
            no_of_news += 1
            keyword_list.append(title)

        print (i +1, ':', title, text)
    
    print(f'\n ---------- Total mentions of "{keyword}" = {no_of_news} ----------')
    for i, title in enumerate(keyword_list):
        print(i+1, ":", title)

    
    #print(news_list)

bbc_news_scraper("us")

