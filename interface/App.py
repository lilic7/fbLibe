import os
from tkinter import *
from time import strftime
from interface.ListFrame import ListFrame

from scheduleLive.scheduleLive import ScheduleLive


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.iconbitmap("../data/FB32x32.ico")
        self.initUI()
        self.window.mainloop()

    def initUI(self):
        data = ScheduleLive().get_today_program()
        listFrame = ListFrame(self.window, data).window.grid(row=8, column=0, columnspan=5)
        # list_frame = ListFrame(self.window).window
        # list_frame.grid(row=0, column=0)
        self.video_frame()
        self.video_info()
        self.live_control_buttons()
        self.time_label()

    def video_frame(self):
        video_label = Label(self.window, text="No video", padx=160, pady=90, bd=1, relief=SUNKEN, bg="#000000",
                            fg="#ffffff")
        video_label.grid(row=0, column=0, rowspan=5, columnspan=4, padx=2, pady=2)

    def video_info(self):
        framerate = Label(self.window, text="0 fps", padx=15)
        v_bitrate = Label(self.window, text="Video bit. 0 Mbps", padx=15)
        a_bitrate = Label(self.window, text="Audio bit. 0 Kbps", padx=15)
        framerate.grid(row=6, column=0, sticky=W + E)
        v_bitrate.grid(row=6, column=1, sticky=W + E)
        a_bitrate.grid(row=6, column=2, columnspan=2, sticky=W + E)

    def click(self, action):

        if action == "stop":
            control_btn = Button(self.window, text="Start Live", padx=btn_settings["padx"], pady=btn_settings["pady"],
                                 command=lambda: self.click("start"))
            control_btn.config(bg="#3b5998", fg=btn_settings['fg'], font=btn_settings['font'])
            control_btn.grid(row=7, column=0, columnspan=2, pady=10)
        if action == "start":
            self.control_btn.config()
            control_btn = Button(self.window, text="End Live", padx=btn_settings["padx"], pady=btn_settings["pady"],
                                 command=lambda: self.click("stop"))
            control_btn.config(bg="red", fg=btn_settings['fg'], font=btn_settings['font'])
            control_btn.grid(row=7, column=0, columnspan=2, pady=10)
        pass

    def live_control_buttons(self):
        btn_settings = {
            "font": ('calibri', 12, 'bold'),
            'fg': "#ffffff",
            'padx': 24,
            'pady': 5
        }
        start_live_btn = Button(self.window, text="Start Live", padx=btn_settings["padx"], pady=btn_settings["pady"],
                                  background="#3b5998", fg=btn_settings['fg'] ).grid(row=7, column=0, columnspan=2, pady=10)
        end_live_btn = Button(self.window, text="End Live", padx=btn_settings["padx"], pady=btn_settings["pady"],
                              background="red", fg=btn_settings['fg']).grid(row=7, column=1, columnspan=2, pady=10)

        # control_btn = Button(self.window, text="Start Live", padx=btn_settings["padx"], pady=btn_settings["pady"], command=lambda: self.click("start"))
        # control_btn.config(bg="#3b5998", fg=btn_settings['fg'], font=btn_settings['font'])
        # control_btn.grid(row=7, column=0, columnspan=2, pady=10)

    def time_label(self):
        self.t_label = Label(self.window, font=('calibri', 28, 'bold'), fg='black')
        self.t_label.grid(row=0, column=5)
        self.time()

    def time(self):
        string = strftime('%H:%M:%S')
        self.t_label.config(text=string)
        self.t_label.after(1000, self.time)


#
# canvas1 = tk.Canvas(self.root, width=400, height=500)
# canvas1.pack()
# fbLive = FbLive("DevTest")
# signal_status_id = 0
#
#
# def start_live():
#     stream_key = fbLive.create_live()
#     obs = Obs()
#     obs.change_key(stream_key)
#     obs.start_live()
#     page = fbLive.get_active_page()


#
# def end_live():
#     os.system("taskkill /F /IM obs64.exe")
#     fbLive.end_live()
#     label['text'] = "Live terminat"
#     root.after_cancel(signal_status_id)
#     stream_framerate.config(text='')
#     stream_vbitrate.config(text='')
#     stream_abitrate.config(text='')
#
#

#
#
# time_label = tk.Label(root, font=('calibri', 40, 'bold'), foreground='black')
# canvas1.create_window(150, 50, window=time_label)
# time()
#
#
# # ==================
# def stream_status():
#     data = fbLive.get_stream_status()
#     if "framerate" in data:
#         stream_size.config(text=f'FR: {data["size"]}')
#         stream_framerate.config(text=f'FR: {data["framerate"]}')
#         stream_vbitrate.config(text=f'VB: {data["v_bitrate"]}')
#         stream_abitrate.config(text=f'AB: {data["a_bitrate"]}')
#     stream_framerate.after(5000, stream_status)
#
#
# stream_info = tk.LabelFrame(root, foreground='black', text="Stream info")
# canvas1.create_window(160, 350, window=stream_info)
#
# stream_size = tk.Label(root, font=('calibri', 12, 'normal'), foreground='black', text="444x333")
# stream_framerate = tk.Label(root, font=('calibri', 12, 'normal'), foreground='black', text="FR: 34")
# stream_vbitrate = tk.Label(root, font=('calibri', 12, 'normal'), foreground='black')
# stream_abitrate = tk.Label(root, font=('calibri', 12, 'normal'), foreground='black')
# canvas1.create_window(50, 465, window=stream_size)
# canvas1.create_window(50, 490, window=stream_framerate)
# canvas1.create_window(150, 490, window=stream_vbitrate)
# canvas1.create_window(250, 490, window=stream_abitrate)
# # ===========
#
# label = tk.Label(root, fg='green', font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 100, window=label)
#
# start_btn = tk.Button(text='Start', command=start_live, bg='brown', fg='white', font="16")
# canvas1.create_window(100, 150, window=start_btn)
#
# stop_btn = tk.Button(text='Stop', command=end_live, bg='brown', fg='white', font="16")
# canvas1.create_window(200, 150, window=stop_btn)
#
# program_label = tk.Label(root, fg='green', font=('helvetica', 12, 'bold'), text="Program pentru azi")
# canvas1.create_window(150, 200, window=program_label)


if __name__ == "__main__":
    app = App(Tk(), "Facebook Live Manager")
