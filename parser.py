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

        self._parse(uifile)

        # Debug print
        pprint(self._items)

    def _parse(self, uifile):
        tree = ElementTree.parse(uifile)
        root = tree.getroot()

        self.version = root.attrib['version']
        for child in root:
            # self._blui = Blui.Node()
            # self._blui.attributes
            for it in root.iter():
                self._items[it.tag] = {}
                for attr, val in it.attrib.items():
                    self._items[it.tag][attr] = val

    def keys(self):
        return self._items.keys()

    def items(self):
        return self._items.items()
