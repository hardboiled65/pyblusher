from . import blusher
from . import parser
from . import view_model
import tkinter as tk

ViewModel = view_model.ViewModel

View = blusher.View
Window = blusher.Window
Button = blusher.Button


class Ui:
    def __init__(self, blui=None, root=None):
        self._ui_tree = parser.Blui(blui)
        print(self._ui_tree)
        self.instances = {}

        if root is not None:
            for child in self._ui_tree.root.children:
                self.create_instance(child)
        else:
            self.create_instance(self._ui_tree.root)
        '''
        for k, v in blui.items():
            instance = Window(Window.WindowType.MainWindow)
            if v.get('title') is not None:
                instance._title = v['title']
            setattr(self, self.get_instance_name(v), instance)
        '''

    @staticmethod
    def get_instance_name(node):
        name = node.attributes.get('instance')
        if name is None:
            name = 'rt_{}'.format(id(node))
        return name

    def create_instance(self, node):
        # print('create_instance: {}'.format(node.class_name))

        # Get Blusher class.
        cls = get_class(node.class_name)
        instance_name = self.get_instance_name(node)
        args = []
        if node.class_name == 'Window':
            args.append(Window.WindowType.MainWindow)
        instance = cls(*args)
        self.instances[instance_name] = instance
        for child in node.children:
            self.create_instance(child)

    @property
    def args(self):
        root = self._ui_tree.root
        args = []
        '''
        if root.attributes.get('type'):
            if root.class_name == 'Window':
        '''
        if root.class_name == 'Window':
            if root.attributes.get('type') is None:
                args.append(Window.WindowType.MainWindow)
        return args

    def __repr__(self):
        text = '<pyblusher.Ui>\n'
        for k, v in self.instances.items():
            text += ' {}: {}\n'.format(k, v)
        return text

    def set(self, target):
        for instance_name in self.instances.keys():
            setattr(target, instance_name, self.instances[instance_name])


class Application(tk.Tk):
    def __init__(self, ui=None):
        super().__init__(None)
        self.ui = ui

    def set_view(self, view):
        print('Application: set_view()')
        self.title('Application')
        self._root_view = view
        if hasattr(self._root_view, 'title'):
            if self._root_view.title is not None:
                self.title(self._root_view.title)
        if self.ui is not None:
            self._create_views(self.ui._ui_tree.root)

    def _create_views(self, tree):
        parent = self
        self._root_view._create_view(self)
        for child in tree.children:
            instance = self.ui.instances[self.ui.get_instance_name(child)]
            instance._create_view(parent)
            # parent = instance._view

    def run(self):
        print('Application: run()')
        self.mainloop()


def get_class(cls_name):
    if cls_name == 'Window':
        return Window
    elif cls_name == 'Button':
        return Button
    print('Not matched class for the name: {}.'.format(cls_name))
    return View
