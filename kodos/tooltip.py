# -*- coding: utf-8 -*-
#  tooltip.py: -*- Python -*-  DESCRIPTIVE TEXT.

from PyQt4 import Qt, QtCore
from .util import FALSE

class Tooltip(Qt.QLabel):
    def __init__(self, text, bgcolor="#ffd700",fgcolor="#000000",delay=1000):
        self.delay = delay
        Qt.QLabel.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint
                        | QtCore.Qt.FramelessWindowHint
                        | QtCore.Qt.Tool)
        self.setMargin(1)
        self.setIndent(0)
        self.setFrameStyle(Qt.QFrame.Plain | Qt.QFrame.Box)
        self.setLineWidth(1)
        self.setText(text)
        self.adjustSize()

        # set the pallete...
        pal = Qt.QPalette()
        pal.setColor(Qt.QPalette.Active, Qt.QPalette.Window, Qt.QColor(bgcolor))
        pal.setColor(Qt.QPalette.Active, Qt.QPalette.WindowText, Qt.QColor(fgcolor))
        pal.setColor(Qt.QPalette.Inactive, Qt.QPalette.Window, Qt.QColor(bgcolor))
        pal.setColor(Qt.QPalette.Inactive, Qt.QPalette.WindowText, Qt.QColor(fgcolor))
        self.setPalette(pal)

        self.enter_timer_id = None
        self.leave_timer_id = None


    def set_tooltip(self, text):
        self.text = text
        self.setText(text)


    def clear_tooltip(self):
        self.text = ''
        self.setText('')


    def addWidget(self, widget):
        widget.installEventFilter(self)


    def removeWidget(self, widget):
        widget.removeEventFilter(self)


    def killCustomTimers( self ):
        if self.enter_timer_id:
            self.killTimer( self.enter_timer_id )
            self.enter_timer_id = None
        if self.leave_timer_id:
            self.killTimer( self.leave_timer_id )
            self.leave_timer_id = None


    def timerEvent( self, ev ):
        if ev.timerId() == self.enter_timer_id:
            self.tooltip_open()
        elif ev.timerId() == self.leave_timer_id:
            self.tooltip_close()
        self.killCustomTimers()


    def eventFilter(self, obj, ev):
        type = ev.type()
        if type == Qt.QEvent.Enter:
            self.killCustomTimers()
            self.enter_timer_id = self.startTimer(self.delay)
            self.event_widget = obj
        elif type == Qt.QEvent.Leave:
            self.killCustomTimers()
            self.leave_timer_id = self.startTimer(self.delay)
            self.event_widget = None
        return FALSE ## Always return unhandled for this kind of filter!!!


    def tooltip_open(self):
        if not self.text:
            return

        try:
            pos = self.event_widget.mapToGlobal(
                Qt.QPoint(0, self.event_widget.height()))
            self.move(pos.x(), pos.y())
            self.show()
            self.setFixedSize( self.sizeHint() )
        except:
            pass


    def tooltip_close(self):
        self.hide()
