import requests
from project_scrapper import save_project

save_project()


def get_data(url):
    data = requests.get(url)
    return data.text


def save_data(url):
    data = get_data(url)
    with open("contributors.json", "w") as file:
        file.write(data)


if __name__ == "__main__":
    user = "py-contributors"
    repo = "awesomescripts"
    url = f"https://api.github.com/repos/{user}/{repo}/contributors"
    save_data(url)
