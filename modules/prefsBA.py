# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/phil/work/kodos/modules/prefsBA.ui'
#
# Created: Sat Jul 9 09:40:32 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.14.1
#
# WARNING! All changes made in this file will be lost!


from qt import *

image0_data = [
"32 32 16 1",
". c None",
"# c #000000",
"h c #00009c",
"i c #0000ff",
"c c #005500",
"k c #0065ff",
"m c #31ffff",
"g c #414441",
"j c #525552",
"b c #62ce31",
"e c #9c0000",
"n c #9c65cd",
"l c #a4a1a4",
"a c #cdceff",
"d c #ffff62",
"f c #ffffff",
"...........###########..........",
".........##aaaaaaaaaaa##........",
"........#aaaaa######aaaa#.......",
".......#aaaa##bccbbc##aaa#......",
"......#aaaa#bcbbbbcbcb#aaa#.....",
"......#aaaa#cbbbbbbbbc#aaa#.....",
"......#aaaa#b########b#aaa#.....",
".....#aaaa#b#bbbbbbbb#b#aaa#....",
".....#aaaaa#bb######bb#aaaa#....",
".....#aaaa#bb#dddddd#bb#aaa#....",
".....#aa#a#b#dddddddd#b#a#a#....",
".....#aa###b#dddedddd#b###a#....",
".....#aa#b#b#dddedddd#b#b#a#....",
".....#aaa#bbb#dddddd#bbb#aa#....",
".....#aaaa##bb######bb##aaa#....",
".....#aaaaa#bbbbbbbbbb#aaaa#....",
"......#aaaa##bb####bbb#aaa#.....",
"......#aaaa#bbbbbbbbbb#aaa#.....",
"......#aaaa###bbbbbb###aaa#.....",
"......#aaa#bbb#bbbbbbbb#aa#.....",
"##....#aaa#b#bbbbbb##b#aaa#.....",
"#b#...#aaa##f#bbb##f#b#aaa#.....",
"#bb#...#aaa#gf###fghib#aa#....##",
"#bbb#..#aaa#ihfjfgiikb#aa#...#b#",
".#bbb#.#aaa#kihlg#kmk#aaa#...#b#",
"..#bb#.#aa##mm###biim#aaa#..#bb#",
"..#bb#####bbikbbbbimi#aaa#..#bb#",
"..###bbbbb#bbk###bikbb#aa#..#bb#",
"..#bbbb#bb#bbbbbbbbbbbb##...#bb#",
"..#bb###bb#############nn###bbb#",
".#bb#.#bb#nnnnnnnnnnnnnnn#bbbb#.",
".###..########################.."
]

class PrefsBA(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        self.image0 = QPixmap(image0_data)

        if not name:
            self.setName("PrefsBA")

        self.setIcon(self.image0)
        self.setSizeGripEnabled(0)


        LayoutWidget = QWidget(self,"layout5")
        LayoutWidget.setGeometry(QRect(11,6,519,246))
        layout5 = QVBoxLayout(LayoutWidget,11,6,"layout5")

        layout4 = QGridLayout(None,1,1,0,6,"layout4")

        self.TextLabel2 = QLabel(LayoutWidget,"TextLabel2")
        self.TextLabel2.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Minimum,0,0,self.TextLabel2.sizePolicy().hasHeightForWidth()))

        layout4.addWidget(self.TextLabel2,1,0)

        self.browserButton = QPushButton(LayoutWidget,"browserButton")
        self.browserButton.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.browserButton.sizePolicy().hasHeightForWidth()))

        layout4.addWidget(self.browserButton,0,3)

        self.browserEdit = QLineEdit(LayoutWidget,"browserEdit")

        layout4.addMultiCellWidget(self.browserEdit,0,0,1,2)

        self.fontButtonMatch = QPushButton(LayoutWidget,"fontButtonMatch")

        layout4.addMultiCellWidget(self.fontButtonMatch,2,3,1,3)

        self.textLabel1 = QLabel(LayoutWidget,"textLabel1")

        layout4.addWidget(self.textLabel1,2,0)

        self.fontButton = QPushButton(LayoutWidget,"fontButton")

        layout4.addMultiCellWidget(self.fontButton,1,1,1,3)

        self.emailServerEdit = QLineEdit(LayoutWidget,"emailServerEdit")

        layout4.addMultiCellWidget(self.emailServerEdit,4,4,1,3)

        self.TextLabel1_2Emaii = QLabel(LayoutWidget,"TextLabel1_2Emaii")
        self.TextLabel1_2Emaii.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Minimum,0,0,self.TextLabel1_2Emaii.sizePolicy().hasHeightForWidth()))

        layout4.addMultiCellWidget(self.TextLabel1_2Emaii,3,4,0,0)

        self.TextLabel1_2 = QLabel(LayoutWidget,"TextLabel1_2")
        self.TextLabel1_2.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Minimum,0,0,self.TextLabel1_2.sizePolicy().hasHeightForWidth()))

        layout4.addWidget(self.TextLabel1_2,5,0)
        Spacer1_2 = QSpacerItem(380,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout4.addMultiCell(Spacer1_2,5,5,2,3)

        self.recentFilesSpinBox = QSpinBox(LayoutWidget,"recentFilesSpinBox")
        self.recentFilesSpinBox.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.recentFilesSpinBox.sizePolicy().hasHeightForWidth()))
        self.recentFilesSpinBox.setMaxValue(25)
        self.recentFilesSpinBox.setValue(5)

        layout4.addWidget(self.recentFilesSpinBox,5,1)

        self.TextLabel1 = QLabel(LayoutWidget,"TextLabel1")
        self.TextLabel1.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Minimum,0,0,self.TextLabel1.sizePolicy().hasHeightForWidth()))

        layout4.addWidget(self.TextLabel1,0,0)
        layout5.addLayout(layout4)
        Spacer1 = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
        layout5.addItem(Spacer1)

        Layout1 = QHBoxLayout(None,0,6,"Layout1")

        self.buttonHelp = QPushButton(LayoutWidget,"buttonHelp")
        self.buttonHelp.setAutoDefault(1)
        Layout1.addWidget(self.buttonHelp)
        Horizontal_Spacing2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(Horizontal_Spacing2)

        self.buttonApply = QPushButton(LayoutWidget,"buttonApply")
        self.buttonApply.setAutoDefault(1)
        Layout1.addWidget(self.buttonApply)

        self.buttonOk = QPushButton(LayoutWidget,"buttonOk")
        self.buttonOk.setAutoDefault(1)
        self.buttonOk.setDefault(1)
        Layout1.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(LayoutWidget,"buttonCancel")
        self.buttonCancel.setAutoDefault(1)
        Layout1.addWidget(self.buttonCancel)
        layout5.addLayout(Layout1)

        self.languageChange()

        self.resize(QSize(540,257).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.buttonOk,SIGNAL("clicked()"),self.accept)
        self.connect(self.buttonCancel,SIGNAL("clicked()"),self.reject)
        self.connect(self.browserButton,SIGNAL("pressed()"),self.browser_slot)
        self.connect(self.fontButton,SIGNAL("pressed()"),self.font_slot)
        self.connect(self.buttonHelp,SIGNAL("pressed()"),self.help_slot)
        self.connect(self.buttonApply,SIGNAL("pressed()"),self.apply_slot)
        self.connect(self.fontButtonMatch,SIGNAL("pressed()"),self.match_font_slot)

        self.setTabOrder(self.browserEdit,self.browserButton)
        self.setTabOrder(self.browserButton,self.fontButton)
        self.setTabOrder(self.fontButton,self.emailServerEdit)
        self.setTabOrder(self.emailServerEdit,self.recentFilesSpinBox)
        self.setTabOrder(self.recentFilesSpinBox,self.buttonHelp)
        self.setTabOrder(self.buttonHelp,self.buttonApply)
        self.setTabOrder(self.buttonApply,self.buttonOk)
        self.setTabOrder(self.buttonOk,self.buttonCancel)


    def languageChange(self):
        self.setCaption(self.__tr("Preferences"))
        self.TextLabel2.setText(self.__tr("Editor Font:"))
        self.browserButton.setText(self.__tr("..."))
        self.fontButtonMatch.setText(QString.null)
        self.textLabel1.setText(self.__tr("Match Font:"))
        self.fontButton.setText(QString.null)
        self.TextLabel1_2Emaii.setText(self.__tr("Email Server:"))
        self.TextLabel1_2.setText(self.__tr("Recent Files:"))
        self.TextLabel1.setText(self.__tr("Web Browser:"))
        self.buttonHelp.setText(self.__tr("&Help"))
        self.buttonApply.setText(self.__tr("&Apply"))
        self.buttonOk.setText(self.__tr("&OK"))
        self.buttonCancel.setText(self.__tr("&Cancel"))


    def font_slot(self):
        print "PrefsBA.font_slot(): Not implemented yet"

    def help_slot(self):
        print "PrefsBA.help_slot(): Not implemented yet"

    def browser_slot(self):
        print "PrefsBA.browser_slot(): Not implemented yet"

    def apply_slot(self):
        print "PrefsBA.apply_slot(): Not implemented yet"

    def match_font_slot(self):
        print "PrefsBA.match_font_slot(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("PrefsBA",s,c)
