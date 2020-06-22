# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

#-----------------------------------------------------------------------------#
# Installed modules

from PyQt4 import QtGui, QtCore

#-----------------------------------------------------------------------------#
# Kodos modules

from .tooltip import Tooltip
from .util import TRUE, FALSE

#-----------------------------------------------------------------------------#

class Status_Bar:
    def __init__(self, parent, progress_bar=FALSE, message=''):
        self.parent = parent

        self.statusBar = parent.statusBar()
        self.__statusTimer = QtCore.QTimer(self.parent)

        self.__statusTimer.timeout.connect(self.reset_message)

        self.__statusLabel = QtGui.QLabel("msg", self.statusBar)
        self.tooltip = Tooltip('')
        self.tooltip.addWidget(self.__statusLabel)

        self.last_status_message = ''

        pixmap = QtGui.QPixmap(":images/yellow.png")

        self.pixmapLabel = QtGui.QLabel("image", self.statusBar)
        self.pixmapLabel.setPixmap(pixmap)

        self.statusBar.addWidget(self.pixmapLabel)
        self.statusBar.addWidget(self.__statusLabel)
        if progress_bar:
            self.progressBar = QtGui.QProgressBar(self.statusBar)
            self.statusBar.addWidget(self.progressBar, 1, TRUE)

        if message:
            self.set_message(message)
        return


    def set_message(self, message='', duration=0, replace=FALSE, tooltip='', pixmap=''):
        """sets the status bar message label to message.

        if duration is > 0 than the message is displayed for duration seconds.

        if duration is > 0 and replace is true then after duration seconds
        have elapsed, the previous message is displayed.
        """

        self.__statusTimer.stop()
        self.last_status_message = unicode(self.__statusLabel.text())
        self.replace_status_message = replace

        self.__statusLabel.setText(message)

        if duration > 0:
            self.__statusTimer.setSingleShot(True)
            self.__statusTimer.start(1000 * duration)

        if tooltip:
            self.tooltip.set_tooltip(tooltip)
        else:
            self.tooltip.clear_tooltip()

        if pixmap:
            self.pixmapLabel.setPixmap(pixmap)
        return


    def reset_message(self):
        self.__statusTimer.stop()
        if self.replace_status_message:
            self.__statusLabel.setText(self.last_status_message)
        else:
            self.__statusLabel.setText('')
        return


    def geometry(self):
        return self.statusBar.geometry()

#-----------------------------------------------------------------------------#
