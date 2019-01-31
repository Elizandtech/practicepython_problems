## Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

## Python library for HTTP
import requests  
from bs4 import BeautifulSoup
import ssl


# request a webpage:
r = requests.get('https://www.nytimes.com')  
# r is a Response object

# convert content to something we can read/parse:
string_html = r.text

parsed_html = BeautifulSoup(string_html, "html.parser")
title = parsed_html.find('span', 'articletitle').string
print(title)
