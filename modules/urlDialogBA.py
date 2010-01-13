# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urlDialogBA.ui'
#
# Created: Wed Jan 13 15:18:29 2010
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_URLDialogBA(object):
    def setupUi(self, URLDialogBA):
        URLDialogBA.setObjectName("URLDialogBA")
        URLDialogBA.resize(443, 170)
        URLDialogBA.setSizeGripEnabled(True)
        self.gridlayout = QtGui.QGridLayout(URLDialogBA)
        self.gridlayout.setObjectName("gridlayout")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.buttonHelp = QtGui.QPushButton(URLDialogBA)
        self.buttonHelp.setAutoDefault(True)
        self.buttonHelp.setObjectName("buttonHelp")
        self.hboxlayout.addWidget(self.buttonHelp)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.buttonOk = QtGui.QPushButton(URLDialogBA)
        self.buttonOk.setAutoDefault(True)
        self.buttonOk.setDefault(True)
        self.buttonOk.setObjectName("buttonOk")
        self.hboxlayout.addWidget(self.buttonOk)
        self.buttonCancel = QtGui.QPushButton(URLDialogBA)
        self.buttonCancel.setAutoDefault(True)
        self.buttonCancel.setObjectName("buttonCancel")
        self.hboxlayout.addWidget(self.buttonCancel)
        self.gridlayout.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.groupBox1 = QtGui.QGroupBox(URLDialogBA)
        self.groupBox1.setObjectName("groupBox1")
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox1)
        self.gridlayout1.setObjectName("gridlayout1")
        self.URLTextEdit = QtGui.QPlainTextEdit(self.groupBox1)
        self.URLTextEdit.setObjectName("URLTextEdit")
        self.gridlayout1.addWidget(self.URLTextEdit, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox1, 0, 0, 1, 1)

        self.retranslateUi(URLDialogBA)
        QtCore.QObject.connect(self.buttonOk, QtCore.SIGNAL("clicked()"), URLDialogBA.ok_slot)
        QtCore.QObject.connect(self.buttonCancel, QtCore.SIGNAL("clicked()"), URLDialogBA.reject)
        QtCore.QObject.connect(self.buttonHelp, QtCore.SIGNAL("clicked()"), URLDialogBA.help_slot)
        QtCore.QMetaObject.connectSlotsByName(URLDialogBA)

    def retranslateUi(self, URLDialogBA):
        URLDialogBA.setWindowTitle(QtGui.QApplication.translate("URLDialogBA", "Import URL", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonHelp.setText(QtGui.QApplication.translate("URLDialogBA", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonHelp.setShortcut(QtGui.QApplication.translate("URLDialogBA", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOk.setText(QtGui.QApplication.translate("URLDialogBA", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("URLDialogBA", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox1.setTitle(QtGui.QApplication.translate("URLDialogBA", "Enter URL to import", None, QtGui.QApplication.UnicodeUTF8))
        self.URLTextEdit.setPlainText(QtGui.QApplication.translate("URLDialogBA", "http://kodos.sourceforge.net", None, QtGui.QApplication.UnicodeUTF8))

