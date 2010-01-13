# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpBA.ui'
#
# Created: Wed Jan 13 13:15:28 2010
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_HelpBA(object):
    def setupUi(self, HelpBA):
        HelpBA.setObjectName("HelpBA")
        HelpBA.resize(494, 585)
        self.widget = QtGui.QWidget(HelpBA)
        self.widget.setGeometry(QtCore.QRect(0, 55, 494, 530))
        self.widget.setObjectName("widget")
        HelpBA.setCentralWidget(self.widget)
        self.toolBar = QtGui.QToolBar(HelpBA)
        self.toolBar.setGeometry(QtCore.QRect(0, 0, 110, 31))
        self.toolBar.setObjectName("toolBar")
        HelpBA.addToolBar(self.toolBar)
        self.menubar = QtGui.QMenuBar(HelpBA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 24))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtGui.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        HelpBA.setMenuBar(self.menubar)
        self.fileHomeAction = QtGui.QAction(HelpBA)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image0"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileHomeAction.setIcon(icon)
        self.fileHomeAction.setProperty("name", QtCore.QVariant("fileHomeAction"))
        self.fileHomeAction.setObjectName("fileHomeAction")
        self.fileBackAction = QtGui.QAction(HelpBA)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image1"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileBackAction.setIcon(icon1)
        self.fileBackAction.setProperty("name", QtCore.QVariant("fileBackAction"))
        self.fileBackAction.setObjectName("fileBackAction")
        self.fileForwardAction = QtGui.QAction(HelpBA)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image2"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileForwardAction.setIcon(icon2)
        self.fileForwardAction.setProperty("name", QtCore.QVariant("fileForwardAction"))
        self.fileForwardAction.setObjectName("fileForwardAction")
        self.fileExitAction = QtGui.QAction(HelpBA)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image3"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileExitAction.setIcon(icon3)
        self.fileExitAction.setProperty("name", QtCore.QVariant("fileExitAction"))
        self.fileExitAction.setObjectName("fileExitAction")
        self.toolBar.addAction(self.fileBackAction)
        self.toolBar.addAction(self.fileForwardAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.fileHomeAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileHomeAction)
        self.fileMenu.addAction(self.fileBackAction)
        self.fileMenu.addAction(self.fileForwardAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileExitAction)
        self.menubar.addAction(self.fileMenu.menuAction())

        self.retranslateUi(HelpBA)
        QtCore.QObject.connect(self.fileExitAction, QtCore.SIGNAL("activated()"), HelpBA.exitSlot)
        QtCore.QObject.connect(self.fileBackAction, QtCore.SIGNAL("activated()"), HelpBA.backSlot)
        QtCore.QObject.connect(self.fileForwardAction, QtCore.SIGNAL("activated()"), HelpBA.forwardSlot)
        QtCore.QObject.connect(self.fileHomeAction, QtCore.SIGNAL("activated()"), HelpBA.homeSlot)
        QtCore.QMetaObject.connectSlotsByName(HelpBA)

    def retranslateUi(self, HelpBA):
        HelpBA.setWindowTitle(QtGui.QApplication.translate("HelpBA", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setLabel(QtGui.QApplication.translate("HelpBA", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.fileMenu.setTitle(QtGui.QApplication.translate("HelpBA", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.fileHomeAction.setText(QtGui.QApplication.translate("HelpBA", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.fileHomeAction.setIconText(QtGui.QApplication.translate("HelpBA", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.fileHomeAction.setShortcut(QtGui.QApplication.translate("HelpBA", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.fileBackAction.setText(QtGui.QApplication.translate("HelpBA", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.fileBackAction.setIconText(QtGui.QApplication.translate("HelpBA", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.fileBackAction.setShortcut(QtGui.QApplication.translate("HelpBA", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.fileForwardAction.setText(QtGui.QApplication.translate("HelpBA", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.fileForwardAction.setIconText(QtGui.QApplication.translate("HelpBA", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.fileForwardAction.setShortcut(QtGui.QApplication.translate("HelpBA", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.fileExitAction.setText(QtGui.QApplication.translate("HelpBA", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.fileExitAction.setIconText(QtGui.QApplication.translate("HelpBA", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.fileExitAction.setShortcut(QtGui.QApplication.translate("HelpBA", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

