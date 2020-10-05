import requests

waqi_url = "https://api.waqi.info"  # air quality index url

token = "9dfef5c5dda118ed1b5d5c53dd20c6c77b1f1b2b"  # api access token

while (True):

    city = input("Enter the city: ")

    # get request to the air quality index website with the selected city
    response = requests.get(waqi_url + f"/feed/{city}/?token={token}")

    try:

        # output result
        print("City: {}, Air quality index: {}".format(
            response.json()['data']['city']['name'],
            response.json()['data']['aqi'])
        )

    # catch if the city is not found
    except TypeError:
        print("Make sure your input is correct!")
