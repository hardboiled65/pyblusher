from .observer import *
import tkinter as tk


class View:
    def __init__(self):
        self._attributes = Observable({
        })

    def _create_view(self, parent):
        self._view = Observer(self._attributes, tk.Frame,
            parent)
        self._view.instance.pack()
        print('View: pack()')

