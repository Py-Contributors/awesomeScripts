# Use tkninter as GUI

# Focus timer default: 25 minutes
# After 25 minutes is up, either output a sound / expand screen.

# Optional feature to be implemented
#   : user can choose to do 15/25/30 mins for focus timer

from tkinter import *
from tkmacosx import Button
import math

# ==================== GLOBAL CONSTANTS ========================= #
# widget colors
BG_COLOR = "#664229"
IDLE_COLOR = "#987554"
ACTIVE_COLOR = "#b99976"
FONT_COLOR = "white"

# window dimensions
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 200

# text display constants
TIMER_FONT_SIZE = 40
ITEM_FONT_SIZE = 15
FONT_FAMILY = "Corbel"
TEXT_X = WINDOW_WIDTH / 2
TEXT_Y = (WINDOW_HEIGHT / 2) - 10

# timer constants
FOCUS_MIN = 25
LONG_BREAK_MIN = 20
SHORT_BREAK_MIN = 5

# comment out this section after testing
# FOCUS_MIN = 0.15         # 0.15 (09 seconds)
# LONG_BREAK_MIN = 0.10    # 0.10 (06 seconds)
# SHORT_BREAK_MIN = 0.05   # 0.05 (03 seconds)

class Pomodoro:
    def __init__(self):

        self.window = Tk()
        self.window.config(bg=BG_COLOR)
        self.window.title("Pomodoro")

        # get screen dimensions
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # center coordinates of window
        self.x = int((self.screen_width / 2) - (WINDOW_WIDTH / 2))
        self.y = int((self.screen_height / 2) - (WINDOW_HEIGHT / 2))

        # centering window onto screen
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{self.x}+{self.y}")

        # set minimum and maximum window size
        self.window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.focus_rounds_text = ""
        self.sessions = -1
        self.restart_button = None
        self.start_button = None
        self.long_break_timer = None
        self.short_break_timer = None
        self.focus_timer = None
        self.progress_indicator = None
        self.mode_display = None
        self.mode_text = ""

        self.long_break_display()
        self.short_break_display()

        self.focus_display()
        self.labels_display()
        self.buttons_display()

        self.window.mainloop()

    # ======================= TIMER MECHANICS ======================= #

    def start_timer(self):

        focus_sec = math.floor(FOCUS_MIN * 60)
        short_break_sec = math.floor(SHORT_BREAK_MIN * 60)
        long_break_sec = math.floor(LONG_BREAK_MIN * 60)

        self.sessions += 1

        # long break if 2nd session
        if self.sessions > 6:
            self.restart_timer()
        else:
            if self.sessions == 3:
                self.long_break_timer.config(text=f"0{LONG_BREAK_MIN}:00")
                self.countdown(long_break_sec, self.long_break_timer, self.focus_timer, self.short_break_timer)
                self.mode_text = "- break -"

            # short break if 1st and 3rd
            elif self.sessions % 2 == 1:
                self.short_break_timer.config(text=f"0{SHORT_BREAK_MIN}:00")
                self.countdown(short_break_sec, self.short_break_timer, self.focus_timer, self.long_break_timer)
                self.mode_text = "- break -"

            else:
                self.focus_timer.config(text=f"0{FOCUS_MIN}:00")
                self.countdown(focus_sec, self.focus_timer, self.short_break_timer, self.long_break_timer)
                self.mode_text = "- focus -"
                self.focus_rounds_text += "*"
                self.progress_indicator.config(text=self.focus_rounds_text)

            self.mode_display.config(text=self.mode_text)
            self.restart_button.place(relx=0.5, rely=0.8, anchor="center")

            if self.start_button is not None:
                self.start_button.place_forget()

        pass

    def restart_timer(self):
        self.destroy_display()
        self.long_break_display()
        self.short_break_display()
        self.focus_display()
        self.labels_display()
        self.buttons_display()
        pass

    # countdown mechanism
    def countdown(self, c, t, f1, f2):
        f1.place_forget()
        f2.place_forget()
        t.place(relx=0.5, rely=0.25, anchor="center")

        curr_min = math.floor(c / 60)
        curr_sec = math.floor(c % 60)

        # adding '0' in front of timer display if single digit
        if curr_min < 10:
            curr_min = f"0{curr_min}"

        if curr_sec < 10:
            curr_sec = f"0{curr_sec}"

        t.config(text=f"{curr_min}:{curr_sec}")

        if c > -1:
            t.after(1000, self.countdown, c - 1, t, f1, f2)

        else:
            self.start_timer()
        pass

    def focus_display(self):
        self.focus_timer = Label(self.window, text=f"{FOCUS_MIN}:00", fg=FONT_COLOR, bg=BG_COLOR,
                                 font=(FONT_FAMILY, TIMER_FONT_SIZE,
                                       "bold"))
        self.focus_timer.place(relx=0.5, rely=0.25, anchor="center")
        pass

    def short_break_display(self):
        self.short_break_timer = Label(self.window, text=f"{SHORT_BREAK_MIN}:00", fg=FONT_COLOR, bg=BG_COLOR,
                                       font=(FONT_FAMILY, TIMER_FONT_SIZE,
                                             "bold"))
        pass

    def long_break_display(self):
        self.long_break_timer = Label(self.window, text=f"{LONG_BREAK_MIN}:00", fg=FONT_COLOR, bg=BG_COLOR,
                                      font=(FONT_FAMILY, TIMER_FONT_SIZE,
                                            "bold"))
        pass

    def buttons_display(self):
        # set buttons display
        self.restart_button = Button(self.window, text="RESTART", bg=IDLE_COLOR, fg=FONT_COLOR,
                                     font=(FONT_FAMILY, ITEM_FONT_SIZE, "bold"), borderless=1,
                                     activebackground=(ACTIVE_COLOR, IDLE_COLOR), activeforeground=BG_COLOR,
                                     command=self.restart_timer)

        self.start_button = Button(self.window, text="START", bg=IDLE_COLOR, fg=FONT_COLOR,
                                   font=(FONT_FAMILY, ITEM_FONT_SIZE, "bold"), borderless=1,
                                   activebackground=(ACTIVE_COLOR, IDLE_COLOR), activeforeground=BG_COLOR,
                                   command=self.start_timer)

        self.start_button.place(relx=0.5, rely=0.8, anchor="center")
        pass

    def labels_display(self):
        # set mode display
        self.mode_text = "- focus -"
        self.mode_display = Label(self.window, text=self.mode_text, fg=FONT_COLOR, bg=BG_COLOR,
                                  font=(FONT_FAMILY, ITEM_FONT_SIZE, "bold"))

        self.mode_display.place(relx=0.5, rely=0.45, anchor="center")

        # set focus rounds display
        self.sessions = -1
        self.focus_rounds_text = ""
        self.progress_indicator = Label(self.window, text=self.focus_rounds_text,
                                        font=(FONT_FAMILY, TIMER_FONT_SIZE, "bold"),
                                        fg=IDLE_COLOR,
                                        bg=BG_COLOR)

        self.progress_indicator.place(relx=0.5, rely=0.65, anchor="center")
        pass

    def destroy_display(self):
        if self.focus_timer is not None:
            self.focus_timer.destroy()
        if self.long_break_timer is not None:
            self.long_break_timer.destroy()
        if self.short_break_timer is not None:
            self.short_break_timer.destroy()
        if self.progress_indicator is not None:
            self.progress_indicator.destroy()
        if self.mode_display is not None:
            self.mode_display.destroy()
        if self.start_button is not None:
            self.start_button.destroy()
        if self.restart_button is not None:
            self.restart_button.destroy()
        pass


Pomodoro()
