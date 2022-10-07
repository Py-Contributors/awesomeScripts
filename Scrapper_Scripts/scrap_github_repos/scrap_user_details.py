""" Scrap Github User Details
    Check README.md for instructions """

__author__ = "CodePerfectPlus"
__date__ = "28/09/2020"

import sys
import requests


class GithubUserScraper:
    def __init__(self, username):
        self.username = username

    def scrapUser(self):
        URL = f"https://api.github.com/users/{self.username}"
        user_data = requests.get(URL).json()
        user_objects = [
            "name",
            "login",
            "company",
            "location",
            "email",
            "bio",
            "public_repos",
            "followers",
            "following",
            "created_at",
            "updated_at",
        ]
        try:
            for object in user_objects:
                details = user_data[object]
                print(f"{object.title()} : {details}")
        except Exception:
            print(
                "User doesn't exist on Github. \
                    Try Again with Proper Details"
            )


if __name__ == "__main__":
    username = sys.argv[1]
    new_user = GithubUserScraper(username)
    new_user.scrapUser()
