# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

#-----------------------------------------------------------------------------#
# Built-in modules

import os
import sys
import webbrowser

#-----------------------------------------------------------------------------#
# Installed modules

from PyQt4.QtGui import *
from PyQt4.QtCore import *

#-----------------------------------------------------------------------------#
# Kodos modules

from debug import *

#-----------------------------------------------------------------------------#

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

    if debug & DEBUG_PIXMAP: print("image: {0}".format(image))

    pixmap = QPixmap(image, fileType)
    pixmap.setMask(pixmap.createHeuristicMask(1))

    return pixmap


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
    return


def restoreWindowSettings(window, filename):
    settings = QSettings()
    window.restoreGeometry(settings.value(window.objectName()).toByteArray())
    return


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
    except webbrowser.Error as e:
        if debug:
            print(e)
        print("Couldn't open URL: {0}".format(url))
        return False
    return True

#-----------------------------------------------------------------------------#
