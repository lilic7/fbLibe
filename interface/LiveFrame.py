import os
from tkinter import *
from fbLive.live import FbLive
from obs import Obs


class LiveFrame:
    def __init__(self, parent):
        self.window = Frame()
        self.parent = parent
        self.info_label_cnf = {
            "padx": 15,
        }
        self.framerate_label = Label(self.window)
        self.v_bitrate_label = Label(self.window)
        self.a_bitrate_label = Label(self.window)

        self.start_btn = Button(self.window)
        self.end_btn = Button(self.window)
        self.schedule_btn = Button(self.window)

        self.schedule_ON = False
        self.live_ON = False
        self.fbLive = FbLive("DevTest")

        self.initUI()

    def initUI(self):
        self.video_frame()
        self.video_info()
        self.live_control_buttons()

    def video_frame(self):
        label_cnf = {
            "padx": 160,
            "pady": 90,
            "bg": "#000000",
            "fg": "#ffffff",
        }
        grid_cnf = {
            "row": 0,
            "column": 0,
            "columnspan": 6,
            "padx": 20,
        }
        Label(self.window, text="No video", cnf=label_cnf).grid(cnf=grid_cnf)

    def video_info(self):
        grid_cnf = {
            "row": 1,
            "sticky": 'we',
            "columnspan": 2
        }
        texts = ["0 fps"]
        self.framerate_label["text"] = "0 fps"
        self.v_bitrate_label["text"] = "Video bit. 0 Mbps"
        self.a_bitrate_label["text"] = "Audio bit. 0 Kbps"
        self.framerate_label.grid(cnf=grid_cnf, column=0, )
        self.v_bitrate_label.grid(cnf=grid_cnf, column=2)
        self.a_bitrate_label.grid(cnf=grid_cnf, column=4)

    def update_info_label(self, data):
        self.framerate_label['text'] = data['framerate']
        self.v_bitrate_label['text'] = data['v_bitrate']
        self.a_bitrate_label['text'] = data['a_bitrate']

    def live_control_buttons(self):
        btn_settings = {
            "font": ('calibri', 12, 'bold'),
            'fg': "#ffffff",
            'padx': 24,
            'pady': 5
        }
        grid_cnf = {
            "row": 2,
            "pady": 10,
            "columnspan": 2
        }
        self.start_btn.config(text="Start Live", background="#3b5998", cnf=btn_settings, command=self.start_btn_click)
        self.start_btn.grid(column=0, cnf=grid_cnf)

        self.end_btn.config(text="End Live", background="#aaa", cnf=btn_settings, command=self.end_btn_click,
                            state=DISABLED)
        self.end_btn.grid(column=2, cnf=grid_cnf)

        self.schedule_btn.config(text="Use program", background="Yellow", fg="#000", cnf=btn_settings)
        self.schedule_btn.bind("<Button-1>", self.schedule_toggle)
        self.schedule_btn.grid(column=4, cnf=grid_cnf)

    # initial
    # end - disabled

    # start press
    #     live_ON = True
    #     start OFF
    #     end ON
    #     schedule OFF + schedule_ON=False

    # end press
    #     live_ON = False
    #     if schedule_ON = True
    #         start OFF
    #     else start ON
    #     end OFF

    def schedule_toggle(self, event):
        self.schedule_ON = not self.schedule_ON
        if self.schedule_ON:
            self.start_btn.config(state=DISABLED, background="#aaa")
            self.end_btn.config(state=NORMAL, background="red")
            self.schedule_btn.config(background="green")
        else:
            self.start_btn.config(state=NORMAL, background="#3b5998")
            self.schedule_btn.config(background="yellow")
            self.end_btn.config(state=DISABLED, background="#aaa")

    def start_btn_click(self):
        self.live_ON = not self.live_ON
        self.check_live_status()
        stream_key = self.fbLive.create_live()
        obs = Obs()
        obs.change_key(stream_key)
        obs.start_live()
        page = self.fbLive.get_active_page()

    def end_btn_click(self):
        self.live_ON = False
        os.system("taskkill /F /IM obs64.exe")
        self.fbLive.end_live()
        self.check_live_status()

    def check_live_status(self):
        if not self.schedule_ON and self.live_ON:
            self.start_btn.config(state=DISABLED, background="#aaa")
            self.end_btn.config(state=NORMAL, background="red")
        else:
            self.start_btn.config(state=NORMAL, background="#3b5998")
            self.end_btn.config(state=DISABLED, background="#aaa")
