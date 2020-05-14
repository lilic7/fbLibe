from time import strftime
from tkinter import *
from interface.AbstractFrame import AbstractFrame

class ListFrame(AbstractFrame):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.data = data
        self.items_in_line = len(data[0])
        self.init_ui()

    def init_ui(self):
        self.window.config(bd=1, relief=SUNKEN)
        self.headings()
        self.generate_list()

    def headings(self):
        lbl_cnf = {
            "font": ('calibri', 12, 'bold'),
            "padx": 10,
            "anchor": "w"
        }
        grid_cnf = {
            "row": 0,
            "sticky": 'we'
        }
        headings = ["Pagina", "Inceput Live", "Sfarsit Live", "Titlu"]
        for i in range(self.items_in_line):
            Label(self.window,
                  cnf=lbl_cnf,
                  text=headings[i]).grid(cnf=grid_cnf, column=i)

    def generate_list(self):
        row = 1
        for item in self.data:
            item["title"] = self.set_title(item["title"])
            for column_num in range(self.items_in_line):
                self.generate_label(item, row, column_num)
            row += 1

    def generate_label(self, item, row, column):
        label_settings = {
            "padx": 10,
            "pady": 5,
            "bg": "#fff",
            "anchor": "w",
            "bd": 1,
            "relief": SUNKEN
        }
        grid_cnf = {
            "sticky": 'we',
        }
        labels_order = ["page", "start_time", "end_time", "title"]
        Label(self.window,
              text=item[labels_order[column]],
              cnf=label_settings).grid(row=row, column=column, cnf=grid_cnf)

    @staticmethod
    def set_title(title):
        return title.replace("::date::", strftime('%d.%m.%Y'))
