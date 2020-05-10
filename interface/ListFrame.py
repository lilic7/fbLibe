from time import strftime
from tkinter import *


class ListFrame:
    def __init__(self, parent, data):
        self.current_date = strftime('%d.%m.%Y')
        self.window = Frame()
        self.parent = parent
        self.data = data
        self.initUI()

    def initUI(self):
        Label(self.window, text="Pagina", font=('calibri', 12, 'bold'), padx=10).grid(row=0, column=0)
        Label(self.window, text="Inceput Live", font=('calibri', 12, 'bold'), padx=10).grid(row=0, column=1)
        Label(self.window, text="Sfarsit Live", font=('calibri', 12, 'bold'), padx=10).grid(row=0, column=2)
        Label(self.window, text="Titlu", font=('calibri', 12, 'bold'), padx=10).grid(row=0, column=3, sticky='w')
        row = 1
        for item in self.data:
            self.setLine(item, row)
            row += 1

    def set_title(self, title):
        return title.replace("::date::", self.current_date)

    def setLine(self, item, row=0):
        return {
            "item_page": Label(self.window, text=item['page'], font=('calibri', 12, 'bold'), padx=10).grid(row=row,
                                                                                                           column=0),
            "item_start": Label(self.window, text=item['start_time'], padx=10).grid(row=row, column=1),
            "item_end": Label(self.window, text=item['end_time'], padx=10).grid(row=row, column=2),
            "item_title": Label(self.window, text=self.set_title(item['title']), padx=10).grid(row=row, column=3,
                                                                                               sticky='w')
        }
