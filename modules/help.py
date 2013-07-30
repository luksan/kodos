# -*- coding: utf-8 -*-
#  help.py: -*- Python -*-  DESCRIPTIVE TEXT.

import os

from PyQt4 import QtGui
from PyQt4 import QtCore

from . import util
from helpBA import HelpBA

class textbrowser(QtGui.QTextBrowser):
    # reimplemented textbrowser that filters out external sources
    # future: launch web browser
    def __init__(self, parent=None, name=None):
        self.parent = parent
        QtGui.QTextBrowser.__init__(self)
        return


    def setSource(self, src):
        s = str(src)
        if s[:7] == 'http://':
            util.launch_browser(s)
            return

        QtGui.QTextBrowser.setSource(self, QtCore.QUrl(src))
        return


class Help(HelpBA):
    def __init__(self, parent, filename):
        HelpBA.__init__(self, parent)

        self.setGeometry(100, 50, 800, 600)

        self.textBrowser = textbrowser(self)
        absPath = self.getHelpFile(filename)

        self.setCentralWidget(self.textBrowser)
        self.textBrowser.setSource(absPath)

        self.fwdAvailable = 0
        self.show()
        return


    def exitSlot(self):
        self.close()
        return


    def backSlot(self):
        self.textBrowser.backward()
        return


    def forwardSlot(self):
        self.textBrowser.forward()
        return


    def homeSlot(self):
        self.textBrowser.home()
        return


    def setForwardAvailable(self, bool):
        self.fwdAvailable = bool
        return


    def forwardHandler(self):
        if self.fwdAvailable:
            self.textBrowser.forward()
        return


    def getHelpFile(self, filename):
        f = util.findFile(os.path.join("help", filename))
        return f

