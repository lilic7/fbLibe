from tkinter import Label

from interface.AbstractFrame import AbstractFrame


class InfoFrame(AbstractFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # self.icon_lbl = Label(self.window)

        self.message_lbl = Label(self.window)

        self.framerate_lbl = Label(self.window)
        self.v_bitrate_lbl = Label(self.window)
        self.a_bitrate_lbl = Label(self.window)
        self.init_ui()

    def init_ui(self):
        info_label_cnf = {
            "padx": 15,
        }
        grid_cnf = {
            "row": 2,
            "sticky": 'we',
        }

        # self.icon_lbl.config(cnf=info_label_cnf, text="No image")
        # self.icon_lbl.grid(row=0, column=0)
        # self.update_icon()

        self.framerate_lbl.config(cnf=info_label_cnf, text="0 fps")
        self.v_bitrate_lbl.config(cnf=info_label_cnf, text="Video bit. 0 Mbps")
        self.a_bitrate_lbl.config(cnf=info_label_cnf, text="Audio bit. 0 Kbps")

        self.framerate_lbl.grid(cnf=grid_cnf, column=0)
        self.v_bitrate_lbl.grid(cnf=grid_cnf, column=1)
        self.a_bitrate_lbl.grid(cnf=grid_cnf, column=2)

        self.message_lbl.config(cnf=info_label_cnf, text="Live Off", font=('calibri', 18, 'bold'), fg="blue")
        self.message_lbl.grid(row=1, columnspan=3, pady=20)

        self.update_info_label()

    def update_info_label(self):
        self.message_lbl['text'] = self.app_settings.get_message()

        if self.app_settings.is_live_active():
            self.message_lbl['text'] = self.app_settings.get_message()
            data = self.app_settings.get_live_info()
            if 'framerate' in data:
                self.framerate_lbl['text'] = f"{data['framerate']} fps"
                self.v_bitrate_lbl['text'] = f"Video bit. {data['v_bitrate']} Mbps"
                self.a_bitrate_lbl['text'] = f"Audio bit. {data['a_bitrate']} Kbps"
        else:
            self.framerate_lbl['text'] = f"0 fps"
            self.v_bitrate_lbl['text'] = f"Video bit. 0 Mbps"
            self.a_bitrate_lbl['text'] = f"Audio bit. 0 Kbps"

        self.framerate_lbl.after(3000, self.update_info_label)

    # def update_icon(self):
    #     if self.app_settings.is_schedule_active():
    #         icon = self.app_settings.get_icon()
    #         self.icon_lbl.config(image=icon, text='')
    #     else:
    #         self.icon_lbl.config(image="", text='no image')
    #
    #     self.icon_lbl.after(1000, self.update_icon)
