import os

from interface.TimerFrame import TimerFrame
from interface.ListFrame import ListFrame
from interface.LiveFrame import LiveFrame
from scheduleLive.scheduleLive import ScheduleLive


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        ico_file = self.filename = os.path.dirname(__file__) + '/../data/FB32x32.ico'
        self.window.iconbitmap(ico_file)
        self.time_frame = TimerFrame(self.window, ScheduleLive().get_next_live_schedule())
        self.initUI()
        self.window.mainloop()

    def initUI(self):
        data = ScheduleLive().get_today_program()
        self.time_frame.window.grid(row=0, column=0)
        LiveFrame(self.window).window.grid(row=1, column=0)
        ListFrame(self.window, data).window.grid(row=2, column=0)
