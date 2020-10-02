# -*- coding: utf-8 -*-
"""Torrent To Google Drive Downloader
    This code will only work in Google Colab as it is using Google drive
# Torrent To Google Drive Downloader

**Important Note:** To get more disk space:
> Go to Runtime -> Change Runtime and give GPU as the Hardware Accelerator.
You will get around 384GB to download any torrent you want.
Don't use GPU if more storage is not needed,
Otherwise your account may get blocked

### Install libtorrent and Initialize Session
"""

# !apt install python3-libtorrent Use in Google Colab

import libtorrent as lt
from google.colab import drive
from google.colab import files
import time
from IPython.display import display
import ipywidgets as widgets

ses = lt.session()
ses.listen_on(6881, 6891)
downloads = []

"""### Mount Google Drive
To stream files we need to mount Google Drive.
"""
drive.mount("/content/drive")
"""### Add From Torrent File
You can run this cell to add more files as many times as you want.
"""
source = files.upload()
params = {
    "save_path": "/content/drive/My Drive/Torrent",
    "ti": lt.torrent_info(list(source.keys())[0]),
}
downloads.append(ses.add_torrent(params))

"""### Add From Magnet Link
You can run this cell to add more files as many times as you want
"""

params = {"save_path": "/content/drive/My Drive/Torrent"}

while True:
    magnet_link = input("Enter Magnet Link Or Type Exit: ")
    if magnet_link.lower() == "exit":
        break
    downloads.append(
        lt.add_magnet_uri(ses, magnet_link, params)
    )

"""### Start Download"""
state_str = [
    "queued",
    "checking",
    "downloading metadata",
    "downloading",
    "finished",
    "seeding",
    "allocating",
    "checking fastresume",
]

layout = widgets.Layout(width="auto")
style = {"description_width": "initial"}
download_bars = [
    widgets.FloatSlider(
        step=0.01, disabled=True, layout=layout, style=style
    )
    for _ in downloads
]
display(*download_bars)

while downloads:
    next_shift = 0
    for index, download in enumerate(downloads[:]):
        bar = download_bars[index + next_shift]
        if not download.is_seed():
            s = download.status()

            bar.description = " ".join(
                [
                    download.name(),
                    str(s.download_rate / 1000),
                    "kB/s",
                    state_str[s.state],
                ]
            )
            bar.value = s.progress * 100
        else:
            next_shift -= 1
            ses.remove_torrent(download)
            downloads.remove(download)
            bar.close()
            download_bars.remove(bar)
            print(download.name(), "complete")
    time.sleep(1)
