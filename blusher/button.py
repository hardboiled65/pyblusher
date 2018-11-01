from .view import View
from .observer import *
import tkinter as tk

class ButtonType:
    PushButton = 0

class Button(View):
    ButtonType = ButtonType

    def __init__(self, button_type=ButtonType.PushButton, title=None):
        super().__init__()
        self._attributes = Observable({
            'type': button_type,
            'title': title,
            'action': None,
        })

    @property
    def title(self):
        return self._attributes['title']

    @title.setter
    def title(self, value):
        self._attributes['title'] = value

    def _create_view(self, parent):
        self._view = Observer(self._attributes, tk.Button, parent)
        self._view.instance['text'] = self.title
        self._view.instance.pack()
        print('Button: pack()')

