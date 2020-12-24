# -*- coding: utf-8 -*-
from PyQt4.QtCore import pyqtSignal
from regexLibraryBA import RegexLibraryBA
from parseRegexLib import ParseRegexLib
from util import restoreWindowSettings, saveWindowSettings, kodos_toolbar_logo

GEO = "regex-lib_geometry"

class RegexLibrary(RegexLibraryBA):

    pasteRegexLib = pyqtSignal(dict)

    def __init__(self, filename):
        RegexLibraryBA.__init__(self, None)
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
            self.descriptionListBox.addItem(d.get('desc', "<unknown>"))


    def descSelectedSlot(self, qlistboxitem):
        if qlistboxitem == None: return

        itemnum = self.descriptionListBox.currentRow()
        self.populateSelected(self.xml_dicts[itemnum])


    def populateSelected(self, xml_dict):
        self.regexTextBrowser.setPlainText(xml_dict.get('regex', ""))
        self.contribEdit.setText(xml_dict.get("contrib", ""))
        self.noteTextBrowser.setPlainText(xml_dict.get('note', ""))
        self.selected = xml_dict


    def editPaste(self):
        if self.selected:
            self.pasteRegexLib.emit(self.selected)





