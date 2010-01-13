# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/phil/work/kodos/modules/regexLibraryBA.ui'
#
# Created: Sat Jul 9 09:40:35 2005
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
"22 22 8 1",
". c None",
"# c #000000",
"e c #000083",
"c c #838100",
"b c #838183",
"d c #c5c2c5",
"a c #ffff00",
"f c #ffffff",
"......................",
".......#####..........",
"..######aaa######.....",
".######aaaaa######....",
"##bcb##a###a##bcb##...",
"#bcb#ddddddddd#bcb#...",
"#cbc#ddddddddd#cbc#...",
"#bcb###########bcb#...",
"#cbcbcbcbcbcbcbcbc#...",
"#bcbcbcbcbcbcbcbcb#...",
"#cbcbcbceeeeeeeeee#...",
"#bcbcbcbefffffffefe...",
"#cbcbcbcefeeeeefeffe..",
"#bcbcbcbefffffffefffe.",
"#cbcbcbcefeeeeefeffffe",
"#bcbcbcbefffffffeeeeee",
"#cbcbcbcefeeeeeffffffe",
"#bcbcbcbeffffffffffffe",
"#cbcbcbcefeeeeeeeeeefe",
".#######effffffffffffe",
"........eeeeeeeeeeeeee",
"......................"
]
image2_data = [
"20 20 20 1",
". c None",
"b c #000000",
"n c #181818",
"q c #202420",
"p c #313031",
"k c #393c39",
"c c #525000",
"a c #626162",
"r c #6a6d6a",
"l c #838100",
"j c #949500",
"# c #b4b6b4",
"i c #bdba00",
"o c #dede00",
"d c #ffaa20",
"e c #ffc66a",
"f c #ffe2b4",
"m c #ffff00",
"h c #ffff6a",
"g c #ffffff",
".#aaaaaaaaaaaaaaaa#.",
"#abbbbbbbbbbbbbbbba#",
"abcdeeeeeeeeeeeedcba",
"abdefffffffffffffdba",
"abefgghijaklihhhfeba",
"abefghmklhabnohhfeba",
"abefghobphobbihhfeba",
"abefghhpahobbihhfeba",
"abefghhhhhlbkohhfeba",
"abefghhhhhqaohhhfeba",
"abefhhhhhrihhhhhfeba",
"abefhhhhokjhhhhhfeba",
"abefhhhhabbhhhhhfeba",
"abefhhhhjbkhhhhhfeba",
"abdehhhhhhhhhhffedba",
"abcdfhffeeeeeeeedcba",
".abbfffedbbbbbbbbba#",
"..abeedbbkaaaaaaaa#.",
"..abdbbka...........",
"..abbba#............"
]

class RegexLibraryBA(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        self.image0 = QPixmap(image0_data)
        self.image1 = QPixmap(image1_data)
        self.image2 = QPixmap(image2_data)

        if not name:
            self.setName("RegexLibraryBA")

        self.setIcon(self.image0)

        self.setCentralWidget(QWidget(self,"qt_central_widget"))
        RegexLibraryBALayout = QGridLayout(self.centralWidget(),1,1,11,6,"RegexLibraryBALayout")

        self.groupBox5 = QGroupBox(self.centralWidget(),"groupBox5")
        self.groupBox5.setColumnLayout(0,Qt.Vertical)
        self.groupBox5.layout().setSpacing(6)
        self.groupBox5.layout().setMargin(11)
        groupBox5Layout = QGridLayout(self.groupBox5.layout())
        groupBox5Layout.setAlignment(Qt.AlignTop)

        self.descriptionListBox = QListBox(self.groupBox5,"descriptionListBox")

        groupBox5Layout.addWidget(self.descriptionListBox,0,0)

        RegexLibraryBALayout.addWidget(self.groupBox5,0,0)

        self.tabWidget3 = QTabWidget(self.centralWidget(),"tabWidget3")

        self.tab = QWidget(self.tabWidget3,"tab")
        tabLayout = QGridLayout(self.tab,1,1,11,6,"tabLayout")

        self.regexTextBrowser = QTextBrowser(self.tab,"regexTextBrowser")
        self.regexTextBrowser.setTextFormat(QTextBrowser.PlainText)

        tabLayout.addWidget(self.regexTextBrowser,0,0)
        self.tabWidget3.insertTab(self.tab,QString.fromLatin1(""))

        self.tab_2 = QWidget(self.tabWidget3,"tab_2")
        tabLayout_2 = QGridLayout(self.tab_2,1,1,11,6,"tabLayout_2")

        self.noteTextBrowser = QTextBrowser(self.tab_2,"noteTextBrowser")
        self.noteTextBrowser.setTextFormat(QTextBrowser.PlainText)

        tabLayout_2.addWidget(self.noteTextBrowser,0,0)

        layout3 = QHBoxLayout(None,0,6,"layout3")

        self.textLabel3 = QLabel(self.tab_2,"textLabel3")
        layout3.addWidget(self.textLabel3)

        self.contribEdit = QLineEdit(self.tab_2,"contribEdit")
        self.contribEdit.setFrameShape(QLineEdit.LineEditPanel)
        self.contribEdit.setFrameShadow(QLineEdit.Sunken)
        self.contribEdit.setReadOnly(1)
        layout3.addWidget(self.contribEdit)

        tabLayout_2.addLayout(layout3,1,0)
        self.tabWidget3.insertTab(self.tab_2,QString.fromLatin1(""))

        RegexLibraryBALayout.addWidget(self.tabWidget3,1,0)

        self.editPasteAction = QAction(self,"editPasteAction")
        self.editPasteAction.setIconSet(QIconSet(self.image1))
        self.helpHelpAction = QAction(self,"helpHelpAction")
        self.helpHelpAction.setIconSet(QIconSet(self.image2))
        self.exitAction = QAction(self,"exitAction")


        self.toolBar = QToolBar(QString(""),self,Qt.DockTop)

        self.editPasteAction.addTo(self.toolBar)


        self.MenuBar = QMenuBar(self,"MenuBar")


        self.fileMenu = QPopupMenu(self)
        self.fileMenu.insertSeparator()
        self.exitAction.addTo(self.fileMenu)
        self.MenuBar.insertItem(QString(""),self.fileMenu,1)

        self.editMenu = QPopupMenu(self)
        self.editPasteAction.addTo(self.editMenu)
        self.editMenu.insertSeparator()
        self.MenuBar.insertItem(QString(""),self.editMenu,2)

        self.helpMenu = QPopupMenu(self)
        self.helpHelpAction.addTo(self.helpMenu)
        self.MenuBar.insertItem(QString(""),self.helpMenu,3)


        self.languageChange()

        self.resize(QSize(491,490).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.editPasteAction,SIGNAL("activated()"),self.editPaste)
        self.connect(self.descriptionListBox,SIGNAL("highlighted(QListBoxItem*)"),self.descSelectedSlot)
        self.connect(self.exitAction,SIGNAL("activated()"),self.close)
        self.connect(self.descriptionListBox,SIGNAL("doubleClicked(QListBoxItem*)"),self.editPaste)


    def languageChange(self):
        self.setCaption(self.__tr("Kodos - Regex Library"))
        self.groupBox5.setTitle(self.__tr("Description"))
        self.tabWidget3.changeTab(self.tab,self.__tr("Regex"))
        self.textLabel3.setText(self.__tr("Contributed By:"))
        self.tabWidget3.changeTab(self.tab_2,self.__tr("Notes"))
        self.editPasteAction.setText(self.__tr("Paste"))
        self.editPasteAction.setMenuText(self.__tr("&Paste Example Into Kodos"))
        self.editPasteAction.setToolTip(self.__tr("Paste This Example Into Kodos"))
        self.editPasteAction.setAccel(self.__tr("Ctrl+V"))
        self.helpHelpAction.setText(self.__tr("Help"))
        self.helpHelpAction.setMenuText(self.__tr("&Help"))
        self.helpHelpAction.setAccel(self.__tr("Ctrl+/"))
        self.exitAction.setText(self.__tr("Exit"))
        self.exitAction.setMenuText(self.__tr("&Exit"))
        self.toolBar.setLabel(self.__tr("Tools"))
        if self.MenuBar.findItem(1):
            self.MenuBar.findItem(1).setText(self.__tr("&File"))
        if self.MenuBar.findItem(2):
            self.MenuBar.findItem(2).setText(self.__tr("&Edit"))
        if self.MenuBar.findItem(3):
            self.MenuBar.findItem(3).setText(self.__tr("&Help"))


    def fileNew(self):
        print "RegexLibraryBA.fileNew(): Not implemented yet"

    def fileOpen(self):
        print "RegexLibraryBA.fileOpen(): Not implemented yet"

    def fileSave(self):
        print "RegexLibraryBA.fileSave(): Not implemented yet"

    def fileSaveAs(self):
        print "RegexLibraryBA.fileSaveAs(): Not implemented yet"

    def filePrint(self):
        print "RegexLibraryBA.filePrint(): Not implemented yet"

    def fileExit(self):
        print "RegexLibraryBA.fileExit(): Not implemented yet"

    def editUndo(self):
        print "RegexLibraryBA.editUndo(): Not implemented yet"

    def editRedo(self):
        print "RegexLibraryBA.editRedo(): Not implemented yet"

    def editCut(self):
        print "RegexLibraryBA.editCut(): Not implemented yet"

    def editCopy(self):
        print "RegexLibraryBA.editCopy(): Not implemented yet"

    def editPaste(self):
        print "RegexLibraryBA.editPaste(): Not implemented yet"

    def editFind(self):
        print "RegexLibraryBA.editFind(): Not implemented yet"

    def helpIndex(self):
        print "RegexLibraryBA.helpIndex(): Not implemented yet"

    def helpContents(self):
        print "RegexLibraryBA.helpContents(): Not implemented yet"

    def helpAbout(self):
        print "RegexLibraryBA.helpAbout(): Not implemented yet"

    def descSelectedSlot(self):
        print "RegexLibraryBA.descSelectedSlot(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("RegexLibraryBA",s,c)
