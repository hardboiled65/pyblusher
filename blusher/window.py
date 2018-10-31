import tkinter as tk

class Window:
    class WindowType:
        MainWindow = 0
        PanelWindow = 1
        AlertWindow = 2

    class WindowState:
        Main = 0
        Key = 1
        Inactive = 2

    def __init__(self, window_type):
        self._type = window_type
        self._title = None
        self._x = 0
        self._y = 0

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, window_type):
        this._type = window_type

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def _set_parent(self, parent):
        print('Window: _set_parent()')
        self._view = tk.Frame(parent, height=100, width=100)
        self._view.pack()
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
