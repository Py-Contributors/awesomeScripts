# DARK WEB SCRAPER

This script allows to scrap the deep and dark websites (.onion URLs) anonymously with Tor proxy.

## Requirements

- Tor Browser is required for the proxy connection.
- Requests(2.27.1) python package

## How to run

1. Install the requirements using `pip install -r requirements.txt` command
2. Open Tor browser and connect to Tor. (**Don't run the script without Tor connection**)
3. Change the `url` variable with your URL needed to be scraped.
4. Run the python script by `python3 dark_web_scraper.py` command in the terminal
5. The scraped HTML content is stored in `download.html` file
