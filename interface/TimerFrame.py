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
        if self.app_settings.is_schedule_active():
            result = self.app_settings.schedule_job()
            if result:
                self.countdown_label.config(
                    text=result['time'] if result['status'] == "ready" or result['status'] == "live" else "0:00:00",
                    fg="red" if result['status'] == "live" else "orange"
                )
        self.window.after(1000, self.countdown)
