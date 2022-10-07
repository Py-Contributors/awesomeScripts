""""
    Program name : Website cloner
    author : https://github.com/codeperfectplus
    How to use : Check README.md
 """

import os
import sys
import requests
from bs4 import BeautifulSoup


class CloneWebsite:
    def __init__(self, website_name):
        self.website_name = website_name

    def crawl_website(self):
        """ This function will crawl website and return content"""
        content = requests.get(website_name)
        if content.status_code == 200:
            return content

    def create_folder(self):
        """ This funtion will create folder for website """
        folder_name = (website_name.split("/"))[2]
        try:
            os.makedirs(folder_name)
        except Exception as e:
            print(e)
        return folder_name

    def save_website(self):
        """ This function will save website to respective folder """
        folder_name = self.create_folder()
        content = self.crawl_website()
        with open(
            f"{folder_name}/index.html", "w", encoding="ascii", errors="ignore"
        ) as file:
            file.write(content.text)

    def save_image(self):
        folder_name = self.create_folder()
        os.chdir(folder_name)
        data = requests.get(website_name).text
        soup = BeautifulSoup(data, "html.parser")
        for img in soup.find_all("img"):
            src = img["src"]
            print(src)
            image_name = src.split("/")[-1]
            path = src.split("/")[:-1]
            path = "/".join(path)
            try:
                os.makedirs(path)
            except Exception:
                print("File Exists")

            if "/" == src[:1]:
                print(src)
                src = website_name + src
                img_data = requests.get(src).content
                with open(f"{path}/{image_name}", "wb") as file:
                    file.write(img_data)
                    print("complete")


if __name__ == "__main__":
    website_name = sys.argv[1]
    clone = CloneWebsite(website_name)
    clone.save_website()
    clone.save_image()
