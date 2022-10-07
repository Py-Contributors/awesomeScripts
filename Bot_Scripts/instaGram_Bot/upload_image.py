from instabot import Bot
import pandas as pd
import os
import glob
import time
import json
import requests

bot = Bot()

cookie_del = glob.glob("config/*cookie.json")
print(cookie_del)
if cookie_del:
   os.remove(cookie_del[0])


def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def download_image(path):
    response = requests.get(path)
    return response.content


USERNAME = 'your instagram username'
PASSWORD = 'your instagram password'

INPUT_CSV_FILE = "data/pixaby.csv"
RECORD_TXT = "{}_record.csv".format(USERNAME)
TIME_INTERVAL =  10 # in minutes(upload every 10 minutes)


with open(RECORD_TXT, 'r') as f:
    records = f.read().splitlines()

print("Loading Records", records)
print("Logging in as : {}".format(USERNAME))

bot.login(username=USERNAME, password=PASSWORD)

df = pd.read_csv(INPUT_CSV_FILE)
df = df.sample(frac=1).reset_index(drop=True)

for _, row in df.iterrows():
    idx = row['id']
    image_url = row['largeImageURL']
    tags = row['tags'].split(',')
    image_name = "{}_{}.jpg".format(tags[0], idx)
    
    idx = str(idx)
    if idx not in records:
        hastags = [tag.strip().replace(' ', '_') for tag in tags]
        hastags = ["#" + tag.strip() for tag in hastags]
        hastags = " ".join(hastags)
        user = row['user']
        
        output_folder = f"temp/{tags[0]}"
            
        if not os.path.isfile(os.path.join(output_folder, image_name)):
            image = download_image(image_url)
            
            os.makedirs(output_folder, exist_ok=True)
            with open(os.path.join(output_folder, image_name), 'wb') as f:
                f.write(image)
        else:
            print(f"Image {image_name} already exists")
        
        caption = "Image by: {}\n{},  #photography #naturephotography #love #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #like #follow #travelphotography #bhfyp #happy".format(user, hastags)
        
        print("Uploading image : {}".format(image_name))
        
        response = bot.upload_photo(os.path.join(output_folder, image_name), caption=caption)
        
        print("Response : {}".format(response))

        print("Updating records")
        
        with open(RECORD_TXT, 'a') as f:
            f.write(str(idx) + '\n')
            
        time.sleep(TIME_INTERVAL*60)
        time.sleep(5)
