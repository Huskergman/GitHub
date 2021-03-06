#import the beautiful soup and scraping tools.
from fileinput import filename
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

#assign the variables you want here
#this will put it in an array for us to loop through
variable_name = html_soup.find_all('', class_="")

#to write to a file, we are choosing a CSV file
filename = 'filename.csv'

#to open a file with write permissions
f = open(filename, 'w')

#creating headers for our CSV file, I went with the title and 
#price. \n to create a new line in the CSV
headers = 'Title, Price \n'

#we want to write the headers here
f.write(headers)

#loop to iterate through our array
#we would want to write our headers in the loop as well

###Example###
#for cactus in cactus_items:
#   title = cactus.find('div', class_="grid-product_title").text
#   title = cactus.find('div', class_="grid-product_price").text
#   f.write(title + ',' + price)
#we want the ',' for this since we are exporting to a CSV file

#lastly we want to close the file
f.close()