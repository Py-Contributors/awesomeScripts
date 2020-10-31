"""This script allows us to see the most popular movies on yts.mx
    - Most popular movies
    - Latest uploads
    - Upcoming movies
    The script uses BeautifylSoup to scrap data from the website.
"""

import requests
from bs4 import BeautifulSoup


title = f"""
\t {'-' * 80}
\t {'YTS.mx Top Movies':^80}
\t {'-' * 80}
\t {'By: chemsedd':^80}
\t {'-' * 80}
"""

print(title)

# YTS website
url = 'https://yts.mx/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0)\
        Gecko/20100101\
        Firefox/79.0'
}
# Request web page
page = requests.get(url, headers=headers)
# parse to html
soup = BeautifulSoup(page.content, 'html.parser')
# top movies titles
top_movies_title = soup.find_all('a', class_='browse-movie-title')
# top movies years
top_movies_year = soup.find_all('div', class_='browse-movie-year')
movies_list = zip(top_movies_title, top_movies_year)
#
# Popular downloads
for index, movie in enumerate(movies_list):
    if index == 0:
        print('\t\n', '\t Popular Downloads:', '\n\t', '-' * 80)
    elif index == 4:
        print('\t\n', '\t Latest Movies:', '\n\t', '-' * 80)
    elif index == 12:
        print('\t\n', '\t Upcoming Movies:', '\n\t', '-' * 80)
    title, year = movie
    link = title.attrs['href']
    title = title.contents[-1].strip()
    year = year.contents[0].strip('\n')
    print(f"\t {index + 1:02} - {title:30} ({year}) >> {link}")
