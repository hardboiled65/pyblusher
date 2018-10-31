from xml.etree import ElementTree
from pprint import pprint

class Blui:
    def __init__(self, uifile):
        self.version = ''
        self._items = {}

        tree = ElementTree.parse(uifile)
        root = tree.getroot()

        self.version = root.attrib['version']
        for child in root:
            self._items[child.tag] = {}
            for attr, val in child.attrib.items():
                self._items[child.tag][attr] = val

        # Debug print
        pprint(self._items)

    def keys(self):
        return self._items.keys()

    def items(self):
        return self._items.items()
