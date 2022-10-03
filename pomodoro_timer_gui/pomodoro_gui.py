# Use tkninter as GUI

# Focus timer default: 25 minutes
# After 25 minutes is up, either output a sound / expand screen.
# Optional feature
#   : user can choose to do 15/25/30 mins for focus timer

from tkinter import *
import time
from tkinter import messagebox

# =========================== DISPLAY =========================== #

window = Tk()
window.title("Pomodoro")

# dimensions of application
window_width  = 500
window_height = 300

# dimensions of screen
screen_width  = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# center coordinates of window
x = int((screen_width  / 2) - (window_width  / 2))
y = int((screen_height / 2) - (window_height / 2))

# centering window onto screen
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# setting window background color
window.config(bg = '#664229')


# canvas = Canvas(bg = '#664229')

# canvas.create_window()
#
# canvas.create_text(300, 50, text = "25:00", fill = 'white', font = 'Courier')
# canvas.pack()

window.mainloop()

# countdown mechanism

# resetting countdown
