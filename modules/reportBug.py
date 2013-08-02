# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

#-----------------------------------------------------------------------------#
# Built-in modules

import sys
import string
import smtplib

#-----------------------------------------------------------------------------#
# Installed modules

from PyQt4.QtGui import QMainWindow, QMessageBox, QToolBar, QPixmap, QIcon
from PyQt4.QtCore import SLOT, QT_VERSION_STR

#-----------------------------------------------------------------------------#
# Kodos modules

from .reportBugBA import reportBugBA
from .util import kodos_toolbar_logo
from .version import VERSION

#-----------------------------------------------------------------------------#

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
        msg += "Kodos Version: {0}\n".format(VERSION)
        msg += "Operating System: {0}\n".format(unicode(self.OSEdit.text()))
        msg += "Python Version: {0}\n".format(unicode(self.pythonVersionEdit.text()))
        msg += "PyQt Version: {0}\n".format(unicode(self.PyQtVersionEdit.text()))
        msg += "\n" + "=" * 70 + "\n"
        msg += "Regex:\n{0}\n".format(unicode(self.regexMultiLineEdit.text()))
        msg += "=" * 70 + "\n"
        msg += "String:\n{0}\n".format(unicode(self.stringMultiLineEdit.text()))
        msg += "=" * 70 + "\n"
        msg += "Comments:\n{0}\n".format(unicode(self.commentsMultiLineEdit.text()))
        email_server = unicode(self.kodos_main.prefs.emailServerEdit.text()) or "localhost"
        try:
            server = smtplib.SMTP(email_server)
            server.sendmail(addr, AUTHOR_ADDR, msg)
            server.quit()
            QMessageBox.information(None,
                                    self.tr("Bug report sent"),
                                    self.tr("Your bug report has been sent."))
            self.parent.close()
        except Exception as e:
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

#-----------------------------------------------------------------------------#
