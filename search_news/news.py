import argparse
import requests

API_KEY = "6281e58eada2455993220febc56c30a3"


def articles_fetcher(search_term):
    req_url = "http://newsapi.org/v2/everything?"

    PARAMS = {
        'qInTitle' : search_term,
        'sortBy' : "popularity",
        'language' : "en",
        'pageSize' : 5,
        'apiKey' : API_KEY,
    }

    headers = {
        'user-agent': 'news_search @ github.com/Py-Contributors/awesomeScripts'
    }
    r = requests.get(req_url, params=PARAMS, headers=headers)
    data = r.json()
    return data.get("articles")


def printer(search_term, articles):

    if len(articles) > 0:
        print("\nNews related to '%s'" % search_term)
    else:
        print("No results for '%s', try searching another term!" % search_term)

    for count, article in enumerate(articles, start=1):

        source_name = article["source"]["name"]
        title = article["title"]
        description = article["description"]
        source_url = article["url"]

        text = "\n%d | %s\n%s\n%s\nContinue reading at %s" % (
            count,
            source_name,
            title,
            description,
            source_url
        )
        print(text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_term", help="The search term.")
    args = parser.parse_args()
    search_term = args.search_term

    articles = articles_fetcher(search_term.lower())
    printer(search_term, articles)


if __name__ == "__main__":
    main()
