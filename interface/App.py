import os
from tkinter import *
from time import strftime
from interface.ListFrame import ListFrame
from interface.LiveFrame import LiveFrame
from scheduleLive.scheduleLive import ScheduleLive


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        ico_file = self.filename = os.path.dirname(__file__) + '/../data/FB32x32.ico'
        self.window.iconbitmap(ico_file)
        self.initUI()
        self.window.mainloop()

    def initUI(self):
        data = ScheduleLive().get_today_program()
        self.time_label()
        LiveFrame(self.window).window.grid(row=1, column=0)
        ListFrame(self.window, data).window.grid(row=2, column=0)

    def time_label(self):
        self.t_label = Label(self.window, font=('calibri', 28, 'bold'), fg='black')
        self.t_label.grid(row=0, column=0)
        self.time()

    def time(self):
        string = strftime('%H:%M:%S')
        self.t_label.config(text=string)
        self.t_label.after(1000, self.time)
