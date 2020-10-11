# mediumScreaper
A screaper for Medium.com -posts

This script searches on `Medium.com` for a supplied `Topic` and returns the results as `Json`.

## Requirements Dependancies
Recommendet Python-Version
- `3.5+`

The only external dependancy is
- `BeautifulSoap`

## Installation
Install the required external dependancies with

```shell
$ pip3 install -r requirements.txt
```

Also, a `chmod +x mediumScraper.py` *can* be needed to make the script executable, otherwise You have to call it with `python3` (see [Usage Examples](#usage-examples))

## Usage examples
Getting help:
```shell
$ (python3) mediumScraper.py -h
```

Get posts for `python`:
```shell
$ (python3) mediumScraper.py python
```

Get maximum `100` posts for `software development`:
```shell
$ (python3) mediumScraper.py "software development" -c 100
```

Pretty-Print the `json` output:
```shell
$ (python3) mediumScraper.py python -b
```
