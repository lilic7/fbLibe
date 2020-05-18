import os

from obs.Obs import Obs
from live.FbLive import FbLive
from schedule.Schedule import Schedule


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
            print("toggle live status START")
            # self.go_live()
        else:
            print("toggle live status - STOP LIVE")
            # self.stop_live()

    def toggle_schedule_status(self):
        self.schedule_ON = not self.schedule_ON

    def schedule_job(self):
        if self.schedule_ON:
            time_remain = self.get_next_timer()
            if time_remain:
                return time_remain
            else:
                # print(" app control Go live ")
                self.toggle_live_status()
                return False

    def get_next_timer(self):
        return self.schedule.get_next_live_schedule(start=not self.live_ON)

    def go_live(self):
        stream_key = self.fb_live.create_live()
        self.obs.change_key(stream_key)
        self.obs.start_live()

    def stop_live(self):
        self.obs.end_live()
        self.fb_live.end_live()

    def test_init_times(self):
        self.schedule.test_generate_times()
