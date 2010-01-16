# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUserDialogBA.ui'
#
# Created: Wed Jan 13 17:29:22 2010
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NewUserDialog(object):
    def setupUi(self, NewUserDialog):
        NewUserDialog.setObjectName("NewUserDialog")
        NewUserDialog.resize(338, 326)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewUserDialog.sizePolicy().hasHeightForWidth())
        NewUserDialog.setSizePolicy(sizePolicy)
        self.vboxlayout = QtGui.QVBoxLayout(NewUserDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.textLabel1 = QtGui.QLabel(NewUserDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel1.setWordWrap(True)
        self.textLabel1.setObjectName("textLabel1")
        self.vboxlayout1.addWidget(self.textLabel1)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.pixmapLabel2 = QtGui.QLabel(NewUserDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixmapLabel2.sizePolicy().hasHeightForWidth())
        self.pixmapLabel2.setSizePolicy(sizePolicy)
        self.pixmapLabel2.setPixmap(QtGui.QPixmap("image1"))
        self.pixmapLabel2.setScaledContents(True)
        self.pixmapLabel2.setWordWrap(False)
        self.pixmapLabel2.setObjectName("pixmapLabel2")
        self.gridlayout.addWidget(self.pixmapLabel2, 1, 1, 1, 1)
        self.textLabel4 = QtGui.QLabel(NewUserDialog)
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName("textLabel4")
        self.gridlayout.addWidget(self.textLabel4, 1, 0, 1, 1)
        self.pixmapLabel1 = QtGui.QLabel(NewUserDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixmapLabel1.sizePolicy().hasHeightForWidth())
        self.pixmapLabel1.setSizePolicy(sizePolicy)
        self.pixmapLabel1.setPixmap(QtGui.QPixmap("image2"))
        self.pixmapLabel1.setScaledContents(True)
        self.pixmapLabel1.setWordWrap(False)
        self.pixmapLabel1.setObjectName("pixmapLabel1")
        self.gridlayout.addWidget(self.pixmapLabel1, 0, 1, 1, 1)
        self.textLabel3 = QtGui.QLabel(NewUserDialog)
        self.textLabel3.setWordWrap(False)
        self.textLabel3.setObjectName("textLabel3")
        self.gridlayout.addWidget(self.textLabel3, 0, 0, 1, 1)
        self.vboxlayout1.addLayout(self.gridlayout)
        self.vboxlayout.addLayout(self.vboxlayout1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtGui.QSpacerItem(241, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(NewUserDialog)
        self.okButton.setDefault(True)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(NewUserDialog)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL("clicked()"), NewUserDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(NewUserDialog)

    def retranslateUi(self, NewUserDialog):
        NewUserDialog.setWindowTitle(QtGui.QApplication.translate("NewUserDialog", "Kodos new user information", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("NewUserDialog", "<h3>Welcome to Kodos.</h3>\n"
"<p></p>\n"
"It appears that this is your first time using \n"
"Kodos - The Python Regular Expression Debugger.\n"
"<p></p>\n"
"In order to help you familiarize yourself with Kodos, you may wish to explore\n"
"the Regex Library.  Additionally, Kodos contains a Python Regex Reference Guide. \n"
"You can access these tools by clicking on the appropriate toolbar icon.", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel4.setText(QtGui.QApplication.translate("NewUserDialog", "<b>Regex Reference Guide</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel3.setText(QtGui.QApplication.translate("NewUserDialog", "<b>Regex Library</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("NewUserDialog", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setShortcut(QtGui.QApplication.translate("NewUserDialog", "Alt+O", None, QtGui.QApplication.UnicodeUTF8))


class NewUserDialog(QtGui.QDialog, Ui_NewUserDialog):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)

