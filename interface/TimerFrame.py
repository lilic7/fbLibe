import time
from tkinter import *

from fbLive.live import FbLive
from obs import Obs


class TimerFrame:
    def __init__(self, parent, next_item):
        self.window = Frame()
        self.parent = parent
        self.time = time.strftime('%H:%M:%S')
        self.next_time = next_item['start_time']
        self.labels_cnf = {
            "font": ('calibri', 28, 'bold'),
            "fg": "black",
            "padx": 25
        }
        self.labels_grid_cnf = {
            "row": 0
        }
        self.clock_label = Label(self.window, cnf=self.labels_cnf)
        self.countdown_label = Label(self.window, cnf=self.labels_cnf)

        self.initUI()

    def initUI(self):
        self.clock_label.grid(cnf=self.labels_grid_cnf, column=0)
        self.clock()

        self.countdown_label.grid(cnf=self.labels_grid_cnf, column=1)
        self.countdown()

    def clock(self):
        self.clock_label['text'] = time.strftime('%H:%M:%S')
        self.clock_label.after(1000, self.clock)

    def countdown(self):
        countdown = self.next()
        if not countdown == "00:00:00":
            self.countdown_label['text'] = countdown
            self.countdown_label.after(1000, self.countdown)
        else:
            stream_key = FbLive("DevTest").create_live()
            obs = Obs()
            obs.change_key(stream_key)
            obs.start_live()

    def next(self):
        now = time.localtime()
        next_time = time.strptime(f"{now.tm_year}-{now.tm_mon}-{now.tm_mday}-{self.next_time}", "%Y-%m-%d-%H:%M:%S")
        hours = next_time.tm_hour - now.tm_hour
        hours = hours if hours>=10 else f"0{hours}"
        mins = next_time.tm_min - now.tm_min - 1
        mins = mins if mins>=10 else f"0{mins}"
        secs = next_time.tm_sec - now.tm_sec+29
        secs = secs if secs>=10 else f"0{secs}"
        return f"{hours}:{mins}:{secs}"
