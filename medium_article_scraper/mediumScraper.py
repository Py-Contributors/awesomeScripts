#!/usr/bin/env python3

import requests
import argparse
import sys
import json
from urllib import parse
from bs4 import BeautifulSoup


def parseArgs():
    parser = argparse.ArgumentParser(description='Gets posts from Medium.com for a specific topic.')
    parser.add_argument('topic', metavar='TOPIC', type=str,
                        help='the topic to search for')
    parser.add_argument('-c', '--count', dest='count', action='store', default=15,
                        help='maximum number of posts')
    parser.add_argument('-b', '--beautify', dest='beautiefy', action='store_true',
                        help='beautiefy json output')

    return parser.parse_args()


def run(args):
    def parsePost(tag):
        title = tag.find('h3', class_='graf')
        desc = tag.find('p')
        url = tag.find_all('a')[3]
        return {
            'title': title.text if title else '',
            'desc': desc.text if desc else '',
            'url': url.get('href').split('?')[0] if url else '',
        }

    urlParams = {
        'topic': parse.quote(args.topic),
        'count': args.count
    }

    url = 'https://medium.com/search/posts?q={topic}&count={count}'.format_map(urlParams)

    posts = []

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    rawPosts = soup.find_all('div', class_='postArticle')

    if len(rawPosts) > 0:
        for post in rawPosts:
            posts.append(parsePost(post))
    else:
        print('No posts found for "%s"...' % args.topic)
        sys.exit(0)

    print(json.dumps(posts, indent=(4 if args.beautiefy else None)))


if __name__ == '__main__':
    run(parseArgs())
