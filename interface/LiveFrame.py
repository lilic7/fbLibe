from tkinter import *
from interface.AbstractFrame import AbstractFrame


class LiveFrame(AbstractFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.video_label = Label(self.window)
        self.framerate_label = Label(self.window)
        self.v_bitrate_label = Label(self.window)
        self.a_bitrate_label = Label(self.window)

        self.live_btn = Button(self.window, text="Start Live")
        self.schedule_btn = Button(self.window, text="Programat")
        self.init_ui()

    def init_ui(self):
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
        self.video_label.config(text="No video", cnf=label_cnf)
        self.video_label.grid(cnf=grid_cnf)

    def video_info(self):
        info_label_cnf = {
            "padx": 15,
        }
        grid_cnf = {
            "row": 1,
            "sticky": 'we',
            "columnspan": 2
        }
        self.framerate_label.config(cnf=info_label_cnf, text="0 fps")
        self.v_bitrate_label.config(cnf=info_label_cnf, text="Video bit. 0 Mbps")
        self.a_bitrate_label.config(cnf=info_label_cnf, text="Audio bit. 0 Kbps")

        self.framerate_label.grid(cnf=grid_cnf, column=0)
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
            "columnspan": 3
        }
        self.live_btn.config(cnf=btn_settings, command=self.btn_click)
        self.live_btn.grid(column=0, cnf=grid_cnf)

        self.schedule_btn.config(bg="Yellow", fg="#000", cnf=btn_settings, command=self.schedule_toggle)
        self.schedule_btn.grid(column=3, cnf=grid_cnf)

        self.btn_status()

    def btn_status(self):
        if self.app_settings.is_schedule_active():
            self.schedule_btn.config(bg="green")
            if self.app_settings.is_live_active():
                self.live_btn.config(state=NORMAL, bg="red", text="End Live")
            else:
                self.live_btn.config(state=DISABLED, bg="#ccc", text="Start Live")
        else:
            self.schedule_btn.config(bg="yellow")
            if self.app_settings.is_live_active():
                self.live_btn.config(state=NORMAL, bg="red", text="End Live")
            else:
                self.live_btn.config(state=NORMAL, bg="#3b5998", text="Start Live")
        self.window.after(1000, self.btn_status)
            
    def schedule_toggle(self):
        self.app_settings.toggle_schedule_status()
        if self.app_settings.is_schedule_active():
            self.live_btn.config(state=DISABLED, bg="#ccc")
            self.schedule_btn.config(background="green")
        else:
            self.live_btn.config(state=NORMAL, bg="#3b5998")
            self.schedule_btn.config(background="yellow")

    def btn_click(self):
        self.app_settings.toggle_live_status()
        self.btn_status()
