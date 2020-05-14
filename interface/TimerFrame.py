from datetime import datetime
import time
from tkinter import *
from interface.AbstractFrame import AbstractFrame


class TimerFrame(AbstractFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.time = time.strftime("%H:%M:%S")

        self.clock_label = Label(self.window)
        self.countdown_label = Label(self.window)

        self.init_ui()

    def init_ui(self):
        labels_cnf = {
            "font": ('calibri', 28, 'bold'),
            "fg": "black",
            "padx": 25
        }
        labels_grid_cnf = {
            "row": 0
        }
        self.clock_label.config(cnf=labels_cnf)
        self.clock_label.grid(cnf=labels_grid_cnf, column=0)
        self.clock()

        self.countdown_label.config(cnf=labels_cnf, text="00:00:00")
        self.countdown_label.grid(cnf=labels_grid_cnf, column=1)
        # self.countdown()

    def clock(self):
        self.clock_label['text'] = time.strftime('%H:%M:%S')
        self.clock_label.after(1000, self.clock)

    # def countdown(self):
    #     countdown = self.next()
    #     if not countdown == "00:00:00":
    #         self.countdown_label['text'] = countdown
    #         self.countdown_label.after(1000, self.countdown)
    #     else:
    #         print("go live from countdown")
    #
    # def next(self):
    #     now = time.localtime()
    #     next_time = time.strptime(f"{now.tm_year}-{now.tm_mon}-{now.tm_mday}-{self.next_time}", "%Y-%m-%d-%H:%M:%S")
    #     hours = next_time.tm_hour - now.tm_hour
    #     hours = hours if hours >= 10 else f"0{hours}"
    #     mins = next_time.tm_min - now.tm_min - 1
    #     mins = mins if mins >= 10 else f"0{mins}"
    #     secs = next_time.tm_sec - now.tm_sec + 29
    #     secs = secs if secs >= 10 else f"0{secs}"
    #     return f"{hours}:{mins}:{secs}"
