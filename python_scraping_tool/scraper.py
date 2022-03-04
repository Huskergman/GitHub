#import the beautiful soup and scraping tools.
from urllib.request import urlopen
from bs4 import BeautifulSoup

#url variable to scrape. 
url_to_scrape = ""

#headers are needed to scrape sites that give a 503 error 
#should be a simple google search on how to do this

#this retrieves the page, reading the information and closing 
#the request
request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

#this will allow us to pick through the html and use what we 
#want from it using beautiful soup and the html parser
html_soup = BeautifulSoup(page_html, 'html.parser')

#using the dev tools (f12) you can define variables of what 
#you want to grab from the site.
