import os
import tkinter as tk
from time import strftime

from obs import Obs
from fbLive.live import FbLive

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()
fbLive = FbLive("DevTest")


def start_live():
    stream_key = fbLive.create_live()
    obs = Obs()
    obs.change_key(stream_key)
    obs.start_live()
    page = fbLive.get_active_page()
    label['text'] = page["name"]


def end_live():
    fbLive.end_live()
    label['text'] = "Live terminat"


def time():
    string = strftime('%H:%M:%S')
    time_label.config(text=string)
    time_label.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
time_label = tk.Label(root, font=('calibri', 40, 'bold'),
               background='purple',
               foreground='white')
canvas1.create_window(150, 50, window=time_label)
time()

label = tk.Label(root, fg='green', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 100, window=label)

start_btn = tk.Button(text='Start', command=start_live, bg='brown', fg='white')
canvas1.create_window(100, 150, window=start_btn)

stop_btn = tk.Button(text='Stop', command=end_live, bg='brown', fg='white')
canvas1.create_window(200, 150, window=stop_btn)

if __name__ == "__main__":
    root.mainloop()
