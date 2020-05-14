import os

from obs.Obs import Obs
from live.FbLive import FbLive


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

        if AppControl.__instance != None:
            raise Exception("AppSettings is singletone!")
        else:
            AppControl.__instance = self

    def get_live_status(self):
        return self.live_ON

    def get_schedule_status(self):
        return self.schedule_ON

    def toggle_live_status(self):
        self.live_ON = not self.live_ON
        if self.live_ON:
            self.go_live()
        else:
            self.stop_live()

    def toggle_schedule_status(self):
        self.schedule_ON = not self.schedule_ON

    def go_live(self):
        stream_key = self.fb_live.create_live()
        obs = Obs()
        obs.change_key(stream_key)
        obs.start_live()

    def stop_live(self):
        os.system("taskkill /F /IM obs64.exe")
        self.fb_live.end_live()