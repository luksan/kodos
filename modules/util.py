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

def saveWindowSettings(window, filename):
    settings = QSettings()
    settings.setValue(window.objectName(), window.saveGeometry())

def restoreWindowSettings(window, filename):
    settings = QSettings()
    window.restoreGeometry(settings.value(window.objectName()).toByteArray())

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
