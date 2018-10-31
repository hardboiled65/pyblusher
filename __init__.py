from . import blusher
from . import parser
import tkinter as tk

Window = blusher.Window
Button = blusher.Button

class Ui:
    def __init__(self, uifile):
        blui = parser.Blui(uifile)

        for k, v in blui.items():
            instance = Window(Window.WindowType.MainWindow)
            if v.get('title') is not None:
                instance._title = v['title']
            setattr(self, v['instance'], instance)

class Application(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)

    def set_view(self, view):
        print('Application: set_view()')
        self._root_view = view
        view._set_parent(self)

    def run(self):
        if hasattr(self._root_view, 'title'):
            if self._root_view.title is not None:
                self.title(self._root_view.title)
        print('Application: run()')
        self.mainloop()

