import os
from datetime import datetime, date, time

class ScheduleItem:
    def __init__(self, item, today=True):
        self.today = today
        self.item = item
        self.start = datetime.strptime(self.item['start_time'], "%H:%M:%S")
        self.end = datetime.strptime(self.item['end_time'], "%H:%M:%S")

    def duration(self):
        return self.end - self.start

    def is_next(self):
        return self.start_time() > self.now()

    def start_now(self):
        return self.start_time() == self.now()

    def end_now(self):
        return self.end_time() == self.now()

    def remain_till_start(self):
        return self.start_time() - self.now()

    def remain_till_end(self):
        return self.end_time() - self.now()

    def finished(self):
        return self.end_time() < self.now()

    @staticmethod
    def now():
        return datetime.now().replace(microsecond=0)

    @staticmethod
    def date():
        return date.today()

    def start_time(self):
        start_time = time.fromisoformat(self.item['start_time'])
        return datetime.combine(self.date(), start_time)

    def end_time(self):
        end_time = time.fromisoformat(self.item['end_time'])
        return datetime.combine(self.date(), end_time)

