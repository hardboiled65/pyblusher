from xml.etree import ElementTree
from pprint import pprint

class Blui:
    class Node:
        def __init__(self):
            self.parent = None
            self.attributes = {}
            self.children = []

        def append(self, node):
            node.parent = self
            self.children.append(node)

    def __init__(self, uifile):
        self.version = ''
        self._items = {}
        self._blui = None
        self.__level = 0    # For debug print

        self._parse(uifile)

        # Debug print
        pprint(self._items)

    def _parse(self, uifile):
        tree = ElementTree.parse(uifile)
        root = tree.getroot()

        self.version = root.attrib['version']
        self._parse_child(root, None)
        '''
        for top in root:
            self._blui = Blui.Node()
            for attr, val in top.attrib.items():
                self._blui.attributes[attr] = val
            self._parse_child(top, self._blui)
        '''

    def _parse_child(self, el, node):
        self.__level += 1
        for child in el:
            print((' ' * (self.__level * 2)) + '- ' + child.tag)
            new_node = Blui.Node()
            new_node.parent = node
            if node is None:
                self._blui = Blui.Node()
                self._blui.append(new_node)
            else:
                node.append(new_node)
            for attr, val in child.attrib.items():
                new_node.attributes[attr] = val
            self._parse_child(child, new_node)
        self.__level -= 1

    def keys(self):
        return self._items.keys()

    def items(self):
        return self._items.items()
