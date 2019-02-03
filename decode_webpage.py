## Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

## Python library for HTTP
import requests  
from bs4 import BeautifulSoup
import ssl


# request a webpage:
url = input('Enter a url: ')
r = requests.get(url)  
# r is a Response object

# convert content to something we can read/parse:
string_html = r.text

# BeautifulSoup object with nested data structure
parsed_html = BeautifulSoup(string_html,'html.parser')
print(parsed_html.prettify())

# retrieve first instanct of h1 tag:
title = parsed_html.find('h1')

# retrieve a list of all h1 tags:
#title = parsed_html.find_all('h1')
#print(title)

#for tag in title:
    #print(tag)
