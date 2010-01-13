# Form implementation generated from reading ui file '/www/kodos/modules/stringBA.ui'
#
# Created: Thu May 8 15:30:15 2003
#      by: The Python User Interface Compiler (pyuic)
#
# WARNING! All changes made in this file will be lost!


from qt import *


class unnamed(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if name == None:
            self.setName('Form2')

        self.resize(700,205)
        self.setCaption(self.tr('Form2'))
        Form2Layout = QGridLayout(self)
        Form2Layout.setSpacing(6)
        Form2Layout.setMargin(11)

        self.GroupBox2 = QGroupBox(self,'GroupBox2')
        self.GroupBox2.setTitle(self.tr('String'))
        self.GroupBox2.setColumnLayout(0,Qt.Vertical)
        self.GroupBox2.layout().setSpacing(0)
        self.GroupBox2.layout().setMargin(0)
        GroupBox2Layout = QVBoxLayout(self.GroupBox2.layout())
        GroupBox2Layout.setAlignment(Qt.AlignTop)
        GroupBox2Layout.setSpacing(6)
        GroupBox2Layout.setMargin(11)

        self.stringMultiLineEdit = QMultiLineEdit(self.GroupBox2,'stringMultiLineEdit')
        stringMultiLineEdit_font = QFont(self.stringMultiLineEdit.font())
        stringMultiLineEdit_font.setFamily('adobe-helvetica')
        stringMultiLineEdit_font.setPointSize(14)
        self.stringMultiLineEdit.setFont(stringMultiLineEdit_font)
        self.stringMultiLineEdit.setWordWrap(QMultiLineEdit.NoWrap)
        GroupBox2Layout.addWidget(self.stringMultiLineEdit)

        Form2Layout.addWidget(self.GroupBox2,0,0)

        self.connect(self.stringMultiLineEdit,SIGNAL('textChanged()'),self.string_changed_slot)

    def event(self,ev):
        ret = QWidget.event(self,ev)

        if ev.type() == QEvent.ApplicationFontChange:
            stringMultiLineEdit_font = QFont(self.stringMultiLineEdit.font())
            stringMultiLineEdit_font.setFamily('adobe-helvetica')
            stringMultiLineEdit_font.setPointSize(14)
            self.stringMultiLineEdit.setFont(stringMultiLineEdit_font)

        return ret

    def string_changed_slot(self):
        print 'unnamed.string_changed_slot(): not implemented yet'
