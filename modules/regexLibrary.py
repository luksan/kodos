# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

#-----------------------------------------------------------------------------#
# Installed modules

from PyQt4 import QtCore

#-----------------------------------------------------------------------------#
# Kodos modules

from .regexLibraryBA import RegexLibraryBA
from .parseRegexLib import ParseRegexLib
from .util import restoreWindowSettings, saveWindowSettings, kodos_toolbar_logo

#-----------------------------------------------------------------------------#

GEO = "regex-lib_geometry"

class RegexLibrary(RegexLibraryBA):

    pasteRegexLib = QtCore.pyqtSignal(dict)

    def __init__(self, filename):
        RegexLibraryBA.__init__(self, None)
        self.filename = filename
        self.selected = None

        self.parseXML()

        self.populateListBox()
        kodos_toolbar_logo(self.toolBar)

        restoreWindowSettings(self, GEO)
        return


    def closeEvent(self, ev):
        saveWindowSettings(self, GEO)
        ev.accept()
        return


    def parseXML(self):
        parser = ParseRegexLib(self.filename)
        self.xml_dicts = parser.parse()
        return


    def populateListBox(self):
        for d in self.xml_dicts:
            self.descriptionListBox.addItem(d.get('desc', "<unknown>"))
        return


    def descSelectedSlot(self, qlistboxitem):
        if qlistboxitem == None: return

        itemnum = self.descriptionListBox.currentRow()
        self.populateSelected(self.xml_dicts[itemnum])
        return


    def populateSelected(self, xml_dict):
        self.regexTextBrowser.setPlainText(xml_dict.get('regex', ""))
        self.contribEdit.setText(xml_dict.get("contrib", ""))
        self.noteTextBrowser.setPlainText(xml_dict.get('note', ""))
        self.selected = xml_dict
        return


    def editPaste(self):
        if self.selected:
            self.pasteRegexLib.emit(self.selected)
        return

#-----------------------------------------------------------------------------#
