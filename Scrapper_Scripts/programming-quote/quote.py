import requests


def fetch_data(url):
    r = requests.get(url)
    if r.status_code == 200:
        data = r.text
        return data
    else:
        print("Something is wrong with API.")


def save_data(url):
    data = fetch_data(url)
    with open("programming-quote/quote.json", "w") as file:
        file.write(data)


if __name__ == "__main__":
    url = "https://programming-quotes-api.herokuapp.com/quotes/lang/en"
    save_data(url)
