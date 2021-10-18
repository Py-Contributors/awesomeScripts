#!/bin/python
'''
Subtitle Searcher

'''
import requests
from bs4 import BeautifulSoup
import os
import sys
import argparse
import tkinter as tk
from tkinter import filedialog
import zipfile


class podnapsi():
    titledict = {}
    finalsoupdict = {}

    def __init__(self):

        self.sub_name = None
        self.queries = None
        self.movie_type = None
        self.seasons = None
        self.year = None
        self.titledict = {}
        self.finalsoupdict = {}

    def get_sublist(self,  *args,  **kwargs):

        website = "https://podnapisi.net/subtitles/search/?movie_type= \
                &episodes=" + self.episode + "&year=&keywords=" \
                + self.subname + "&seasons=" + self.season
        try:
            podpage = requests.get(website)
            podsoup = BeautifulSoup(podpage.text, "lxml")
            finalsoup = podsoup.find_all('span', {'class': 'release'})
            # Finds the corresponding links
            finalsoup1 = podsoup.find_all(
                                          'a', {"alt": "Download subtitles."})
            self.titledict = {}
            self.finalsoupdict = {}
            for number, title in enumerate(finalsoup, start=1):
                self.titledict[number] = title['title']
                print(number, title['title'])
            if len(self.titledict) == 0:
                print("No subtitles found\n Exiting...")
                sys.exit(1)
            for number, href in enumerate(finalsoup1, start=1):
                self.finalsoupdict[number] = href['href']
            if len(self.finalsoupdict) == 0:
                print("No subtitles found\n Exiting...")
                sys.exit(1)
        except ConnectionError:
            print("Error")

    def download_sub(self, path, subnum, *args, **kwargs):

        self.root = tk.Tk()
        self.root.withdraw()
        download_link = "https: //www.podnapisi.net"+self.finalsoupdict[subnum]
        def_title = self.titledict[subnum]

        if not path:
            path = filedialog.asksaveasfilename(
                defaultextension=".zip", filetypes=(
                    ("Zip", "*.zip"), ("all files", "*.*")))
            if not path:
                path = os.getcwd()+"/"+def_title
        while True:
            try:
                subdownload = requests.get(download_link, timeout=0.5)
            except requests.exceptions.Timeout:
                print("\n Retrying")
            else:
                break

        print("DIRECTORY", path)
        if subdownload.status_code == 200:
            with open(path, "wb") as req_file:
                req_file.write(subdownload.content)
                with zipfile.ZipFile(path, "r") as zip_ref:
                    zip_ref.extractall(os.getcwd()+"/")
                    os.remove(path)


def main():

    try:
        subparse = argparse.ArgumentParser(prog="main.py")
        subparse.add_argument(
            'subtitle_name',
            metavar="subtitle name",
            help="Specify the subtitle name",
            type=str)
        subparse.add_argument(
            'season_num',
            metavar="Season number",
            help="Specify the season number",
            type=str)
        subparse.add_argument(
            'episode_num',
            metavar="Episode number",
            help="Specify the episode number",
            type=str)
        subparse.add_argument(
            '-d', '--directory',
            metavar="Directory",
            help="Specify the Directory",
            type=str)
        if len(sys.argv) < 2:
            print("\rUse the -h or --help option with main.py ")
            subparse.exit(1)
        parsedopt = subparse.parse_args()
        sub_name = parsedopt.subtitle_name.replace(" ", '+')
        sub_episode = parsedopt.episode_num
        sub_season = parsedopt.season_num
        sub_directory = parsedopt.directory
        ne = podnapsi(sub_name, sub_episode, sub_season)
        ne.get_sublist()
        while True:
            try:
                sub_number = int(
                    input(
                        "\nPlease enter the subtitle number> "
                    )
                )
            except ValueError:
                print("Invalid input")
            else:
                break
        ne.download_sub(sub_directory, sub_number)
    except KeyboardInterrupt:
        print("\nExited forcefully")


if __name__ == "__main__":
    main()
