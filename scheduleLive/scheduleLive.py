import json
import datetime
import time
import os


class ScheduleLive:
    def __init__(self):
        self.settings = self.read_json()["data"]

    @staticmethod
    def read_json():
        filename = os.path.dirname(__file__)+'/settings.json'
        try:
            with open(filename) as settings:
                return json.load(settings)
        except FileNotFoundError:
            print(f"File '{filename}' does not exists")

    @staticmethod
    def get_current_day():
        return time.strftime("%a", time.gmtime())

    def check_default_program(self, day):
        default_days = self.settings[0]["default"]["days"]
        return default_days.count(day)

    def get_today_program(self):
        day = self.get_current_day()
        position = "default" if self.check_default_program(day) else day
        return self.settings[0][position]["program"]

    def get_next_live_schedule(self):
        today_program = self.get_today_program()
        now = time.localtime()
        for item in today_program:
            item_time = time.strptime(f"{now.tm_year}-{now.tm_mon}-{now.tm_mday}-{item['start_time']}", "%Y-%m-%d-%H:%M:%S")
            if item_time > now:
                # print(item_time, now, item)
                return item
