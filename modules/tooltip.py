# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

#-----------------------------------------------------------------------------#
# Installed modules

from PyQt4 import QtGui, QtCore

#-----------------------------------------------------------------------------#
# Kodos modules

from .util import FALSE

#-----------------------------------------------------------------------------#

class Tooltip(QtGui.QLabel):
    def __init__(self, text, bgcolor="#ffd700",fgcolor="#000000",delay=1000):
        self.delay = delay
        QtGui.QLabel.__init__(
            self,
            None,
            QtCore.Qt.WindowStaysOnTopHint |
                QtCore.Qt.FramelessWindowHint |
                QtCore.Qt.Tool
        )
        self.setMargin(1)
        self.setIndent(0)
        self.setFrameStyle(QtGui.QFrame.Plain | QtGui.QFrame.Box)
        self.setLineWidth(1)
        self.setText(text)
        self.adjustSize()

        # set the pallete...
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Active, QtGui.QPalette.Window,
                     QtGui.QColor(bgcolor))
        pal.setColor(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                     QtGui.QColor(fgcolor))
        pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
                     QtGui.QColor(bgcolor))
        pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                     QtGui.QColor(fgcolor))
        self.setPalette(pal)

        self.enter_timer_id = None
        self.leave_timer_id = None
        return


    def set_tooltip(self, text):
        self.text = text
        self.setText(text)
        return


    def clear_tooltip(self):
        self.text = ''
        self.setText('')
        return


    def addWidget(self, widget):
        widget.installEventFilter(self)
        return


    def removeWidget(self, widget):
        widget.removeEventFilter(self)
        return


    def killCustomTimers( self ):
        if self.enter_timer_id:
            self.killTimer( self.enter_timer_id )
            self.enter_timer_id = None
        if self.leave_timer_id:
            self.killTimer( self.leave_timer_id )
            self.leave_timer_id = None
        return


    def timerEvent( self, ev ):
        if ev.timerId() == self.enter_timer_id:
            self.tooltip_open()
        elif ev.timerId() == self.leave_timer_id:
            self.tooltip_close()
        self.killCustomTimers()
        return


    def eventFilter(self, obj, ev):
        type = ev.type()
        if type == QtCore.QEvent.Enter:
            self.killCustomTimers()
            self.enter_timer_id = self.startTimer(self.delay)
            self.event_widget = obj
        elif type == QtCore.QEvent.Leave:
            self.killCustomTimers()
            self.leave_timer_id = self.startTimer(self.delay)
            self.event_widget = None
        return FALSE ## Always return unhandled for this kind of filter!!!


    def tooltip_open(self):
        if not self.text:
            return

        try:
            pos = self.event_widget.mapToGlobal(
                QtCore.QPoint(0, self.event_widget.height()))
            self.move(pos.x(), pos.y())
            self.show()
            self.setFixedSize( self.sizeHint() )
        except:
            pass
        return


    def tooltip_close(self):
        self.hide()
        return

#-----------------------------------------------------------------------------#
