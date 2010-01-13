from regexLibraryBA import RegexLibraryBA
from parseRegexLib import ParseRegexLib
from qt import *
from util import restoreWindowSettings, saveWindowSettings, kodos_toolbar_logo

import os

GEO = "regex-lib_geometry"

class RegexLibrary(RegexLibraryBA):
    def __init__(self, parent, filename):
        RegexLibraryBA.__init__(self, None)
        self.parent = parent
        self.filename = filename
        self.selected = None

        self.parseXML()

        self.populateListBox()
        kodos_toolbar_logo(self.toolBar)

        restoreWindowSettings(self, GEO) 

    def closeEvent(self, ev):
        saveWindowSettings(self, GEO)
        ev.accept()


    def parseXML(self):
        parser = ParseRegexLib(self.filename)
        self.xml_dicts = parser.parse()

        
    def populateListBox(self):
        for d in self.xml_dicts:
            self.descriptionListBox.insertItem(d.get('desc', "<unknown>"))

        
    def descSelectedSlot(self, qlistboxitem):
        if qlistboxitem == None: return

        itemnum = self.descriptionListBox.currentItem()
        self.populateSelected(self.xml_dicts[itemnum])


    def populateSelected(self, xml_dict):
        self.regexTextBrowser.setText(xml_dict.get('regex', ""))
        self.contribEdit.setText(xml_dict.get("contrib", ""))
        self.noteTextBrowser.setText(xml_dict.get('note', ""))
        self.selected = xml_dict

        
    def editPaste(self):
        if self.selected:
            self.parent.emit(PYSIGNAL('pasteRegexLib()'), (self.selected,) )





