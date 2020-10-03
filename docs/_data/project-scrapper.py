from bs4 import BeautifulSoup
import requests

url = "https://github.com/Py-Contributors/awesomeScripts/blob/master/README.md"
page = requests.get(url)
pagetext = page.text

projects_table = {
    "name": [],
    "author": [],
    "description": [],
}

soup = BeautifulSoup(pagetext, "lxml")
table = soup.find("table")

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll(["th", "td"]):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

file = open("projects.csv", "w")
for item in list_of_rows:
    file.write(",".join(item))
    file.write("\n")
file.close()
