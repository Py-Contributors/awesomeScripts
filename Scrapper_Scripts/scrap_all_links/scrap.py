import requests
import argparse
from bs4 import BeautifulSoup, SoupStrainer
from validator_collection import checkers

parser = argparse.ArgumentParser(description='Scrape them all!')
parser.add_argument('link', metavar='link',
                    type=str, nargs=1, help='Link of the target website')
parser.add_argument('-o', metavar='outputFile',
                    type=str, nargs=1, help='Outputs results into a file')
args = parser.parse_args()


class Scraper:

    def __init__(self, args):
        self.args = args
        self.greet()

    def greet(self):
        print('''
                    Scrap All Links!

        from github.com/Py-Contributors/awesomeScripts
        ''')

    def scrape(self, args):
        links = []

        link_arg = args.link[0]
        if not checkers.is_url(link_arg):
            raise Exception(link_arg + " is not a valid URL")
        response = requests.get(link_arg)

        for link in BeautifulSoup(response.text, features="html.parser",
                                  parse_only=SoupStrainer('a')):
            if link.has_attr('href') and link['href'].startswith("http"):
                links.append(link['href'])

        return links

    def pretty_print(self, links):
        out = False
        outPath = str
        if self.args.o:
            out = True
            outPath = "./" + self.args.o[0]
            open(outPath, 'w').close()

        for link in links:
            print(link)
            if out:
                with open(outPath, 'a') as f:
                    f.write(link + "\n")
                    f.close()

    def run(self):
        self.pretty_print(self.scrape(self.args))


if __name__ == "__main__":
    scraper = Scraper(args)
    scraper.run()
