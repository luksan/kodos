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


    def setSource(self, src):
        s = str(src)
        if s[:7] == 'http://':
            util.launch_browser(s)
            return

        QtGui.QTextBrowser.setSource(self, QtCore.QUrl(src))




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


    def exitSlot(self):
        self.close()

    def backSlot(self):
        self.textBrowser.backward()

    def forwardSlot(self):
        self.textBrowser.forward()

    def homeSlot(self):
        self.textBrowser.home()



    def setForwardAvailable(self, bool):
        self.fwdAvailable = bool


    def forwardHandler(self):
        if self.fwdAvailable:
            self.textBrowser.forward()

    def getHelpFile(self, filename):
        f = util.findFile(os.path.join("help", filename))
        return f



