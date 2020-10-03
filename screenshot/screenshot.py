import tkinter as tk
import pyautogui
import os


root = tk.Tk()
time = tk.IntVar( )
time.set(3)


def take_shot():
    timeleft = time.get()
    if timeleft > 0:
        timeleft -= 1
        time.set(timeleft)
        root.after(1000,take_shot)
    else :
        s = pyautogui.screenshot()
        
# Save a screenshot on current working directory
        s.save(os.getcwd() + "shot.png")
        tk.messagebox.showinfo("Screenshot", "Screenshot saved!")
        time.set(3)


l = tk.Label(root,textvariable = time,fg="blue")
l.pack()

b = tk.Button(root,text = f"Take Screenshot 3 secs", command = take_shot)
b.pack()

root.mainloop()