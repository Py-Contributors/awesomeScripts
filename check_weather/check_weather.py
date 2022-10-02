import os
import requests
import pprint
from dotenv import load_dotenv
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-c", "--city", required=True, help="City name")
args = vars(arg.parse_args())


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
    
    city_name = args["city"]
    response = get_city_weather(city_name)
    pprint.pprint(response)
