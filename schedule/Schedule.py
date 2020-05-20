import json
from datetime import datetime, time, date, timedelta
import time
import os

from schedule.ScheduleItem import ScheduleItem


class Schedule:
    def __init__(self):
        self.settings = self.read_json()["data"]
        self.test_data = []

    @staticmethod
    def read_json():
        filename = os.path.dirname(__file__) + '/settings.json'
        try:
            with open(filename) as settings:
                return json.load(settings)
        except FileNotFoundError:
            print(f"File '{filename}' does not exists")

    @staticmethod
    def set_title(title):
        return title.replace("::date::", time.strftime('%d.%m.%Y'))

    @staticmethod
    def get_current_day():
        return time.strftime("%a", time.gmtime())

    def check_default_program(self, day):
        default_days = self.settings[0]["default"]["days"]
        return default_days.count(day)

    def get_today_program(self):
        day = self.get_current_day()
        position = "default" if self.check_default_program(day) else day
        # print(self.settings[0][position]["program"])
        return self.settings[0][position]["program"]

    def ordered_program(self):
        program = self.get_today_program()
        return sorted(program, key=lambda item: item['start_time'])

    def process(self):
        # today_program = self.ordered_program()
        today_program = self.test_schedule()  # just for test. Remove when DONE
        # print(today_program)
        for live_item in today_program:
            scheduled_item = ScheduleItem(live_item)
            if scheduled_item.finished():
                continue
            if scheduled_item.is_next():
                return {
                    'status': "ready",
                    'time': scheduled_item.remain_till_start()
                }
            elif scheduled_item.start_now():
                return {
                    'status': "start_live",
                    'page': live_item['page'],
                    'title': self.set_title(live_item['title'])
                }
            elif scheduled_item.end_now():
                return {
                    "status": "end_live"
                }
            else:
                return {
                    "status": "live",
                    "time": scheduled_item.remain_till_end()
                }

        # TODO: schedule first item from tomorow list
        print("all items end")

    def test_schedule(self):
        return [
            {
                "start_time": f"{self.test_data[0]}",
                "end_time": f"{self.test_data[1]}",
                "page": "DevTest",
                "title": "Live Test 1 ::date::"
            },
            {
                "start_time": f"{self.test_data[2]}",
                "end_time": f"{self.test_data[3]}",
                "page": "Calatorii cu gust",
                "title": "Live Test 2 ::date::"
            }
        ]

    def test_generate_times(self):
        start_1 = datetime.now().replace(microsecond=0) + timedelta(seconds=10)
        self.test_data.append(str(start_1.time()))
        end_1 = datetime.now().replace(microsecond=0) + timedelta(seconds=30)
        self.test_data.append(str(end_1.time()))

        start_2 = datetime.now().replace(microsecond=0) + timedelta(seconds=50)
        self.test_data.append(str(start_2.time()))
        end_2 = datetime.now().replace(microsecond=0) + timedelta(seconds=120)
        self.test_data.append(str(end_2.time()))
