import tkinter as tk

class ButtonType:
    PushButton = 0

class Button:
    ButtonType = ButtonType

    def __init__(self, button_type=ButtonType.PushButton, title=None):
        print(Button)
        self._type = button_type
        self._title = title
        self._action = None

    @property
    def title(self):
        return self._title

    def _set_parent(self, parent):
        print('Button: _set_parent()')
        self._view = tk.Button(parent)
        self._view['text'] = self.title
        self._view.pack()
        print('Button: pack()')
