import json
from datetime import datetime, time, timedelta
import time
import os
from schedule.ScheduleItem import ScheduleItem


class Schedule:
    def __init__(self):
        self.settings = self.read_json()["data"]
        self.test_data = []
        self.program = self.ordered_program()
        self.day = True
        self.icons = self.settings[1]

    def toggle_day(self):
        self.day = not self.day

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
        return datetime.today().strftime("%a")

    @staticmethod
    def get_tomorrow():
        today = datetime.today()
        tomorrow = today.replace(day=today.day + 1)
        return tomorrow.strftime("%a")

    def check_default_program(self, day):
        default_days = self.settings[0]["default"]["days"]
        return default_days.count(day)

    def get_program(self, today=True):
        day = self.get_current_day() if today else self.get_tomorrow()
        position = "default" if self.check_default_program(day) else day
        return self.settings[0][position]["program"]

    def get_icons(self):
        return self.settings[1]['pages']

    def ordered_program(self, today=True):
        program = self.get_program(today)
        return sorted(program, key=lambda item: item['start_time'])

    def process(self):
        for live_item in self.program:
            scheduled_item = ScheduleItem(live_item, today=self.day)
            if scheduled_item.finished():
                continue
            if scheduled_item.is_next():
                return {
                    'status': "ready",
                    'time': scheduled_item.remain_till_start(),
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
        return {
            "status": "no_lives"
        }

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
