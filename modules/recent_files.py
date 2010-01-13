
from util import getHomeDirectory
import os
import string
from qt import *
import xpm

MAX_SIZE = 50 # max number of files to retain

class RecentFiles:
    def __init__(self, parent, numShown=5, debug=None):
        self.parent = parent
        self.numShown = int(numShown)
        self.debug = debug
        self.filename = getHomeDirectory() + os.sep + ".kodos" + os.sep + "recent_files"
        self.__recent_files = []
        self.__indecies = []
        self.load()


    def load(self):
        try:
            fp = open(self.filename, "r")
            self.__recent_files = map(string.strip, fp.readlines())
        except Exception, e:
            #print "Warning: ", str(e)
            return
        
        if self.debug: print "recent_files:", self.__recent_files
        self.addToMenu()


    def save(self):
        # truncate list if necessary
        self.__recent_files = self.__recent_files[:MAX_SIZE]
        try:
            fp = open(self.filename, "w")
            for f in self.__recent_files:
                fp.write("%s\n" % f)
            fp.close()
        except Exception, e:
            print "Could not save recent file list", str(e)
            

    def add(self, filename):
        try:
            self.__recent_files.remove(filename)
        except:
            pass

        self.__recent_files.insert(0, filename)
        self.save()
        self.addToMenu()


    def clearMenu(self):
        # clear each menu entry...
        for idx in self.__indecies:
            self.parent.fileMenu.removeItem(idx)

        # clear list of menu entry indecies
        self.__indecies = []

        
    def addToMenu(self, clear=1):
        if clear: self.clearMenu()

        # add applicable items to menu
        num = min(self.numShown, len(self.__recent_files))
        for i in range(num):
            filename = self.__recent_files[i]
            idx = self.parent.fileMenu.insertItem(
                QIconSet(QPixmap(xpm.newIcon)),
                filename)

            self.__indecies.insert(0, idx)
        

    def setNumShown(self, numShown):
        ns = int(numShown)
        if ns == self.numShown: return

        # clear menu of size X then add entries of size Y
        self.clearMenu()
        self.numShown = ns
        self.addToMenu(0)


    def isRecentFile(self, menuid):
        return menuid in self.__indecies


    def move(self, filename, menuid):
        # fix me....
        menu = self.parent.fileMenu
        idx = menu.indexOf(self.__indecies[0])
        menu.removeItem(menuid)
        menu.insertItem(QIconSet(QPixmap(xpm.newIcon)),
                        filename,
                        -1,
                        idx)
        try:
            self.__recent_files.remove(filename)
        except:
            pass
        self.__indecies.insert(0, filename)

