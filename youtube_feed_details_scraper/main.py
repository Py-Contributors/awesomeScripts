import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def start_youtube_scraping():
    # Setup and start browser
    browser = setup_browser_and_options()
    browser.get('https://www.youtube.com')
    print(
        'Selenium has started scraping the following url: '
        + browser.current_url
    )

    # Scroll down as many times as possible to get the maximum amount of videos
    print('Youtube homepage is being processed, please wait...')
    scroll_until_there_is_no_tomorrow(browser)

    # Get the number of videos
    videos = get_all_loaded_videos(browser)
    print(str(len(videos)) + ' videos found. Approximate run time: ' + str(
        len(videos) * 3) + ' seconds.')

    # For each video grab its details
    all_videos_details = []
    for video in videos:
        details = get_video_details(browser, video['href'])
        if details:
            all_videos_details.append(details)

    print(all_videos_details)

    # Save everything to a csv
    save_result_to_csv(all_videos_details)

    # Make sure we quit the browser
    browser.quit()


def setup_browser_and_options():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    # ChromeDriverManager().install() will download chromedriver to the cache
    print('Downloading chromedriver, please wait...')

    return webdriver.Chrome(ChromeDriverManager().install(), options=options)


def scroll_until_there_is_no_tomorrow(browser):
    while True:
        try:
            load_more_element = WebDriverWait(browser, 7).until(
                ec.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     'ytd-continuation-item-renderer.ytd-rich-grid-renderer')))
            browser.execute_script("arguments[0].scrollIntoView();",
                                   load_more_element)
        except (TimeoutException, Exception) as e:
            print('No more videos to load.', e)
            break


def get_all_loaded_videos(browser):
    soup = BeautifulSoup(browser.page_source, 'lxml')
    videos = soup.find_all("a", {'id': 'video-title-link'}, href=True)
    return videos


def get_video_details(browser, video_link):
    browser.get('https://www.youtube.com' + video_link)
    print('Video url: ' + browser.current_url)

    try:
        WebDriverWait(browser, 3).until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, 'h1.title.ytd-video-primary-info-renderer'))
        )
        print('Video page loaded successfully, scraping video details.')

        bs = BeautifulSoup(browser.page_source, 'lxml')

        video_details = {
            'title': bs.find('h1', {'class': ['title',
                                              'ytd-video-primary-info-renderer'
                                              ]}).get_text(),
            'views': bs.find('span',
                             {'class': 'view-count'}).get_text().replace(
                ' views', ''),
            'link': browser.current_url,
            'upload_date': bs.find('div', {'id': 'date'})
                           .get_text()
                           .replace('•', '')
                           .replace('Premiered ', '')
                           .replace('on ', ''),
            'likes': bs.select(
                '.ytd-video-primary-info-renderer .ytd-menu-renderer '
                'a yt-formatted-string')[0]['aria-label'].replace(' likes',
                                                                  ''),
            'dislikes': bs.select(
                '.ytd-video-primary-info-renderer .ytd-menu-renderer '
                'a yt-formatted-string')[1]['aria-label'].replace(' dislikes',
                                                                  '')
        }

        return video_details

    except (TimeoutException, Exception) as e:
        print(
            "An error occurred while processing the video link."
            "Skipping it... \n Error:",
            e)
        return None


def save_result_to_csv(all_videos_details):
    try:
        with open("video_details.csv", 'w') as csv_file:
            writer = csv.DictWriter(csv_file,
                                    fieldnames=all_videos_details[0].keys())
            writer.writeheader()
            for data in all_videos_details:
                writer.writerow(data)
    except (IOError, Exception) as e:
        print("An error occurred while writing to the csv file.", e)


if __name__ == "__main__":
    print('Welcome to Youtube Feed Video Details Scraper v0.1')
    start_youtube_scraping()
