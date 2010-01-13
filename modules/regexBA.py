# Form implementation generated from reading ui file '/www/kodos/modules/regexBA.ui'
#
# Created: Thu May 8 15:30:14 2003
#      by: The Python User Interface Compiler (pyuic)
#
# WARNING! All changes made in this file will be lost!


from qt import *


class unnamed(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if name == None:
            self.setName('Form1')

        self.resize(695,255)
        self.setCaption(self.tr('Form1'))
        Form1Layout = QGridLayout(self)
        Form1Layout.setSpacing(6)
        Form1Layout.setMargin(11)

        self.GroupBox1 = QGroupBox(self,'GroupBox1')
        self.GroupBox1.setTitle(self.tr('Regular Expression'))
        self.GroupBox1.setColumnLayout(0,Qt.Vertical)
        self.GroupBox1.layout().setSpacing(0)
        self.GroupBox1.layout().setMargin(0)
        GroupBox1Layout = QVBoxLayout(self.GroupBox1.layout())
        GroupBox1Layout.setAlignment(Qt.AlignTop)
        GroupBox1Layout.setSpacing(6)
        GroupBox1Layout.setMargin(11)

        self.regexMultiLineEdit = QMultiLineEdit(self.GroupBox1,'regexMultiLineEdit')
        regexMultiLineEdit_font = QFont(self.regexMultiLineEdit.font())
        regexMultiLineEdit_font.setFamily('adobe-helvetica')
        regexMultiLineEdit_font.setPointSize(14)
        self.regexMultiLineEdit.setFont(regexMultiLineEdit_font)
        self.regexMultiLineEdit.setWordWrap(QMultiLineEdit.NoWrap)
        GroupBox1Layout.addWidget(self.regexMultiLineEdit)

        Form1Layout.addWidget(self.GroupBox1,0,0)

        self.GroupBox3 = QGroupBox(self,'GroupBox3')
        self.GroupBox3.setTitle(self.tr('Flags'))
        self.GroupBox3.setColumnLayout(0,Qt.Vertical)
        self.GroupBox3.layout().setSpacing(0)
        self.GroupBox3.layout().setMargin(0)
        GroupBox3Layout = QHBoxLayout(self.GroupBox3.layout())
        GroupBox3Layout.setAlignment(Qt.AlignTop)
        GroupBox3Layout.setSpacing(6)
        GroupBox3Layout.setMargin(11)

        self.ignorecaseCheckBox = QCheckBox(self.GroupBox3,'ignorecaseCheckBox')
        self.ignorecaseCheckBox.setText(self.tr('Ignore Case'))
        GroupBox3Layout.addWidget(self.ignorecaseCheckBox)

        self.multilineCheckBox = QCheckBox(self.GroupBox3,'multilineCheckBox')
        self.multilineCheckBox.setText(self.tr('Multi Line'))
        GroupBox3Layout.addWidget(self.multilineCheckBox)

        self.dotallCheckBox = QCheckBox(self.GroupBox3,'dotallCheckBox')
        self.dotallCheckBox.setText(self.tr('Dot All'))
        GroupBox3Layout.addWidget(self.dotallCheckBox)

        self.verboseCheckBox = QCheckBox(self.GroupBox3,'verboseCheckBox')
        self.verboseCheckBox.setText(self.tr('Verbose'))
        GroupBox3Layout.addWidget(self.verboseCheckBox)

        self.localeCheckBox = QCheckBox(self.GroupBox3,'localeCheckBox')
        self.localeCheckBox.setText(self.tr('Locale'))
        GroupBox3Layout.addWidget(self.localeCheckBox)

        self.unicodeCheckBox = QCheckBox(self.GroupBox3,'unicodeCheckBox')
        self.unicodeCheckBox.setText(self.tr('Unicode'))
        GroupBox3Layout.addWidget(self.unicodeCheckBox)

        Form1Layout.addWidget(self.GroupBox3,1,0)

        self.connect(self.regexMultiLineEdit,SIGNAL('textChanged()'),self.regex_changed_slot)
        self.connect(self.ignorecaseCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.multilineCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.dotallCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.verboseCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.localeCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.unicodeCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.ignorecaseCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.multilineCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.dotallCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.verboseCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.localeCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.unicodeCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)

    def event(self,ev):
        ret = QWidget.event(self,ev)

        if ev.type() == QEvent.ApplicationFontChange:
            regexMultiLineEdit_font = QFont(self.regexMultiLineEdit.font())
            regexMultiLineEdit_font.setFamily('adobe-helvetica')
            regexMultiLineEdit_font.setPointSize(14)
            self.regexMultiLineEdit.setFont(regexMultiLineEdit_font)

        return ret

    def checkbox_slot(self):
        print 'unnamed.checkbox_slot(): not implemented yet'

    def checkbox_slot(self):
        print 'unnamed.checkbox_slot(): not implemented yet'

    def regex_changed_slot(self):
        print 'unnamed.regex_changed_slot(): not implemented yet'
