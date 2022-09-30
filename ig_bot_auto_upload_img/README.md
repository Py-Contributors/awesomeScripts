# Script to auto upload picture on instagram account 

- Script will automatically upload pictures on the Instagram account from pixaby and upload them on the Instagram account in intervals of every 1 hour.

## About Pixaby  
Pixabay.com is a free stock photography and royalty-free stock media website. It is used for sharing photos, illustrations, vector graphics, film footage, and music, exclusively under the custom Pixabay license, which generally allows the free use of the material with some restrictions


INPUT_CSV_FILE- Input csv file is images link extracted from pixaby website under free license.

- input csv format

```csv
id,largeImageURL,webformatURL,previewURL,user,tags,pageURL
3113318,https://pixabay.com/get/g8d6619353738778e1dce41cb3ce1a459a8dd43d4ffca236e0c1a1ff7963149e506635cc811362e20631f5a2830819107a9cec3b0db1b34a7b09c45975a6a4c8b_1280.jpg,https://pixabay.com/get/gf577f4d05313461ecdeb5a68c36a42dc380f7de62e82af930b65069bde66671006acf323f771c9af372d11c3f9ed2a8c61d596c4e5ce3a290b1361d9ff7fd03a_640.jpg,https://cdn.pixabay.com/photo/2018/01/28/11/24/sunflower-3113318_150.jpg,bichnguyenvo,"sunflower, nature, flora",https://pixabay.com/photos/sunflower-nature-flora-flower-3113318/
```

### Parameters

# IG USERNAME AND PASSWORD
USERNAME = 'your instagram username'
PASSWORD = 'your instagram password'

#### sample Pixaby csv file is included in this repo
INPUT_CSV_FILE = csv link for images


#### Record txt for uploaded images to avoid duplicate upload
RECORD_TXT = "{}_record.csv".format(USERNAME)

#### TIME DELAY in minutes between each upload
TIME_INTERVAL =  10 # in minutes(upload every 10 minutes)
