# -*- coding: utf-8 -*-
#  help.py: -*- Python -*-  DESCRIPTIVE TEXT.

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from util import *
from helpBA import HelpBA

class textbrowser(QTextBrowser):
    # reimplemented textbrowser that filters out external sources
    # future: launch web browser
    def __init__(self, parent=None, name=None):
        self.parent = parent
        QTextBrowser.__init__(self)


    def setSource(self, src):
        #print "setSource:", src
        s = str(src)
        if s[:7] == 'http://':
            launch_browser(s)
            return

        QTextBrowser.setSource(self, QUrl(src))
                
    
                

class Help(HelpBA):
    def __init__(self, parent, filename):
        HelpBA.__init__(self, parent)
        #Qt.WType_TopLevel | Qt.WDestructiveClose)

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
        #print "bool: ", bool
        self.fwdAvailable = bool


    def forwardHandler(self):
        #print "fwdAvail?: ", self.fwdAvailable
        if self.fwdAvailable:
            self.textBrowser.forward()
    
    def getHelpFile(self, filename):
        f = findFile(os.path.join("help", filename))
        return f
    

        
