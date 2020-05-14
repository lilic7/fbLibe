import os
from tkinter import *
from abc import ABC, abstractmethod
from interface.AppControl import AppControl


class AbstractFrame(ABC):
    def __init__(self, parent):
        self.window = Frame()
        self.parent = parent
        self.app_settings = AppControl.get_instance()

    @abstractmethod
    def init_ui(self):
        pass
