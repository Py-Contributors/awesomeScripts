import tkinter as tk
from tkinter import messagebox
import pyautogui
import os


root = tk.Tk()
time = tk.IntVar()
time.set(3)


def take_shot():
    timeleft = time.get()
    if timeleft > 0:
        timeleft -= 1
        time.set(timeleft)
        root.after(1000, take_shot)
    else :
        s = pyautogui.screenshot()
# Save a screenshot on current working directory
        s.save(os.getcwd() + "shot.png")
        messagebox.showinfo("Screenshot", "Screenshot saved!")
        time.set(3)


L = tk.Label(root, textvariable=time, fg="blue")
L.pack()

b = tk.Button(root, text="Take Screenshot 3 secs", command=take_shot)
b.pack()

root.mainloop()
