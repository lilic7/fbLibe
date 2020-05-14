import json
from datetime import datetime, time
import time
import os


class Schedule:
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
        now = datetime.today()
        dt = datetime.today()
        for item in today_program:
            item_time = datetime.strptime(f"{dt.date()} {item['start_time']}", "%Y-%m-%d %H:%M:%S")
            # print('item_time', item_time)
            # print("now", now)
            if item_time > now:
                # print(f"{item_time} greater", now, item)
                return item
            else:
                # item_time = time.strptime(f"{now.tm_year}-{now.tm_mon}-{now.tm_mday+1}-{item['start_time']}",
                #                           "%Y-%m-%d-%H:%M:%S")
                # print(f"{item_time} lower", now, item)
                return item


