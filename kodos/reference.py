# -*- coding: utf-8 -*-
#  reference.py: -*- Python -*-  DESCRIPTIVE TEXT.

from PyQt5.QtCore import pyqtSignal
from . import referenceBA
from .util import kodos_toolbar_logo, restoreWindowSettings, saveWindowSettings

GEO = "regex-ref_geometry"

class Reference(referenceBA.ReferenceBA):

    pasteSymbol = pyqtSignal(str)

    def __init__(self, parent):
        referenceBA.ReferenceBA.__init__(self, None)
        self.parent = parent

        restoreWindowSettings(self, GEO)
        kodos_toolbar_logo(self.toolBar)


    def closeEvent(self, ev):
        saveWindowSettings(self, GEO)
        ev.accept()


    def editPaste(self):
        list_view_item = self.referenceListView.currentItem()
        if list_view_item == None:
            return

        symbol = str(list_view_item.text(0))
        self.pasteSymbol.emit(symbol)


    def help_slot(self):
        self.parent.helpHelp()

    def help_python_slot(self):
        self.parent.helpPythonRegex()
