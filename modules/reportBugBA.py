# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/phil/work/kodos/modules/reportBugBA.ui'
#
# Created: Sun Nov 27 07:14:37 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.14.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class reportBugBA(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("reportBugBA")


        reportBugBALayout = QGridLayout(self,1,1,11,6,"reportBugBALayout")

        Layout8 = QHBoxLayout(None,0,6,"Layout8")
        Spacer1 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout8.addItem(Spacer1)

        self.submitButton = QPushButton(self,"submitButton")
        Layout8.addWidget(self.submitButton)

        self.cancelButton = QPushButton(self,"cancelButton")
        Layout8.addWidget(self.cancelButton)

        reportBugBALayout.addLayout(Layout8,3,0)

        self.GroupBox6 = QGroupBox(self,"GroupBox6")
        self.GroupBox6.setColumnLayout(0,Qt.Vertical)
        self.GroupBox6.layout().setSpacing(6)
        self.GroupBox6.layout().setMargin(11)
        GroupBox6Layout = QGridLayout(self.GroupBox6.layout())
        GroupBox6Layout.setAlignment(Qt.AlignTop)

        Layout10 = QVBoxLayout(None,0,6,"Layout10")

        self.TextLabel4 = QLabel(self.GroupBox6,"TextLabel4")
        Layout10.addWidget(self.TextLabel4)

        self.TextLabel5 = QLabel(self.GroupBox6,"TextLabel5")
        Layout10.addWidget(self.TextLabel5)

        GroupBox6Layout.addLayout(Layout10,0,0)

        Layout11 = QVBoxLayout(None,0,6,"Layout11")

        self.regexMultiLineEdit = QMultiLineEdit(self.GroupBox6,"regexMultiLineEdit")
        self.regexMultiLineEdit.setReadOnly(1)
        Layout11.addWidget(self.regexMultiLineEdit)

        self.stringMultiLineEdit = QMultiLineEdit(self.GroupBox6,"stringMultiLineEdit")
        self.stringMultiLineEdit.setReadOnly(1)
        Layout11.addWidget(self.stringMultiLineEdit)

        GroupBox6Layout.addLayout(Layout11,0,1)

        reportBugBALayout.addWidget(self.GroupBox6,1,0)

        self.GroupBox5 = QGroupBox(self,"GroupBox5")
        self.GroupBox5.setColumnLayout(0,Qt.Vertical)
        self.GroupBox5.layout().setSpacing(6)
        self.GroupBox5.layout().setMargin(11)
        GroupBox5Layout = QGridLayout(self.GroupBox5.layout())
        GroupBox5Layout.setAlignment(Qt.AlignTop)

        self.TextLabel1 = QLabel(self.GroupBox5,"TextLabel1")

        GroupBox5Layout.addWidget(self.TextLabel1,0,0)

        self.TextLabel3 = QLabel(self.GroupBox5,"TextLabel3")

        GroupBox5Layout.addWidget(self.TextLabel3,2,0)

        self.TextLabel2 = QLabel(self.GroupBox5,"TextLabel2")

        GroupBox5Layout.addWidget(self.TextLabel2,1,0)

        self.OSEdit = QLineEdit(self.GroupBox5,"OSEdit")

        GroupBox5Layout.addWidget(self.OSEdit,0,1)

        self.pythonVersionEdit = QLineEdit(self.GroupBox5,"pythonVersionEdit")

        GroupBox5Layout.addWidget(self.pythonVersionEdit,1,1)

        self.PyQtVersionEdit = QLineEdit(self.GroupBox5,"PyQtVersionEdit")

        GroupBox5Layout.addWidget(self.PyQtVersionEdit,2,1)

        reportBugBALayout.addWidget(self.GroupBox5,0,0)

        self.GroupBox7 = QGroupBox(self,"GroupBox7")
        self.GroupBox7.setColumnLayout(0,Qt.Vertical)
        self.GroupBox7.layout().setSpacing(6)
        self.GroupBox7.layout().setMargin(11)
        GroupBox7Layout = QGridLayout(self.GroupBox7.layout())
        GroupBox7Layout.setAlignment(Qt.AlignTop)

        Layout22 = QGridLayout(None,1,1,0,6,"Layout22")

        self.commentsMultiLineEdit = QMultiLineEdit(self.GroupBox7,"commentsMultiLineEdit")

        Layout22.addWidget(self.commentsMultiLineEdit,1,1)

        self.TextLabel3_2 = QLabel(self.GroupBox7,"TextLabel3_2")

        Layout22.addWidget(self.TextLabel3_2,1,0)

        self.emailAddressEdit = QLineEdit(self.GroupBox7,"emailAddressEdit")

        Layout22.addWidget(self.emailAddressEdit,0,1)

        self.TextLabel2_2 = QLabel(self.GroupBox7,"TextLabel2_2")
        self.TextLabel2_2.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Fixed,0,0,self.TextLabel2_2.sizePolicy().hasHeightForWidth()))

        Layout22.addWidget(self.TextLabel2_2,0,0)

        GroupBox7Layout.addLayout(Layout22,0,0)

        reportBugBALayout.addWidget(self.GroupBox7,2,0)

        self.languageChange()

        self.resize(QSize(750,653).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.submitButton,SIGNAL("clicked()"),self.submit_slot)
        self.connect(self.cancelButton,SIGNAL("clicked()"),self.cancel_slot)

        self.setTabOrder(self.OSEdit,self.pythonVersionEdit)
        self.setTabOrder(self.pythonVersionEdit,self.PyQtVersionEdit)
        self.setTabOrder(self.PyQtVersionEdit,self.emailAddressEdit)
        self.setTabOrder(self.emailAddressEdit,self.commentsMultiLineEdit)
        self.setTabOrder(self.commentsMultiLineEdit,self.submitButton)
        self.setTabOrder(self.submitButton,self.cancelButton)
        self.setTabOrder(self.cancelButton,self.regexMultiLineEdit)
        self.setTabOrder(self.regexMultiLineEdit,self.stringMultiLineEdit)


    def languageChange(self):
        self.setCaption(self.__tr("Form1"))
        self.submitButton.setText(self.__tr("Submit Bug Report"))
        self.cancelButton.setText(self.__tr("Cancel"))
        self.GroupBox6.setTitle(self.__tr("Kodos State Information"))
        self.TextLabel4.setText(self.__tr("Regular Expression:"))
        self.TextLabel5.setText(self.__tr("Match String:"))
        self.GroupBox5.setTitle(self.__tr("System Information"))
        self.TextLabel1.setText(self.__tr("Operating System:"))
        self.TextLabel3.setText(self.__tr("PyQt Version:"))
        self.TextLabel2.setText(self.__tr("Python Version:"))
        self.GroupBox7.setTitle(self.__tr("Comments"))
        self.TextLabel3_2.setText(self.__tr("Comments:"))
        self.TextLabel2_2.setText(self.__tr("Email address:"))


    def cancel_slot(self):
        print "reportBugBA.cancel_slot(): Not implemented yet"

    def submit_slot(self):
        print "reportBugBA.submit_slot(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("reportBugBA",s,c)
