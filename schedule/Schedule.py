import json
from datetime import datetime, time, date
import time
import os


class Schedule:
    def __init__(self):
        self.settings = self.read_json()["data"]

    @staticmethod
    def read_json():
        filename = os.path.dirname(__file__) + '/settings.json'
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

    def ordered_program(self):
        program = self.get_today_program()
        return sorted(program, key=lambda item: item['start_time'])

    def get_next_live_schedule(self):
        today_program = self.ordered_program()
        ymd = date.today()
        now = datetime.now().replace(microsecond=0)
        for live_item in today_program:
            hms = time.strptime(live_item['start_time'], "%H:%M:%S")
            dt = datetime(ymd.year, ymd.month, ymd.day, hms.tm_hour, hms.tm_min, hms.tm_sec)
            if dt > now:
                return dt - now
                # time_remains = dt - now
                # print(time_remains)
            # elif dt <= now:
            #     print(f"{live_item['title']} go live")
            # break
        return False
