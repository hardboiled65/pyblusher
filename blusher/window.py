from pyblusher.blusher import Button
from .view import View
from .observer import *
import tkinter as tk


class Window(View):
    class WindowType:
        MainWindow = 0
        PanelWindow = 1
        AlertWindow = 2

    class WindowState:
        Main = 0
        Key = 1
        Inactive = 2

    def __init__(self, window_type):
        super().__init__()
        self._attributes = Observable({
            'type': window_type,
            'title': None,
            'x': 0,
            'y': 0,
        })

    @property
    def type(self):
        return self._attributes['type']

    @type.setter
    def type(self, window_type):
        self._attributes['type'] = window_type

    @property
    def title(self):
        return self._attributes['title']

    @title.setter
    def title(self, title):
        self._attributes['title'] = title

    def _create_view(self, parent):
        self._view = Observer(self._attributes, tk.Frame,
            parent, height=100, width=100)
        self._view.instance.pack()
        print('Window: pack()')


class Alert(Window):
    def __init__(self, message=None, informative_text='This is an alert'):
        super().__init__(Window.WindowType.AlertWindow)

        self._message = message
        self._informative_text = informative_text
        self._buttons = []

        # Set default buttons.
        self._buttons.append(Button(title='Ok'))
        self._buttons.append(Button(title='Cancel'))

    @property
    def message(self):
        return self._message

    @property
    def informative_text(self):
        return self._informative_text

    @property
    def buttons(self):
        return self._buttons
