# City Weather

Get The Weather Of Your City using Python CLI.

## Pre-Requisites

- Open Weather API Key. You can get the API Key by creating an account at https://openweathermap.org/

## Instructions

- Run the command `pip install -r requirements.txt` to install the required dependencies.

- Create a .env file at the check_weather root directory and add the line

`OPEN_WEATHER_API_KEY = {YOUR-OPEN-WEATHER-API-KEY-GOES-HERE}`

- Run the program with command-line arguments

`python check_weather.py {city_name}` or `python check_weather {city_name}`

depending on your system to get the weather details of that particular city.