import time
from tkinter import *
from interface.AbstractFrame import AbstractFrame


class TimerFrame(AbstractFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.time = time.strftime("%H:%M:%S")

        self.clock_label = Label(self.window)
        self.countdown_label = Label(self.window)
        self.countdown_job = None

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
        self.app_settings.test_init_times()
        self.clock_label.config(cnf=labels_cnf)
        self.clock_label.grid(cnf=labels_grid_cnf, column=0)
        self.clock()

        self.countdown_label.config(cnf=labels_cnf, text="0:00:00")
        self.countdown_label.grid(cnf=labels_grid_cnf, column=1)
        self.countdown()

    def clock(self):
        self.clock_label['text'] = time.strftime('%H:%M:%S')
        self.clock_label.after(1000, self.clock)

    def countdown(self):
        # time_remain contains remaining time or False if no time has left
        schedule_status = self.app_settings.get_schedule_status()
        if schedule_status:
            time_remain = self.app_settings.schedule_job()
            self.countdown_label['text'] = (time_remain if time_remain and schedule_status else "0:00:00")
            print("time_remain", time_remain)
        print("live_ON", self.app_settings.live_ON)
        # print("schedule_ON", self.app_settings.schedule_ON)
        print("===")
        self.countdown_job = self.window.after(1000, self.countdown)
