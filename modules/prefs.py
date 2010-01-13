#  prefs.py: -*- Python -*-  DESCRIPTIVE TEXT.

from util import *
from prefsBA import PrefsBA
import help

##class Prefs(PrefsBA):
##    def __init__(self, parent=None, name=None, modal=0):
##        print type(self)
##        PrefsBA.__init__(self, parent, name, modal)
##        self.parent = parent

def get_font_value(s):
    if s in ('0', 'False'): return 0
    else:                   return 1

        
class Preferences(PrefsBA):
    def __init__(self, parent, autoload=0):
        self.parent = parent
        PrefsBA.__init__(self, parent)

        prefsFilename = "prefs"
        self.prefsPath = getHomeDirectory() + os.sep + ".kodos" + os.sep + prefsFilename
        if autoload: self.load()
        
    def load(self):
        try:
            fp = open(self.prefsPath, "r")
        except:
            return
        
        prefsList = fp.readlines()
        for pref in prefsList:
            preference, setting = string.split(pref, ":", 1)
            setting = string.strip(setting)
            if preference == 'Font' and setting:
                self.parseFontStr(setting, self.parent.setfont)
            if preference == 'Match Font' and setting:
                self.parseFontStr(setting, self.parent.setMatchFont)
            if preference == 'Web Browser' and setting:
                self.browserEdit.setText(setting)
            if preference == 'Email Server' and setting:
                self.emailServerEdit.setText(setting)
            if preference == 'Recent Files' and setting:
                self.recentFilesSpinBox.setValue(int(setting))
            

    def save(self):
        try:
            fp = open(self.prefsPath, "w")
        except:
            print "Could not save preferences:", self.prefsPath
            return

        #print self.prefsPath
        f = self.parent.getfont()

        fp.write("Font: %s:%s:%s:%s:%s:%s\n" %
                 (f.family(), f.pointSize(),
                  f.bold(), f.italic(),
                  f.underline(), f.strikeOut()))

        f = self.parent.getMatchFont()
        fp.write("Match Font: %s:%s:%s:%s:%s:%s\n" %
                 (f.family(), f.pointSize(),
                  f.bold(), f.italic(),
                  f.underline(), f.strikeOut()))

        fp.write("Web Browser: %s\n" % str(self.browserEdit.text()))
        fp.write("Email Server: %s\n" % str(self.emailServerEdit.text()))
        fp.write("Recent Files: %s\n" % str(self.recentFilesSpinBox.text()))
        fp.close()
        self.parent.emit(PYSIGNAL('prefsSaved()'), () )


    def parseFontStr(self, fontstr, meth):
        # parse a font in the form: family:pt size:bold:italic:underline:strikeout
        parts = string.split(fontstr, ":")
        if len(parts) != 6: return
        
        f = QFont()
        f.setFamily(parts[0])
        f.setPointSize(int(parts[1]))
        f.setBold(get_font_value(parts[2]))
        f.setItalic(get_font_value(parts[3]))
        f.setUnderline(get_font_value(parts[4]))
        f.setStrikeOut(get_font_value(parts[5]))
        meth(f)
        #self.parent.setfont(f)


    def setFontButtonText(self, button, font):
        #self.fontButton.setText("%s %s" % (str(font.family()),font.pointSize() ))
        button.setText("%s %s" % (str(font.family()),font.pointSize() ))

    def showPrefsDialog(self):
        f = self.parent.getfont()
        self.fontButton.setFont(f)
        self.setFontButtonText(self.fontButton, f)

        f = self.parent.getMatchFont()
        self.fontButtonMatch.setFont(f)
        self.setFontButtonText(self.fontButtonMatch, f)

        self.show()

    def font_slot(self):
        (font, ok) = QFontDialog.getFont(self.fontButton.font())
        if ok:
            self.fontButton.setFont(font)
            self.setFontButtonText(self.fontButton, font)

    def match_font_slot(self):
        (font, ok) = QFontDialog.getFont(self.fontButtonMatch.font())
        if ok:
            self.fontButtonMatch.setFont(font)
            self.setFontButtonText(self.fontButtonMatch, font)        

    def browser_slot(self):
        fn = QFileDialog.getOpenFileName(self.browserEdit.text(), "All (*)",
                                         self, "Choose Web Browser")
        if not fn.isEmpty():
            self.browserEdit.setText(fn)


    def apply_slot(self):
        self.parent.setfont(self.fontButton.font())
        self.parent.setMatchFont(self.fontButtonMatch.font())
        self.save()


    def accept(self):
        self.apply_slot()
        QDialog.accept(self)


    def help_slot(self):
        self.helpWindow = help.Help(self, "prefs.html")

