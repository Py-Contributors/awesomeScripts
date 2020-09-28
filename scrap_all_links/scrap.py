import httplib2
from bs4 import BeautifulSoup, SoupStrainer

# args handling
# pretty print scraped links

http = httplib2.Http()
status, response = http.request('http://google.com/')

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        print(link['href'])