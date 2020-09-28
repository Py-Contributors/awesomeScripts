import requests
from bs4 import BeautifulSoup, SoupStrainer

# args handling
# | pretty print scraped links
# |-> parse [done]

response = requests.get("https://gesco.bearzi.it/")

for link in BeautifulSoup(response.text, features="html.parser", parse_only=SoupStrainer('a')):
    if link.has_attr('href') and link['href'].startswith("http"):
        print(link['href'])