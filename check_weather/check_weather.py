import os
import sys
import requests
import pprint
from dotenv import load_dotenv


def get_city_weather(city_name):
    """
    Uses Open Weather Map API to fetch Current Weather Details of a Given City
    """
    load_dotenv()
    # Not Setting Up API Key will respond with a 401 Error Code and Invalid
    # API Key message
    OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
    URL = (
        f'http://api.openweathermap.org/data/2.5/weather?'
        f'q={city_name}&appid={OPEN_WEATHER_API_KEY}'
    )
    response = requests.get(URL).json()
    return response


if __name__ == "__main__":
    try:
        city_name = sys.argv[1]
    except Exception:
        print("Please Enter The City Name as a Command-Line Argument!")
        exit(0)
    response = get_city_weather(city_name)
    pprint.pprint(response)
