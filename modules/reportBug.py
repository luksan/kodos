#  reportBug.py: -*- Python -*-  DESCRIPTIVE TEXT.

from reportBugBA import reportBugBA
from util import *
import qt 
import sys
import string
import smtplib
from version import VERSION
import xpm

AUTHOR_ADDR = "phil_schwartz@users.sourceforge.net"

class reportBug(reportBugBA):
    def __init__(self, parent=None, name=None):
        reportBugBA.__init__(self, parent, name)
        self.parent = parent
        self.kodos_main = parent.kodos_main
        self.populate()
        

    def populate(self):
        self.OSEdit.setText(sys.platform)
        pyvers = string.replace(sys.version, "\n", " - ")
        self.pythonVersionEdit.setText(pyvers)
        self.PyQtVersionEdit.setText(qt.QT_VERSION_STR)
        self.regexMultiLineEdit.setText(self.kodos_main.regexMultiLineEdit.text())
        self.stringMultiLineEdit.setText(self.kodos_main.stringMultiLineEdit.text())


    def cancel_slot(self):
        self.parent.close()

    def submit_slot(self):
        addr = str(self.emailAddressEdit.text())
        if not addr:
            msg = self.tr(
                "An email address is necessary so that the author "
                "can contact you.  Your email address will not "
                "be used for any other purposes.")

            QMessageBox.information(None,
                                    self.tr("You must supply a valid email address"),
                                    msg)
            return 

        msg = "Subject: Kodos bug report\n\n"
        msg += "Kodos Version: %s\n" % VERSION
        msg += "Operating System: %s\n" % unicode(self.OSEdit.text())
        msg += "Python Version: %s\n" % unicode(self.pythonVersionEdit.text())
        msg += "PyQt Version: %s\n" % unicode(self.PyQtVersionEdit.text())
        msg += "\n" + "=" * 70 + "\n"
        msg += "Regex:\n%s\n" % unicode(self.regexMultiLineEdit.text())
        msg += "=" * 70 + "\n"
        msg += "String:\n%s\n" % unicode(self.stringMultiLineEdit.text())
        msg += "=" * 70 + "\n"
        msg += "Comments:\n%s\n" % unicode(self.commentsMultiLineEdit.text())
        email_server = unicode(self.kodos_main.prefs.emailServerEdit.text()) or "localhost"
        try:
            server = smtplib.SMTP(email_server)
            server.sendmail(addr, AUTHOR_ADDR, msg)
            server.quit()
            QMessageBox.information(None,
                                    self.tr("Bug report sent"),
                                    self.tr("Your bug report has been sent."))
            self.parent.close()
        except Exception, e:
            QMessageBox.information(None,
                                    self.tr("An exception occurred sending bug report"),
                                    str(e))
        

class reportBugWindow(QMainWindow):
    def __init__(self, kodos_main):
        self.kodos_main = kodos_main

        QMainWindow.__init__(self, None, None,
                             Qt.WType_TopLevel | Qt.WDestructiveClose)
        
        self.setGeometry(100, 50, 800, 600)
        self.setCaption(self.tr("Report a Bug"))
        #self.setIcon(getPixmap("kodos_icon.png", "PNG"))
        self.setIcon(QPixmap(xpm.kodosIcon))
        self.bug_report = reportBug(self)
        self.setCentralWidget(self.bug_report)

        
        self.createMenu()
        self.createToolBar()

        self.show()


    def createMenu(self):
        self.filemenu = QPopupMenu()
        id = self.filemenu.insertItem(self.tr("&Close"), self, SLOT("close()"))

        self.menubar = QMenuBar(self)
        self.menubar.insertItem(self.tr("&File"), self.filemenu)


    def createToolBar(self):
        toolbar = QToolBar(self)
        toolbar.setStretchableWidget(self.menubar)
        self.logolabel = kodos_toolbar_logo(toolbar)
 
