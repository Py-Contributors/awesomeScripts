# YouTube Feed Video Details Scraper 
A selenium scraper that loads all the videos from YouTube's homepage and crawls through them gathering their details.

## About the Program
YouTube uses a real-time javascript loading mechanism making it difficult to scrape the website. 
For this purpose, using selenium, we scroll through the homepage until it stops giving us new videos.
Then, one-by-one, I visit the links to those videos and scrape the info required.

For the purpose of this project I have gathered the following details:
```
1. title
2. views
3. link
4. upload_date
5. likes
6. dislikes
```

Finally the results are exported to a csv file in the root of the project names `video_details.csv`

## To Run
- Run `pip3 install -r requirements.txt`
- Run `python3 main.py`
- Enjoy!

