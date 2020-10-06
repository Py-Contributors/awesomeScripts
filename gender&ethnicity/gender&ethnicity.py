import requests


def main(url):
    data = requests.get(url).json()
    return data


def print_data(url):
    data = main(url)
    for key, value in data.items():
        print(f"{key} : {value}")


if __name__ == "__main__":
    full_name = input("Please Enter your full name :")
    url = f"https://api.diversitydata.io/?fullname={full_name}"
    print_data(url)
