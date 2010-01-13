# Form implementation generated from reading ui file '/www/kodos/modules/resultsBA.ui'
#
# Created: Thu May 8 15:30:17 2003
#      by: The Python User Interface Compiler (pyuic)
#
# WARNING! All changes made in this file will be lost!


from qt import *


class unnamed(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if name == None:
            self.setName('Form3')

        self.resize(715,250)
        self.setCaption(self.tr('Form3'))
        Form3Layout = QGridLayout(self)
        Form3Layout.setSpacing(6)
        Form3Layout.setMargin(11)

        self.infoTabWidget = QTabWidget(self,'infoTabWidget')

        self.tab = QWidget(self.infoTabWidget,'tab')
        tabLayout = QVBoxLayout(self.tab)
        tabLayout.setSpacing(6)
        tabLayout.setMargin(11)

        self.groupListView = QListView(self.tab,'groupListView')
        self.groupListView.addColumn(self.tr('Group #'))
        self.groupListView.addColumn(self.tr('Group Name'))
        self.groupListView.addColumn(self.tr('Match'))
        self.groupListView.setAllColumnsShowFocus(1)
        self.groupListView.setShowSortIndicator(1)
        tabLayout.addWidget(self.groupListView)
        self.infoTabWidget.insertTab(self.tab,self.tr('Group'))

        self.tab_2 = QWidget(self.infoTabWidget,'tab_2')
        tabLayout_2 = QVBoxLayout(self.tab_2)
        tabLayout_2.setSpacing(6)
        tabLayout_2.setMargin(11)

        self.matchTextBrowser = QTextBrowser(self.tab_2,'matchTextBrowser')
        self.matchTextBrowser.setTextFormat(QTextBrowser.RichText)
        tabLayout_2.addWidget(self.matchTextBrowser)
        self.infoTabWidget.insertTab(self.tab_2,self.tr('Match'))

        self.tab_3 = QWidget(self.infoTabWidget,'tab_3')
        tabLayout_3 = QVBoxLayout(self.tab_3)
        tabLayout_3.setSpacing(6)
        tabLayout_3.setMargin(11)

        self.codeTextBrowser = QTextBrowser(self.tab_3,'codeTextBrowser')
        tabLayout_3.addWidget(self.codeTextBrowser)
        self.infoTabWidget.insertTab(self.tab_3,self.tr('Sample Code'))

        Form3Layout.addWidget(self.infoTabWidget,1,0)

        Layout10 = QHBoxLayout()
        Layout10.setSpacing(6)
        Layout10.setMargin(0)
        spacer = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout10.addItem(spacer)

        self.TextLabel3 = QLabel(self,'TextLabel3')
        self.TextLabel3.setText(self.tr('Match number:'))
        Layout10.addWidget(self.TextLabel3)

        self.matchNumberSpinBox = QSpinBox(self,'matchNumberSpinBox')
        self.matchNumberSpinBox.setEnabled(0)
        self.matchNumberSpinBox.setSizePolicy(QSizePolicy(0,0,self.matchNumberSpinBox.sizePolicy().hasHeightForWidth()))
        self.matchNumberSpinBox.setMinValue(1)
        Layout10.addWidget(self.matchNumberSpinBox)
        spacer_2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout10.addItem(spacer_2)

        Form3Layout.addLayout(Layout10,0,0)

        self.connect(self.matchNumberSpinBox,SIGNAL('valueChanged(int)'),self.match_num_slot)

    def match_num_slot(self):
        print 'unnamed.match_num_slot(): not implemented yet'
