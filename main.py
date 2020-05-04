import os
import tkinter as tk
from time import strftime

from obs import Obs
from fbLive.live import FbLive
from scheduleLive.scheduleLive import ScheduleLive

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=500)
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
    os.system("taskkill /F /IM obs64.exe")
    fbLive.end_live()
    label['text'] = "Live terminat"


def time():
    string = strftime('%H:%M:%S')
    time_label.config(text=string)
    time_label.after(1000, time)




# Styling the label widget so that clock
# will look more attractive
time_label = tk.Label(root, font=('calibri', 40, 'bold'), foreground='black')
canvas1.create_window(150, 50, window=time_label)
time()

label = tk.Label(root, fg='green', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 100, window=label)

start_btn = tk.Button(text='Start', command=start_live, bg='brown', fg='white', font="16")
canvas1.create_window(100, 150, window=start_btn)

stop_btn = tk.Button(text='Stop', command=end_live, bg='brown', fg='white', font="16")
canvas1.create_window(200, 150, window=stop_btn)

program_label = tk.Label(root, fg='green', font=('helvetica', 12, 'bold'), text="Program pentru azi")
canvas1.create_window(150, 200, window=program_label)

sc = ScheduleLive()
program = sc.get_today_program()
start_pos = 220
current_date = strftime('%d.%m.%Y')
i=0
for item in program:
    title = item["title"].replace("::date::", current_date)
    label = tk.Label(root, fg='black', font=('helvetica', 10, 'normal'), text=f'{title}').grid(row=i, column=0)
    canvas1.create_window(100, start_pos, window=label)
    start_pos += 30
    i += 1

if __name__ == "__main__":
    root.mainloop()
