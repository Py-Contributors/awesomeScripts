import urllib.request


def check_website_status():
    prompt = "Please enter a website URL: "
    while True:
        # asks for URL to check
        # adds in https or http if necessary
        url = str(input(prompt))
        if url.startswith('https://'):
            pass
        elif url.startswith('http://'):
            pass
        else:
            url = 'https://' + url
        try:
            # tries to make a request to the URL that was input
            # uses defined headers that are not a "bot"
            headers = {}
            headers['User-Agent'] = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
            req = urllib.request.Request(url, headers=headers)
            page = urllib.request.urlopen(req)
            code = str(page.getcode())
            print('The website ' + url + ' has returned a ' + code + ' code')
            break
        except Exception as e:
            # if there is an error it will ask if you want to try again
            print(str(e))
            print("Make sure you are entering a valid URL")
            try_again = input("Do you want to try again (y/n): ")
            try_again = try_again.lower()
            if try_again == 'y':
                continue
            else:
                break


check_website_status()
