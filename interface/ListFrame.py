from time import strftime
from tkinter import *


class ListFrame:
    def __init__(self, parent, data):
        self.current_date = strftime('%d.%m.%Y')
        self.window = Frame(bd=1, relief=SUNKEN)
        self.parent = parent
        self.data = data
        self.items_in_line = len(data[0])
        self.label_settings = {
            "padx": 10,
            "pady": 5,
            "bg": "#fff",
            "anchor": "w",
            "bd": 1,
            "relief": SUNKEN
        }
        self.initUI()

    def initUI(self):
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
        headings = ["Pagina", "Inceput Live", "Sfarsit Live", "Title"]
        for i in range(self.items_in_line):
            self.label(headings[i], row=0, column=i, lbl_cnf=lbl_cnf, grid_cnf=grid_cnf)

    def generate_list(self):
        row = 1
        grid_cnf = {
            "sticky": 'we',
        }
        ord = ["page", "start_time", "end_time", "title"]
        for item in self.data:
            item["title"] = self.set_title(item["title"])
            for key in range(self.items_in_line):
                self.label(item[ord[key]], row, key, self.label_settings, grid_cnf)
            row += 1

    def label(self, text, row, column, lbl_cnf, grid_cnf):
        Label(self.window, cnf=lbl_cnf, text=text).grid(row=row, column=column, cnf=grid_cnf)

    def set_title(self, title):
        return title.replace("::date::", self.current_date)
