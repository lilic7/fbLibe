import os
import tkinter as tk
from time import strftime

from fbLive.live import FbLive
from obs import Obs

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.fb_live = FbLive("DevTest")


canvas1 = tk.Canvas(root, width=400, height=500)
canvas1.pack()
fbLive = FbLive("DevTest")
signal_status_id = 0


def start_live():
    stream_key = fbLive.create_live()
    obs = Obs()
    obs.change_key(stream_key)
    obs.start_live()
    page = fbLive.get_active_page()
    label['text'] = page["name"]
    stream_framerate.after(5000, stream_status)


def end_live():
    os.system("taskkill /F /IM obs64.exe")
    fbLive.end_live()
    label['text'] = "Live terminat"
    root.after_cancel(signal_status_id)
    stream_framerate.config(text='')
    stream_vbitrate.config(text='')
    stream_abitrate.config(text='')


def time():
    string = strftime('%H:%M:%S')
    time_label.config(text=string)
    time_label.after(1000, time)


time_label = tk.Label(root, font=('calibri', 40, 'bold'), foreground='black')
canvas1.create_window(150, 50, window=time_label)
time()


# ==================
def stream_status():
    data = fbLive.get_stream_status()
    if "framerate" in data:
        stream_size.config(text=f'FR: {data["size"]}')
        stream_framerate.config(text=f'FR: {data["framerate"]}')
        stream_vbitrate.config(text=f'VB: {data["v_bitrate"]}')
        stream_abitrate.config(text=f'AB: {data["a_bitrate"]}')
    stream_framerate.after(5000, stream_status)


stream_info = tk.LabelFrame(root, foreground='black', text="Stream info")
canvas1.create_window(160, 350, window=stream_info)

stream_size = tk.Label(root, font=('calibri', 12, 'normal'), foreground='black', text="444x333")
stream_framerate = tk.Label(root, font=('calibri', 12, 'normal'), foreground='black', text="FR: 34")
stream_vbitrate = tk.Label(root, font=('calibri', 12, 'normal'), foreground='black')
stream_abitrate = tk.Label(root, font=('calibri', 12, 'normal'), foreground='black')
canvas1.create_window(50, 465, window=stream_size)
canvas1.create_window(50, 490, window=stream_framerate)
canvas1.create_window(150, 490, window=stream_vbitrate)
canvas1.create_window(250, 490, window=stream_abitrate)
# ===========

label = tk.Label(root, fg='green', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 100, window=label)

start_btn = tk.Button(text='Start', command=start_live, bg='brown', fg='white', font="16")
canvas1.create_window(100, 150, window=start_btn)

stop_btn = tk.Button(text='Stop', command=end_live, bg='brown', fg='white', font="16")
canvas1.create_window(200, 150, window=stop_btn)

program_label = tk.Label(root, fg='green', font=('helvetica', 12, 'bold'), text="Program pentru azi")
canvas1.create_window(150, 200, window=program_label)


if __name__ == "__main__":
    app = App()