""""
    Program name : Website cloner
    author : https://github.com/codeperfectplus
    How to use : Check README.md
 """

import os
import sys
import requests

class CloneWebsite:

    def __init__(self,website_name):
        self.website_name = website_name

    def crawl_website(self):
        """ This function will crawl website and return content"""
        content = requests.get(website_name)
        if content.status_code == 200:
            return content

    def create_folder(self):
        ''' This funtion will create folder for website '''
        folder_name = (website_name.split("/"))[2]
        try:
            os.makedirs(folder_name)
        except Exception as e:
            print(e)
        return folder_name

    def save_website(self):
        ''' This function will save website to respective folder '''
        folder_name = self.create_folder()
        content = self.crawl_website()
        with open(f"{folder_name}/index.html", "w") as file:
            file.write(content.text)

if __name__ == "__main__":
    website_name = sys.argv[1]
    clone = CloneWebsite(website_name)
    clone.save_website()
