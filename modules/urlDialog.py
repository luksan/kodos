# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

#-----------------------------------------------------------------------------#
# Built-in modules

import urllib

#-----------------------------------------------------------------------------#
# Installed modules

from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QMessageBox

#-----------------------------------------------------------------------------#
# Kodos modules

from .urlDialogBA import URLDialogBA
from . import help

#-----------------------------------------------------------------------------#

class URLDialog(URLDialogBA):

    urlImported = pyqtSignal(str, str)

    def __init__(self, parent, url=None):
        URLDialogBA.__init__(self, parent)
        if url:
            self.URLTextEdit.setPlainText(url)

        self.show()
        return


    def help_slot(self):
        self.helpWindow = help.Help(self, "importURL.html")
        return


    def ok_slot(self):
        url = str(self.URLTextEdit.toPlainText())
        try:
            fp = urllib.urlopen(url)
            lines = fp.readlines()
        except Exception as e:
            QMessageBox.information(None, "Failed to open URL",
                "Could not open the specified URL.  Please check to ensure \
                that you have entered the correct URL.\n\n{0}".format(str(e)))
            return


        html = ''.join(lines)

        self.urlImported.emit(html, url)

        URLDialogBA.accept(self)
        return

#-----------------------------------------------------------------------------#
