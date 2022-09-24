# Image Scrapper - A simple script to download images from a website.


import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm
import logging
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-u", "--url", help="Enter the url of the website")
args = vars(arg.parse_args())
url = args['url']

# save loggings to a file
logging.basicConfig(filename='image_scraper.log', 
                    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


class Scrapper:
    ''' 
    Scrapes the images from the website
    
    args:
        url: url of the website
    
    methods:
        get_data: gets the data from the website
        create_folder_for_site: creates a folder for the website
        get_links: gets the links of the images
        download_links: downloads the images

    '''
    def __init__(self, url):
        self.url = url
        logging.info("Starting image scraper for: {}".format(self.url))
    
    def get_data(self):
        ''' requests the data from the website '''
        response = requests.get(self.url)
        data = BeautifulSoup(response.content, 'html.parser')
        return data

    def create_folder_for_site(self):
        ''' creates a folder for the website '''
        basename = self.url.split('//')[1].split('/')[0].split('.')[0]
        image_out_dir = os.path.join(os.getcwd(), basename)
        if not os.path.isdir(image_out_dir):
            logger.info("Creating folder for site: {}".format(basename))
            os.makedirs(image_out_dir, exist_ok=True)
        return image_out_dir

    def get_links(self, data):
        ''' gets the links of the images '''
        images_links = []
        images_tags = data.find_all('img')
        for idx, image in enumerate(images_tags):
            images_links.append(urljoin(self.url, image['src']))
        
        total_links = len(images_links)
        logger.info("Total images found: {}".format(total_links))
        return images_links
    
    def download_links(self, links, image_out_dir):
        ''' downloads the images in the website folder'''
        for idx, link in enumerate(tqdm(links)):
            logger.info("Downloading image: {}".format(link))
            response = requests.get(link)
            with open(os.path.join(image_out_dir, str(idx) + '.jpg'), 'wb') as f:
                f.write(response.content)
                logger.info("Image {} downloaded with status code: {}".format(link, response.status_code))
            

def run_script():
    scrapper = Scrapper(url)
    data = scrapper.get_data()
    image_out_dir = scrapper.create_folder_for_site()
    images_link = scrapper.get_links(data)
    scrapper.download_links(images_link, image_out_dir)

    
if __name__ == "__main__":
    run_script()    