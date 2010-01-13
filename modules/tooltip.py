#  tooltip.py: -*- Python -*-  DESCRIPTIVE TEXT.

from qt import *
from util import *

class Tooltip(QLabel):
    def __init__(self, text, bgcolor="#ffd700",fgcolor="#000000",delay=1000):
        self.delay = delay
        QLabel.__init__(self, None, "tooltip", Qt.WStyle_StaysOnTop
                        | Qt.WStyle_Customize
                        | Qt.WStyle_NoBorder
                        | Qt.WStyle_Tool)
        self.setMargin(1)
        self.setIndent(0)
        self.setAutoMask(FALSE)
        self.setFrameStyle(QFrame.Plain | QFrame.Box)
        self.setLineWidth(1)
        self.polish()
        self.setText(text)
        self.adjustSize()

        # set the pallete...
        pal = QPalette()
        cg = QColorGroup()
        cg.setColor(QColorGroup.Background, QColor(bgcolor))
        cg.setColor(QColorGroup.Foreground, QColor(fgcolor))
        pal.setActive(cg)
        pal.setInactive(cg)
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
        #print "adding widget", widget
        widget.installEventFilter(self)


    def removeWidget(self, widget):
        #print "removing widget", widget
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
        #print obj, type
        if type == QEvent.Enter:
            self.killCustomTimers()
            self.enter_timer_id = self.startTimer(self.delay)
            #print "tip!"
            self.event_widget = obj
        elif type == QEvent.Leave:
            self.killCustomTimers()
            self.leave_timer_id = self.startTimer(self.delay)
            #print "remove tip!"
            self.event_widget = None
        return FALSE ## Always return unhandled for this kind of filter!!!


    def tooltip_open(self):
        if not self.text:
            return
        
        try:
            pos = self.event_widget.mapToGlobal(
                QPoint(0, self.event_widget.height()))
            self.move(pos.x(), pos.y())
            self.show()
            self.setFixedSize( self.sizeHint() )
        except:
            pass


    def tooltip_close(self):
        self.hide()
