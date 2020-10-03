# Title :- URL Shortener
# The URL shortener is application which takes url input from user and shorts it

# import pyshorteners module

import pyshorteners

# Taking url input from user
url = input('Please Enter the URL:-')
shorturl = pyshorteners.Shortener().tinyurl.short(url)

# displaying the shorted url
print('The URL after shortening is :-', shorturl)
