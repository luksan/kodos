# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/phil/work/kodos/modules/newUserDialogBA.ui'
#
# Created: Sat Jul 9 09:40:30 2005
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
image1_data = [
"33 25 9 1",
"a c None",
"# c None",
". c None",
"b c #000000",
"f c #838183",
"d c #83ae5a",
"e c #c5c2c5",
"g c #d555d5",
"c c #ffffff",
".#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.",
"a.a.abbbbbbba.a.a.a.abbbbbbba.a.a",
".#.bbbccccccbb.#.#.bbccccccbbb.#.",
"abbbcbcccccccdb.a.bccccccccbcbbba",
".bebcbcccccccedb.bcecccccccbcbeb.",
"abebcbcccccccceebeeccccccccbcbeba",
".bebcbcccccccecebececccccccbcbeb.",
"abebcbcccccccceebeeccccccccbcbeba",
".bebcbcccccccecebececccccccbcbeb.",
"abebcbcccccccceebeeccccccccbcbeba",
".bebcbcccccccecebececccccccbcbeb.",
"abebcbcccccccceebeeccccccccbcbeba",
".bebcbcccccccecebececccccccbcbeb.",
"abebcbcccccccceebeeccccccccbcbeba",
".bebcbcccccccecebececccccccbcbeb.",
"abebcbcccccccceeeeeccccccccbcbeba",
".bebcbcccccccecebececccccccbcbeb.",
"abebcbcccccccceebeeccccccccbcbeba",
".bebcbbbbbbbcecebececbbbbbbbcbeb.",
"abebbfffffffbbeebeebbfffffffbbeba",
".bebffffffffffbebebffffffffffbeb.",
"abeeeeeeeeeeeeebfbeeeeeeeeeeeeeba",
".bbbbbbbbbbbbbeebeebbbbbbbbbbbbb.",
"a.a.a.a.a.a.gcbbbbb.a.a.a.a.a.a.a",
".#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#."
]
image2_data = [
"34 34 29 1",
". c None",
"# c #000000",
"d c #313062",
"c c #31346a",
"v c #31656a",
"q c #31696a",
"r c #31ff9c",
"a c #39346a",
"s c #39696a",
"w c #39ff9c",
"z c #39ffa4",
"p c #414441",
"u c #4a444a",
"x c #525552",
"A c #5a555a",
"y c #5a595a",
"i c #6265cd",
"b c #6a65cd",
"e c #6a69d5",
"t c #7b797b",
"k c #acaaac",
"j c #acaeac",
"o c #b4aeb4",
"h c #cd9962",
"l c #cd996a",
"f c #d5996a",
"n c #d59d6a",
"g c #ffce9c",
"m c #ffcea4",
"..................................",
"...........######.................",
"...........#abac#.................",
"...........#deda#.................",
"...........#abac#.................",
"...........#dedc#.................",
"......######abac#######...........",
"......#fgfh#ieia#jkjkj#...........",
"......#lmln######kokok#####.......",
"......#g.gg#ieic#jk.pj#qrs#.......",
"......#potu######kopok#vwv#.......",
"......#fgfh#deda#jkjkj#srq#.......",
"......#xoty#abac#kokok#vzv#.......",
"......#Aktx#dedc#jkjkj#qrs#.......",
"......#Aoty#abac#kokok#vwv#.......",
"......#Aktx#deda#jkjkj#srq#.......",
"......#xoty#abac#kokok#vzv#.......",
"......#Aktx#dedc#jkjkj#qrs#.......",
".....##Aoty#abac#kokok#vwv##......",
"....#u#fgfh#deda#jkjkj#srq#u#.....",
"...#up#g.gg#abac#kokok#vzv#pu#....",
"...#pu#uktp#dedc#jkjkj#qrs#up#....",
"..#pup#lgln#abac#kokok#vwv#pup#...",
"..#upu#fgfh#ieia#jkjkj#srq#upu#...",
"..#pup#lmln######kokok#vzv#pup#...",
"..#upu#fgfh#ieic#jkjkj#qrs#upu#...",
"..#pup#lgln######kokok#vwv#pup#...",
"..#upu#fgfh#deda#jkjkj#srq#upu#...",
"..#pup#lmln#abac#kokok#vzv#pup#...",
"..#upu#fgfh#dedc#jk.pj#qrs#upu#...",
"..#pup#lgln#abac#kopok#vwv#pup#...",
"..#upu#fgfh#deda#jkjkj#srq#upu#...",
"..#############################...",
".................................."
]

class NewUserDialog(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        self.image0 = QPixmap(image0_data)
        self.image1 = QPixmap(image1_data)
        self.image2 = QPixmap(image2_data)

        if not name:
            self.setName("NewUserDialog")

        self.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Preferred,0,0,self.sizePolicy().hasHeightForWidth()))
        self.setIcon(self.image0)

        NewUserDialogLayout = QVBoxLayout(self,11,6,"NewUserDialogLayout")

        layout14 = QVBoxLayout(None,0,6,"layout14")

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)
        layout14.addWidget(self.textLabel1)

        layout13 = QGridLayout(None,1,1,0,6,"layout13")

        self.pixmapLabel2 = QLabel(self,"pixmapLabel2")
        self.pixmapLabel2.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.pixmapLabel2.sizePolicy().hasHeightForWidth()))
        self.pixmapLabel2.setPixmap(self.image1)
        self.pixmapLabel2.setScaledContents(1)

        layout13.addWidget(self.pixmapLabel2,1,1)

        self.textLabel4 = QLabel(self,"textLabel4")

        layout13.addWidget(self.textLabel4,1,0)

        self.pixmapLabel1 = QLabel(self,"pixmapLabel1")
        self.pixmapLabel1.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.pixmapLabel1.sizePolicy().hasHeightForWidth()))
        self.pixmapLabel1.setPixmap(self.image2)
        self.pixmapLabel1.setScaledContents(1)

        layout13.addWidget(self.pixmapLabel1,0,1)

        self.textLabel3 = QLabel(self,"textLabel3")

        layout13.addWidget(self.textLabel3,0,0)
        layout14.addLayout(layout13)
        NewUserDialogLayout.addLayout(layout14)

        layout15 = QHBoxLayout(None,0,6,"layout15")
        spacer10 = QSpacerItem(241,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout15.addItem(spacer10)

        self.okButton = QPushButton(self,"okButton")
        self.okButton.setDefault(1)
        layout15.addWidget(self.okButton)
        NewUserDialogLayout.addLayout(layout15)

        self.languageChange()

        self.resize(QSize(338,326).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.okButton,SIGNAL("clicked()"),self.accept)


    def languageChange(self):
        self.setCaption(self.__tr("Kodos new user information"))
        self.textLabel1.setText(self.__tr("<h3>Welcome to Kodos.</h3>\n"
"<p></p>\n"
"It appears that this is your first time using \n"
"Kodos - The Python Regular Expression Debugger.\n"
"<p></p>\n"
"In order to help you familiarize yourself with Kodos, you may wish to explore\n"
"the Regex Library.  Additionally, Kodos contains a Python Regex Reference Guide. \n"
"You can access these tools by clicking on the appropriate toolbar icon."))
        self.textLabel4.setText(self.__tr("<b>Regex Reference Guide</b>"))
        self.textLabel3.setText(self.__tr("<b>Regex Library</b>"))
        self.okButton.setText(self.__tr("&OK"))
        self.okButton.setAccel(self.__tr("Alt+O"))


    def __tr(self,s,c = None):
        return qApp.translate("NewUserDialog",s,c)
