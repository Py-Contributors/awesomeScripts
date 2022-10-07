# extracting data from imdb
import sys
import requests
from bs4 import BeautifulSoup


class imdb:
    url = "https://www.imdb.com"

    def __init__(self):
        self.name = (
            self.episode
        ) = self.about = self.rating = self.directors = self.stars = ""
        self.more = []

    def find_name_episode(self, film):
        names_list = film.find_all("h3")[0].find_all("a")
        years_list = film.find_all("h3")[0].find_all("span")
        self.name = names_list[0].text + " " + years_list[1].text.strip()
        if len(names_list) == 2:
            self.episode = names_list[1].text + " " \
                                                + years_list[2].text.strip()

    def find_about(self, film):
        self.about = (
            film.find_all("p", {"class": "text-muted"})[0]
            .text.replace("\n", " ")
            .strip()
        )

    def find_more(self, film):
        more_list = film.find_all("h3")[0].find_all("a")
        self.more.append(more_list[0]["href"])
        if len(more_list) == 2:
            self.more.append(more_list[1]["href"])

    def find_rating(self, film):
        rating_list = film.find_all("div", {"class": "ratings-imdb-rating"})
        if rating_list == []:
            self.rating = "NA"
        else:
            self.rating = rating_list[0].text.replace("\n", "")

    def find_director_stars(self, film):
        stars_list = film.find_all("p")[2].text.replace("\n",
                                                        " ").strip().split("|")
        if len(stars_list) == 2:
            self.directors = stars_list[0].split(":")[1].strip()
            self.stars = stars_list[1].split(":")[1].strip()
        elif len(stars_list) == 1:
            if stars_list[0].split(":")[0].strip() == "Director":
                self.directors = stars_list[0].split(":")[1].strip()
            elif (
                stars_list[0].split(":")[0].strip() == "Stars"
                or stars_list[0].split(":")[0].strip() == "Star"
            ):
                self.stars = stars_list[0].split(":")[1].strip()

    def display(self):
        if self.name != "":
            print("Name      : " + self.name.strip())
        if self.episode != "":
            print("Episode   : " + self.episode.strip())
        if self.about != "":
            print("About     : " + self.about)
        if self.rating != "":
            print("Rating    : " + self.rating)
        if self.directors != "":
            print("Directors : " + self.directors)
        if self.stars != "":
            print("Stars     : " + self.stars)
        if len(self.more) == 2:
            print(
                "Read more : "
                + self.url
                + self.more[0]
                + "  or  "
                + self.url
                + self.more[1]
            )
        if len(self.more) == 1:
            print("Read more : " + self.url + self.more[0])
        print("\n\n")


def main():
    url = "https://www.imdb.com/search/title/"
    print("\n\nFetching Data...\n\n")
    page_start = 1
    flag = 1
    keyword = ""
    minimum = "0"
    maximum = "10"
    if len(sys.argv) >= 2:
        keyword = sys.argv[1]
        keyword = keyword.strip()
        keyword = keyword.replace(" ", "+")
    if len(sys.argv) >= 3:
        minimum = sys.argv[2]
    if len(sys.argv) >= 4:
        maximum = sys.argv[3]
    while flag:
        arr = []
        url = (
            url
            + "?title="
            + keyword
            + "&user_rating="
            + minimum
            + ","
            + maximum
            + "&start="
            + str(page_start)
            + "&ref_=adv_nxt"
        )
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        div = soup.find_all("div", {"class": "lister-item-content"})
        if div == []:
            print("\n\nNothing to Show\n\n")
        for film in div:
            arr.append(imdb())
            arr[-1].find_name_episode(film)
            arr[-1].find_about(film)
            arr[-1].find_more(film)
            arr[-1].find_rating(film)
            arr[-1].find_director_stars(film)
        for film in arr:
            film.display()
        page_start += 50
        progress = soup.find("div", {"class": "desc"}).find_all("span")[0].text
        print(progress)
        progress = progress.split()
        if len(progress) == 4:
            last = int(progress[2].replace(",", ""))
            if page_start > last:
                flag = 0
                print("End of titles\n")
            else:
                c = ""
                print(
                    "Type 'q' and enter to quit, another key \
                    and enter to see next set of entries : ",
                    end="",
                )
                while c == "":
                    c = input()
                if c == "q" or c == "Q":
                    flag = 0
                    print("End of titles\n")
                else:
                    print("\n\nFetching Data...\n\n")
        elif len(progress) == 2:
            print("End of titles\n")
            flag = 0


if __name__ == "__main__":
    main()
