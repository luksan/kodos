# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

#-----------------------------------------------------------------------------#
# Installed modules

from PyQt4.QtCore import pyqtSignal

#-----------------------------------------------------------------------------#
# Kodos modules

from referenceBA import ReferenceBA
from util import kodos_toolbar_logo, restoreWindowSettings, saveWindowSettings

#-----------------------------------------------------------------------------#

GEO = "regex-ref_geometry"

class Reference(ReferenceBA):

    pasteSymbol = pyqtSignal(str)

    def __init__(self, parent):
        ReferenceBA.__init__(self, None)
        self.parent = parent

        restoreWindowSettings(self, GEO)
        kodos_toolbar_logo(self.toolBar)
        return


    def closeEvent(self, ev):
        saveWindowSettings(self, GEO)
        ev.accept()
        return


    def editPaste(self):
        list_view_item = self.referenceListView.currentItem()
        if list_view_item == None:
            return

        symbol = str(list_view_item.text(0))
        self.pasteSymbol.emit(symbol)
        return


    def help_slot(self):
        self.parent.helpHelp()
        return


    def help_python_slot(self):
        self.parent.helpPythonRegex()
        return

#-----------------------------------------------------------------------------#
