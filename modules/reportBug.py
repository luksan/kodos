# -*- coding: utf-8 -*-
#  reportBug.py: -*- Python -*-  DESCRIPTIVE TEXT.

from reportBugBA import reportBugBA
from util import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import *
import sys
import string
import smtplib
from version import VERSION

AUTHOR_ADDR = "phil_schwartz@users.sourceforge.net"

class reportBug(reportBugBA):
    def __init__(self, parent=None, name=None):
        reportBugBA.__init__(self, parent)
        self.parent = parent
        self.kodos_main = parent.kodos_main
        self.populate()
        return


    def populate(self):
        self.OSEdit.setText(sys.platform)
        pyvers = string.replace(sys.version, "\n", " - ")
        self.pythonVersionEdit.setText(pyvers)
        self.PyQtVersionEdit.setText(QT_VERSION_STR)
        self.regexMultiLineEdit.setPlainText(self.kodos_main.regexMultiLineEdit.toPlainText())
        self.stringMultiLineEdit.setPlainText(self.kodos_main.stringMultiLineEdit.toPlainText())
        return


    def cancel_slot(self):
        self.parent.close()
        return


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
        return


class reportBugWindow(QMainWindow):
    def __init__(self, kodos_main):
        self.kodos_main = kodos_main
        QMainWindow.__init__(self, kodos_main)#, Qt.Window | Qt.WA_DeleteOnClose)

        self.setGeometry(100, 50, 800, 600)
        self.setWindowTitle(self.tr("Report a Bug"))
        self.setWindowIcon(QIcon(QPixmap(":images/kodos_icon.png")))

        self.bug_report = reportBug(self)
        self.setCentralWidget(self.bug_report)


        self.createMenu()
        self.createToolBar()

        self.show()
        return


    def createMenu(self):
        self.menubar = self.menuBar()
        self.filemenu = self.menubar.addMenu(self.tr("&File"))
        self.filemenu.addAction(self.tr("&Close"), self, SLOT("close()"))
        return


    def createToolBar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        self.logolabel = kodos_toolbar_logo(toolbar)
        return

