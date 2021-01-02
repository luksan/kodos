# -*- coding: utf-8 -*-
#  help.py: -*- Python -*-  DESCRIPTIVE TEXT.

import os

from PyQt5.QtWidgets import QTextBrowser, QMainWindow
from PyQt5.QtCore import QUrl

from . import util
from . import helpBA

class textbrowser(QTextBrowser):
    # reimplemented textbrowser that filters out external sources
    # future: launch web browser
    def __init__(self, parent=None, name=None):
        self.parent = parent
        QTextBrowser.__init__(self)


    def setSource(self, src):
        s = str(src)
        if s[:7] == 'http://':
            util.launch_browser(s)
            return

        QTextBrowser.setSource(self, QUrl(src))




class Help(QMainWindow, helpBA.Ui_HelpBA):
    def __init__(self, parent, filename):
        super(Help, self).__init__(parent=parent)
        self.setupUi(self)
        self.parent = parent

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



