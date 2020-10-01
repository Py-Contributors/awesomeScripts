import re
import sys
import requests

url = sys.argv[1]

website = requests.get(url)
html = website.text

emails = re.findall(r"[\w\.-]+@[\w\.-]+", html)

print(emails)
