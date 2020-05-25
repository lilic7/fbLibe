import os

from interface.TimerFrame import TimerFrame
from interface.ListFrame import ListFrame
from interface.LiveFrame import LiveFrame
from schedule.Schedule import Schedule


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        ico_file = os.path.dirname(__file__) + '\\..\\data\\FB32x32.ico'
        self.window.iconbitmap(ico_file)
        self.init_ui()
        self.window.mainloop()

    def init_ui(self):
        sch = Schedule()
        # sch.test_generate_times()
        data = sch.get_program()

        TimerFrame(self.window).window.grid(row=0, column=0)
        LiveFrame(self.window).window.grid(row=1, column=0)
        ListFrame(self.window, data).window.grid(row=2, column=0)
