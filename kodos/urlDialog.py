# -*- coding: utf-8 -*-

from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QMessageBox
from . import urlDialogBA
from . import help
import urllib


class URLDialog(urlDialogBA.URLDialogBA):

    urlImported = pyqtSignal(str, str)

    def __init__(self, parent, url=None):
        urlDialogBA.URLDialogBA.__init__(self, parent)
        if url:
            self.URLTextEdit.setPlainText(url)

        self.show()

    def help_slot(self):
        self.helpWindow = help.Help(self, "importURL.html")

    def ok_slot(self):
        url = str(self.URLTextEdit.toPlainText())
        try:
            fp = urllib.urlopen(url)
            lines = fp.readlines()
        except Exception, e:
            QMessageBox.information(None, "Failed to open URL",
                                    "Could not open the specified URL.  Please check to ensure that you have entered the correct URL.\n\n%s" % str(e))
            return


        html = ''.join(lines)

        self.urlImported.emit(html, url)

        URLDialogBA.accept(self)
