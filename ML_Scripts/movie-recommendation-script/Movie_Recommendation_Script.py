# Python3 code for movie recommendation based on emotion
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP


def main(emotion):

    if (emotion == "sad"):
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    # movie against emotion Disgust
    elif (emotion == "disgust"):
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
    # IMDb Url for Family genre of
    # movie against emotion Anger
    elif (emotion == "anger"):
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
    # IMDb Url for Thriller genre of
    # movie against emotion Anticipation
    elif (emotion == "anticipation"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    # IMDb Url for Sport genre of
    # movie against emotion Fear
    elif (emotion == "fear"):
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
    # IMDb Url for Thriller genre of
    # movie against emotion Enjoyment
    elif (emotion == "enjoyment"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    # IMDb Url for Western genre of
    # movie against emotion Trust
    elif (emotion == "trust"):
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
    # IMDb Url for Film_noir genre of
    # movie against emotion Surprise
    elif (emotion == "surprise"):
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
    # HTTP request to get the data of
    # the whole page
    response = HTTP.get(urlhere)
    data = response.text
    # Parsing the data using
    # BeautifulSoup
    soup = SOUP(data, "lxml")
    # Extract movie titles from the
    # data using regex
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    return title


# Driver Function
if __name__ == '__main__':

    emotion = input("Enter the emotion: ")
    a = main(emotion)
    count = 0
    if (emotion == "disgust" or emotion == "anger" or emotion == "surprise"):
        for i in a:
            # Splitting each line of the IMDb data to scrape movies
            tmp = str(i).split('>;')

            if (len(tmp) == 3):
                print(tmp[1][:-3])

            if (count > 13):
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split('>')

            if (len(tmp) == 3):
                print(tmp[1][:-3])

            if (count > 11):
                break
            count += 1
