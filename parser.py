from xml.etree import ElementTree
from pprint import pprint

class Blui:
    class Node:
        def __init__(self):
            self.parent = None
            self.class_name = ''
            self.attributes = {}
            self.children = []

        def append(self, node):
            node.parent = self
            self.children.append(node)

    def __init__(self, uifile):
        self.version = ''
        self._blui = None
        self.__level = 0    # For debug print

        self._parse(uifile)

        # Debug print
        # pprint(self._blui)

    @property
    def root(self):
        return self._blui

    def _parse(self, uifile):
        tree = ElementTree.parse(uifile)
        blusher_el = tree.getroot()

        self.version = blusher_el.attrib['version']
        self._parse_child(blusher_el, None)

    def _parse_child(self, el, node):
        self.__level += 1
        for child in el:
            # print((' ' * (self.__level * 2)) + '- ' + child.tag)
            new_node = Blui.Node()
            new_node.parent = node
            new_node.class_name = child.tag
            if node is None:
                self._blui = new_node
            else:
                node.append(new_node)
            for attr, val in child.attrib.items():
                new_node.attributes[attr] = val
            self._parse_child(child, new_node)
        self.__level -= 1

    @property
    def root(self):
        return self._blui

    def traverse(self, func, node=None):
        if node is None:
            node = self.root
        func(node)
        self.__level += 1
        for child in node.children:
            self.traverse(func, child)
        self.__level -= 1

    def __repr__(self):
        self._repr_text = '<blusher version: {}>\n'.format(self.version)
        def print_func(node):
            self._repr_text += (' ' * (self.__level * 2)) \
                + (node.class_name) \
                + ' ' + str(node.attributes) \
                + '\n'
        self.traverse(print_func)
        text = self._repr_text + '------------------------'
        self._repr_text = ''
        return text

