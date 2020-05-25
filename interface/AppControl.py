import os

from obs.Obs import Obs
from live.FbLive import FbLive
from schedule.Schedule import Schedule
from PIL import ImageTk, Image


class AppControl:
    __instance = None

    @staticmethod
    def get_instance():
        if AppControl.__instance == None:
            AppControl()
        return AppControl.__instance

    def __init__(self):
        self.schedule_ON = False
        self.live_ON = False
        self.fb_live = FbLive()
        self.obs = Obs()
        self.schedule = Schedule()
        self.icons = self.schedule.get_icons()
        self.message = "Live OFF"

        if AppControl.__instance != None:
            raise Exception("AppSettings is singletone!")
        else:
            AppControl.__instance = self

    def is_live_active(self):
        return self.live_ON

    def is_schedule_active(self):
        return self.schedule_ON

    def toggle_live_status(self, page=None, live_title=None):
        self.live_ON = not self.live_ON
        if self.live_ON:
            self.message = "Live On"
            print("toggle live status START")
            self.go_live(page, live_title)
        else:
            self.message = "Live Off"
            print("toggle live status - STOP LIVE")
            self.stop_live()

    def toggle_schedule_status(self):
        self.schedule_ON = not self.schedule_ON

    def schedule_job(self):
        process = self.schedule.process()
        if process['status'] == "start_live" and not self.live_ON:
            self.toggle_live_status(process['page'], process['title'])
        if process['status'] == "end_live" and self.live_ON:
            self.toggle_live_status()
        if process['status'] == "no_lives" and self.schedule_ON:
            self.message = "Sfarsit program"
            self.toggle_schedule_status()
        return process

    def go_live(self, page, live_title):
        if page:
            self.fb_live.set_active_page(page)
        stream_key = self.fb_live.create_live(live_title)
        self.obs.change_key(stream_key)
        self.obs.start_live()

    def stop_live(self):
        self.obs.end_live()
        self.fb_live.end_live()

    def get_live_info(self):
        return self.fb_live.get_stream_status()

    def get_message(self):
        return self.message

    def get_icon(self, page):
        icon = list(filter(lambda item: item["title"] == self.item['page'], self.icons))[0]['icon']
        icon_path = os.path.dirname(__file__) + f"\\..\\data\\{icon}"
        return ImageTk.PhotoImage(Image.open(icon_path))