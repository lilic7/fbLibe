import os
import tkinter as tk
from time import strftime

from obs import Obs
from fbLive.live import FbLive
from scheduleLive.scheduleLive import ScheduleLive


# sc = ScheduleLive()
# program = sc.get_today_program()
# start_pos = 220
# current_date = strftime('%d.%m.%Y')
# i = 0
# for item in program:
#     title = item["title"].replace("::date::", current_date)
#     label = tk.Label(root, fg='black', font=('helvetica', 10, 'normal'), text=f'{title}').grid(row=i, column=0)
#     canvas1.create_window(100, start_pos, window=label)
#     start_pos += 30
#     i += 1

if __name__ == "__main__":
    root.mainloop()
