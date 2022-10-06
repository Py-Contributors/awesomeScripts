# DARK WEB SCRAPER

This script allows to scrap the deep and dark websites (.onion URLs) anonymously with Tor proxy.

## Requirements

Tor Browser is required for the proxy connection. Other than no python libraries are required, all the libraries used in this are built-in python packages.

## How to run

1. Open Tor browser and connect to tor. (**Don't run the script without Tor connection**)
2. Change the `url` variable with your URL needed to be scraped.
3. Run the python script by `python3 dark_web_scraper.py` command in the terminal
4. The scraped HTML content is stored in `download.html` file
