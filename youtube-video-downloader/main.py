from tkinter import Tk, PhotoImage, Label, Entry, Button, StringVar
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from functools import partial
from threading import Thread
from pytube import YouTube


def dldfunc(url1):
    global thumburl
    url2 = (url1.get())
    path = askdirectory()
    yt = YouTube(url2)
    thumburl = yt.thumbnail_url
    yt.streams.filter(progressive=True, res='720p').first().download(path)
    showinfo("Downloaded", 'Download Successfull!')
    Entry.delete(0, 'end')


def altthread(url):
    dlthread = Thread(target=dldfunc(url))
    dlthread.start()


# gui
root = Tk()
root.geometry('400x500')
file = PhotoImage(file='youtube-video-downloader\\images\\head_icon.png')
Label(root, image=file).pack(side='top')
root.title('PytubeDL-Unofficial')
url = StringVar()
Label(root, text="Input URL \U00002193").pack()
Entry(root, textvariable=url).pack(side='top', fill='x', padx=5)
dldfunc1 = partial(altthread, url)
btn = Button(root, text="Download", command=dldfunc1)
btn.pack(side='top')
root.mainloop()
