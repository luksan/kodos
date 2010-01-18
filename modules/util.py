# -*- coding: utf-8 -*-
#  util.py: -*- Python -*-  DESCRIPTIVE TEXT.

import os
import os.path
import sys
from debug import *
import webbrowser

from PyQt4.QtGui import *
from PyQt4.QtCore import *

# QT constants that should be defined
FALSE = 0
TRUE = 1

global debug

def getAppPath():
    "Convenience function so that we can find the necessary images"
    fullpath = os.path.abspath(sys.argv[0])
    path = os.path.dirname(fullpath)
    return path


def getPixmap(fileStr, fileType="PNG", dir="images"):
    """Return a QPixmap instance for the file fileStr relative
    to the binary location and residing in it's 'images' subdirectory"""

    image = getAppPath() + os.sep + dir + os.sep + fileStr

    if debug & DEBUG_PIXMAP: print "image:", image
    
    pixmap = QPixmap(image, fileType)
    pixmap.setMask(pixmap.createHeuristicMask(1))
    
    return pixmap


def getHomeDirectory():
    "attempt to get the home directory... not sure how this behaves w/ Windoze"
    if sys.platform != "win32":
        try:
            homedir = os.environ["HOME"]
        except KeyError:
            homedir = "/tmp"
    else:
        try:
            homedir = os.path.join(os.environ["HOMEDRIVE"],
                                   os.environ["HOMEPATH"])
        except KeyError:
            homedir = ""

    return homedir

def kodos_toolbar_logo(toolbar):
    # hack to move logo to right
    blanklabel = QLabel()
    blanklabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    logolabel = QLabel("kodos_logo")
    logolabel.setPixmap(QPixmap(":/images/kodos_icon.png"))
    
    toolbar.addWidget(blanklabel)
    toolbar.addWidget(logolabel)

    return logolabel


def getSavedWindowSettings(path):
    try:
        fp = open(path, "r")
        line = fp.readline()[:-1]
        fp.close()
        geo = line.split(" ")

        x = int(geo[0])
        y = int(geo[1])
        width = int(geo[2])
        height = int(geo[3])
        
        return {'x': x,
                'y': y,
                'width': width,
                'height': height}
    except:
        return None


def saveWindowSettings(window, filename):
    path = os.path.join(getHomeDirectory(), ".kodos", filename)

    try:
        s = window.size()
        x = window.x()
        y = window.y()

        #print x, y
        if x == 0 and y == 0 and sys.platform != 'win32':
            # hack because some window managers (sawfish for instance)
            # seem to have an issue w/ repositioning window coords.
            d = getSavedWindowSettings(path)
            if d:
                x = d['x']
                y = d['y']

                #print "save:", d
        fp = open(path, "w")
        fp.write("%d %d %d %d\n" % (x, y, s.width(), s.height()))
        fp.close()
    except:
        pass


def restoreWindowSettings(window, filename):
    path = os.path.join(getHomeDirectory(), ".kodos", filename)

    d = getSavedWindowSettings(path)

    x = d['x']
    y = d['y']
    width = d['width']
    height = d['height']
    #print "load:", d
    sz = QSize(width, height)

    try:
        window.move(x, y)
        window.resize(sz)
    except Exception, e:
        print window.tr("Restoring of saved window geometry failed.")
    

def findFile(filename):
    dirs = [getAppPath(),
            os.path.join("/", "usr", "share", "kodos"),
            os.path.join("/", "usr", "local", "kodos")]

    for d in dirs:
        path = os.path.join(d, filename)
        if os.access(path, os.R_OK): return path

    return None

def launch_browser(url, caption=None, message=None):
    if not caption: caption = "Info"
    if not message: message = "Launch web browser?"
    
    button = QMessageBox.information(None, caption, message, QMessageBox.Ok | QMessageBox.Cancel)
    if button == QMessageBox.Cancel:
        return False
    try:
        webbrowser.open(url)
    except webbrowser.Error, e:
        if debug:
            print e
        print "Couldn't open URL:", url
        return False
    return True
