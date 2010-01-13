#!/usr/bin/env python
#  kodos.py: -*- Python -*-  DESCRIPTIVE TEXT.

import sys
import os
import string
import re
import copy
import cPickle
import types
import getopt
import urllib
import signal

try:
    from qt import *
except:
    print """Could not locate the PyQt module.  Please make sure that
you have installed PyQt for the version of Python that you are running."""
    sys.exit(1)
    
### make sure that this script can find kodos specific modules ###
import os.path
from distutils.sysconfig import get_python_lib

sys.path.insert(0, os.path.join(get_python_lib(), "kodos")) 

###################################################################

from modules.kodosBA import *
from modules.util import *
from modules.about import *
import modules.help as help
from modules.status_bar import *
from modules.reference import *
from modules.prefs import *
from modules.webbrowser import launch_browser
from modules.reportBug import reportBugWindow
from modules.version import VERSION
from modules.recent_files import RecentFiles
import modules.xpm as xpm
from modules.urlDialog import URLDialog
from modules.migrate_settings import MigrateSettings
from modules.regexLibrary import RegexLibrary
from modules.newUserDialogBA import NewUserDialog


# match status
MATCH_NA       = 0
MATCH_OK       = 1
MATCH_FAIL     = 2
MATCH_PAUSED   = 3
MATCH_EXAMINED = 4

TRUE  = 1
FALSE = 0

TIMEOUT = 3

# regex to find special flags which must begin at beginning of line
# or after some spaces
EMBEDDED_FLAGS = r"^ *\(\?(?P<flags>[iLmsux]*)\)"

RX_BACKREF = re.compile(r"""\\\d""")

STATE_UNEDITED = 0
STATE_EDITED   = 1

GEO = "kodos_geometry"

# colors for normal & examination mode
QCOLOR_WHITE  = QColor(Qt.white)     # normal
QCOLOR_YELLOW = QColor(255,255,127)  # examine

QT_VERS = int(QT_VERSION_STR[0])

if QT_VERS < 3:
    print "Qt versions prior to 3.0 are no longer supported"
    sys.exit(0)

try:
    signal.SIGALRM
    HAS_ALARM = 1
except:
    HAS_ALARM = 0


##############################################################################
#
# The Kodos class which defines the main functionality and user interaction
#
##############################################################################

class Kodos(KodosBA):
    def __init__(self, filename, debug):
        KodosBA.__init__(self)

        self.debug = debug
        self.regex = ""
        self.matchstring = ""
        self.replace = ""
        self.flags = 0
        self.is_paused = 0
        self.is_examined = 0
        self.filename = ""
        self.match_num = 1 # matches are labeled 1..n
        self.replace_num = 0 # replace all
        self.url = None
        self.group_tuples = None
        self.editstate = STATE_UNEDITED

        self.ref_win = None
        self.regexlibwin = None
        
        self.embedded_flags_obj = re.compile(EMBEDDED_FLAGS)
        self.embedded_flags = ""
        self.regex_embedded_flags_removed = ""

        self.createStatusBar()

        self.MSG_NA     = self.tr("Enter a regular expression and a string to match against")
        self.MSG_PAUSED = self.tr("Kodos regex processing is paused.  Click the pause icon to unpause")
        self.MSG_FAIL   = self.tr("Pattern does not match")

        
        self.statusPixmapsDict = {MATCH_NA: QPixmap(xpm.yellowStatusIcon),
                                  MATCH_OK: QPixmap(xpm.greenStatusIcon),
                                  MATCH_FAIL: QPixmap(xpm.redStatusIcon),
                                  MATCH_PAUSED: QPixmap(xpm.pauseStatusIcon)}

        
        self.updateStatus(self.MSG_NA, MATCH_NA)

        restoreWindowSettings(self, GEO)
        
        self.show()

        self.prefs = Preferences(self, 1)
        self.recent_files = RecentFiles(self,
                                        self.prefs.recentFilesSpinBox.value(),
                                        self.debug)

        self.matchTextBrowser.setTextFormat(QTextEdit.PlainText)

        if filename and self.openFile(filename):
            qApp.processEvents()

        self.connect(self, PYSIGNAL('prefsSaved()'), self.prefsSaved)

        self.connect(self.fileMenu,
                     SIGNAL('activated(int)'),
                     self.fileMenuHandler)
        
        self.connect(self, PYSIGNAL('pasteSymbol()'), self.paste_symbol)

        self.connect(self, PYSIGNAL('urlImported()'), self.urlImported)

        self.connect(self, PYSIGNAL('pasteRegexLib()'), self.pasteFromRegexLib)

        kodos_toolbar_logo(self.toolBar)
        if self.replace:  self.show_replace_widgets()
        else:             self.hide_replace_widgets()

        self.checkForKodosDir()


    def checkForKodosDir(self):
        kdir = os.path.join(getHomeDirectory(), ".kodos")
        if os.access(kdir, os.X_OK):
            return

        try:
            os.mkdir(kdir, 0755)
        except:
            print "Failed to create:", kdir

        self.newuserdialog = NewUserDialog()
        self.newuserdialog.show()
        

    def createStatusBar(self):
        self.status_bar = Status_Bar(self, FALSE, "")


    def updateStatus(self, status_string, status_value, duration=0, replace=FALSE, tooltip=''):
        pixmap = self.statusPixmapsDict.get(status_value)

        self.status_bar.set_message(status_string, duration, replace, tooltip, pixmap)


    def fileMenuHandler(self, menuid):
        if self.recent_files.isRecentFile(menuid):
            fn = str(self.fileMenu.text(menuid))
            self.recent_files.add(fn)
            self.openFile(fn)

    def prefsSaved(self):
        if self.debug: print "prefsSaved slot"
        self.recent_files.setNumShown(self.prefs.recentFilesSpinBox.value())   
  
        
    def kodos_edited_slot(self):
        # invoked whenever the user has edited something
        self.editstate = STATE_EDITED
        

    def checkbox_slot(self):
        self.flags = 0
        
        if self.ignorecaseCheckBox.isChecked():
            self.flags = self.flags + re.IGNORECASE

        if self.multilineCheckBox.isChecked():
            self.flags = self.flags + re.MULTILINE

        if self.dotallCheckBox.isChecked():
            self.flags = self.flags + re.DOTALL

        if self.verboseCheckBox.isChecked():
            self.flags = self.flags + re.VERBOSE

        if self.localeCheckBox.isChecked():
            self.flags = self.flags + re.LOCALE

        if self.unicodeCheckBox.isChecked():
            self.flags = self.flags + re.UNICODE

        self.process_regex()


    def set_flags(self, flags):
        # from the given integer value of flags, set the checkboxes
        # this is used when loading a saved file
        if flags & re.IGNORECASE:
            self.ignorecaseCheckBox.setChecked(1)
        else:
            self.ignorecaseCheckBox.setChecked(0)

        if flags & re.MULTILINE:
            self.multilineCheckBox.setChecked(1)
        else:
            self.multilineCheckBox.setChecked(0)
            
        if flags & re.DOTALL:
            self.dotallCheckBox.setChecked(1)
        else:
            self.dotallCheckBox.setChecked(0)
            
        if flags & re.VERBOSE:
            self.verboseCheckBox.setChecked(1)
        else:
            self.verboseCheckBox.setChecked(0)

        if flags & re.LOCALE:
            self.localeCheckBox.setChecked(1)
        else:
            self.localeCheckBox.setChecked(0)

        if flags & re.UNICODE:
            self.unicodeCheckBox.setChecked(1)
        else:
            self.unicodeCheckBox.setChecked(0)


    def get_flags_string(self):
        flags_str = ""
        
        if self.ignorecaseCheckBox.isChecked():
            flags_str += "| re.IGNORECASE"

        if self.multilineCheckBox.isChecked():
            flags_str += "| re.MULTILINE"

        if self.dotallCheckBox.isChecked():
            flags_str += "| re.DOTALL"

        if self.verboseCheckBox.isChecked():
            flags_str += "| re.VERBOSE"

        if self.localeCheckBox.isChecked():
            flags_str += "| re.LOCALE"

        if self.unicodeCheckBox.isChecked():
            flags_str += "| re.UNICODE"

        if flags_str: flags_str = ", " + flags_str[1:]
        return flags_str


    def get_embedded_flags_string(self):
        flags_str = flags = ""
        
        if self.ignorecaseCheckBox.isChecked():
            flags += "i"

        if self.multilineCheckBox.isChecked():
            flags += "m"

        if self.dotallCheckBox.isChecked():
            flags += "s"

        if self.verboseCheckBox.isChecked():
            flags += "x"

        if self.localeCheckBox.isChecked():
            flags += "L"

        if self.unicodeCheckBox.isChecked():
            flags += "u"

        if flags:
            flags_str = "(?" + flags + ")"

        return flags_str
        

    def pause(self):
        self.is_paused = not self.is_paused
        if self.debug: print "is_paused:", self.is_paused
        
        if self.is_paused:
            self.update_results(self.MSG_PAUSED, MATCH_PAUSED)
            self.matchNumberSpinBox.setDisabled(1)

        else:
            self.process_regex()
            self.matchNumberSpinBox.setEnabled(1)            


    def examine(self):
        self.is_examined = not self.is_examined
        if self.debug: print "is_examined:", self.is_examined
        
        if self.is_examined:
            color = QCOLOR_YELLOW
            regex = self.regex
            self.regex_saved = self.regex
            length = len(regex)
            found = 0
            self.regexMultiLineEdit.setReadOnly(1)
            self.stringMultiLineEdit.setReadOnly(1)
            self.replaceTextEdit.setReadOnly(1)
            for i in range(length, 0,  -1):
                regex = regex[:i]
                self.process_embedded_flags(self.regex)
                try:
                    m = re.search(regex, self.matchstring, self.flags)
                    if m:
                        if self.debug: print "examined regex:", regex
                        self.__refresh_regex_widget(color, regex)
                        return
                except:
                    pass
                
            self.__refresh_regex_widget(color, "")
        else:
            regex = self.regex_saved
            color = QCOLOR_WHITE
            self.regexMultiLineEdit.setReadOnly(0)
            self.stringMultiLineEdit.setReadOnly(0)
            self.replaceTextEdit.setReadOnly(0)
            self.__refresh_regex_widget(color, regex)
            

    def __refresh_regex_widget(self, base_qcolor, regex):
        self.regexMultiLineEdit.setPaletteBackgroundColor(base_qcolor)
        
        self.regexMultiLineEdit.blockSignals(1)
        self.regexMultiLineEdit.clear()
        self.regexMultiLineEdit.blockSignals(0)
        self.regexMultiLineEdit.setText(regex)


    def match_num_slot(self, num):
        self.match_num = num
        self.process_regex()


    def replace_num_slot(self, num):
        self.replace_num = num
        self.process_regex()
        

    def regex_changed_slot(self):
        try:
            self.regex = str(self.regexMultiLineEdit.text())
        except UnicodeError:
            self.regex = unicode(self.regexMultiLineEdit.text())
            
        self.process_regex()


    def string_changed_slot(self):
        try:
            self.matchstring = str(self.stringMultiLineEdit.text())
        except UnicodeError:
            self.matchstring = unicode(self.stringMultiLineEdit.text())
        self.process_regex()


    def hide_replace_widgets(self):
        self.spacerLabel.hide()
        self.replaceLabel.hide()
        self.replaceNumberSpinBox.hide()
        self.replaceTextBrowser.clear()
        self.replaceTextBrowser.setDisabled(TRUE)

    def show_replace_widgets(self):
        self.spacerLabel.show()
        self.replaceLabel.show()
        self.replaceNumberSpinBox.show()
        self.replaceNumberSpinBox.setEnabled(TRUE)
        self.replaceTextBrowser.setEnabled(TRUE)

    def replace_changed_slot(self):
        try:
            self.replace = str(self.replaceTextEdit.text())
        except UnicodeError:
            self.replace = unicode(self.replaceTextEdit.text())
            
        self.process_regex()
        if not self.replace:
            self.hide_replace_widgets()
        else:
            self.show_replace_widgets()


    def update_results(self, msg, val):
        self.updateStatus(msg, val)


    def populate_group_listview(self, tuples):
        # deprecated as of 2.4.0 - now uses QTable instead of QListView
        self.groupListView.clear()

        num_cols = 3
        for t in tuples:
            item = QListViewItem(self.groupListView)
            for col in range(num_cols):
                try:
                    item.setText(col, str(t[col]))
                except UnicodeError:
                    item.setText(col, unicode(t[col]))


    def populate_group_table(self, tuples):
        self.groupTable.setNumRows(len(tuples))

        row = 0
        for t in tuples:
            self.groupTable.setText(row, 0, unicode(t[1]))
            self.groupTable.setText(row, 1, unicode(t[2]))
            self.groupTable.adjustRow(row)
            row += 1
            
        self.groupTable.adjustColumn(0)
        self.groupTable.adjustColumn(1)


    def populate_code_textbrowser(self):
        self.codeTextBrowser.setText("")

        code =  "import re\n\n"
        code += "# common variables\n\n"
        code += "rawstr = r\"\"\"" + self.regex_embedded_flags_removed + "\"\"\"\n"
        code += "embedded_rawstr = r\"\"\"" + self.get_embedded_flags_string() + \
                self.regex_embedded_flags_removed + "\"\"\"\n"
        code += 'matchstr = \"\"\"' + self.matchstring + '\"\"\"'
        code += "\n\n"
        code += "# method 1: using a compile object\n"
        code += "compile_obj = re.compile(rawstr"
        if self.flags != 0:
            code += self.get_flags_string()
        code += ")\n"
        code += "match_obj = compile_obj.search(matchstr)\n\n"
        
        code += "# method 2: using search function (w/ external flags)\n"
        code += "match_obj = re.search(rawstr, matchstr"
        if self.flags != 0:
            code += self.get_flags_string()
        code += ")\n\n"

        code += "# method 3: using search function (w/ embedded flags)\n"
        embedded_str = self.get_embedded_flags_string() + self.regex_embedded_flags_removed
        code += "match_obj = re.search(embedded_rawstr, matchstr)\n\n"

        
        if self.group_tuples:
            code += "# Retrieve group(s) from match_obj\n"
            code += "all_groups = match_obj.groups()\n\n"
            code += "# Retrieve group(s) by index\n"
            i = 0
            named_grps = 0
            for grp in self.group_tuples:
                i += 1
                code += "group_%d = match_obj.group(%d)\n" % (i, i)
                if grp[1]: named_grps = 1

            if named_grps:
                code += "\n# Retrieve group(s) by name\n"    
                for grp in self.group_tuples:
                    if grp[1]:
                        code += "%s = match_obj.group('%s')\n" % (grp[1], grp[1])

            code += "\n"

        if self.replace:
            code += "# Replace string\n"
            code += "newstr = compile_obj.subn('%s', %d)\n" % (self.replace,
                                                               self.replace_num)
        

        self.codeTextBrowser.setText(code)


    def colorize_strings(self, strings, widget, cursorOffset=0):
        widget.clear()

        colors = (QColor(Qt.black), QColor(Qt.blue) )
        i = 0
        pos = widget.getCursorPosition()
        for s in strings:
            widget.setColor(colors[i%2])            
            widget.insert(s)
            if i == cursorOffset: pos = widget.getCursorPosition()
            i += 1
            
        widget.setCursorPosition(pos[0], pos[1])
        

    def populate_match_textbrowser(self, startpos, endpos):
        pre = post = match = ""
        
        match = self.matchstring[startpos:endpos]

        # prepend the beginning that didn't match
        if startpos > 0:
            pre = self.matchstring[0:startpos]
            
        # append the end that didn't match
        if endpos < len(self.matchstring):
            post = self.matchstring[endpos:]
            
        strings = [pre, match, post]
        self.colorize_strings(strings, self.matchTextBrowser, 1)


    def populate_replace_textbrowser(self, spans, nummatches, compile_obj):
        self.replaceTextBrowser.clear()
        if not spans: return

        num = self.replaceNumberSpinBox.value()
        if num == 0: num = nummatches
        text = self.matchstring
        
        replace_text = unicode(self.replaceTextEdit.text())
        if RX_BACKREF.search(replace_text):
            # if the replace string contains a backref we just use the
            # python regex methods for the substitution
            replaced = compile_obj.subn(replace_text, text, num)[0]
            self.replaceTextBrowser.setText(replaced)
            return
        
        numreplaced = idx = 0

        strings = []

        for span in spans:
            if span[0] != 0:
                s = text[idx:span[0]]
            else:
                s = ""
                
            idx = span[1]
            numreplaced += 1
            
            strings.append(s)
            strings.append(self.replace)

            if numreplaced >= num:
                strings.append(text[span[1]:])
                break

        self.colorize_strings(strings, self.replaceTextBrowser)

    
    def populate_matchAll_textbrowser(self, spans):
        self.matchAllTextBrowser.clear()
        if not spans: return

        idx = 0
        text = self.matchstring
        strings = []
        for span in spans:
            if span[0] != 0:
                s = text[idx:span[0]]
            else:
                s = ""
                
            idx = span[1]
            strings.append(s)
            strings.append(text[span[0]:span[1]])

        if 0 <= idx <= len(text): 
            strings.append(text[span[1]:])
            
        self.colorize_strings(strings, self.matchAllTextBrowser)

        
    def clear_results(self):
        #self.groupListView.clear()
        self.groupTable.setNumRows(0)
        self.codeTextBrowser.setText("")
        self.matchTextBrowser.setText("")
        self.matchNumberSpinBox.setEnabled(FALSE)
        self.replaceNumberSpinBox.setEnabled(FALSE)
        self.replaceTextBrowser.setText("")
        self.matchAllTextBrowser.setText("")
        

    def process_regex(self):
        def timeout(signum, frame):
            return

        if self.is_paused:
            return
        
        if not self.regex or not self.matchstring:
            self.update_results(self.MSG_NA, MATCH_NA)
            self.clear_results()
            return

        self.process_embedded_flags(self.regex)
        #print self.resultTabWidget.currentPageIndex()
        
        if HAS_ALARM:
            signal.signal(signal.SIGALRM, timeout)
            signal.alarm(TIMEOUT)

        try:
            compile_obj = re.compile(self.regex, self.flags)
            allmatches = compile_obj.findall(self.matchstring)

            replace_spans = []
            if allmatches and len(allmatches):
                self.matchNumberSpinBox.setMaxValue(len(allmatches))
                self.matchNumberSpinBox.setEnabled(TRUE)
                self.replaceNumberSpinBox.setMaxValue(len(allmatches))
                self.replaceNumberSpinBox.setEnabled(TRUE)
            else:
                self.matchNumberSpinBox.setEnabled(FALSE)
                self.replaceNumberSpinBox.setEnabled(FALSE)

            match_obj = compile_obj.search(self.matchstring)

        except Exception, e:
            self.update_results(str(e), MATCH_FAIL)
            return

        if HAS_ALARM:
            signal.alarm(0)

        if not match_obj:
            self.update_results(self.MSG_FAIL, MATCH_FAIL)

            self.clear_results()
            return

        # match_index is the list element for match_num.
        # Therefor match_num is for ui display
        # and match_index is for application logic.
        match_index = self.match_num - 1 
        
        if match_index > 0:
            for i in range(match_index):
                match_obj = compile_obj.search(self.matchstring,
                                               match_obj.end())
                
        self.populate_match_textbrowser(match_obj.start(), match_obj.end())

        self.group_tuples = []

        if match_obj.groups():
            #print match_obj.groups()
            s = "<font color=blue>"
            num_groups = len(match_obj.groups())

            group_nums = {}
            if compile_obj.groupindex:
                keys = compile_obj.groupindex.keys()
                for key in keys:
                    group_nums[compile_obj.groupindex[key]] = key

            if self.debug:
                print "group_nums:", group_nums                         
                print "grp index: ", compile_obj.groupindex
                print "groups:", match_obj.groups()
                print "span: ", match_obj.span()

            # create group_tuple in the form: (group #, group name, group matches)
            g = allmatches[match_index]
            if type(g) == types.TupleType:
                for i in range(len(g)):
                    group_tuple = (i+1, group_nums.get(i+1, ""), g[i])
                    self.group_tuples.append(group_tuple)
            else:
                self.group_tuples.append( (1, group_nums.get(1, ""), g) )
                        
            #print group_tuples
            self.populate_group_table(self.group_tuples)
            #self.populate_group_listview(self.group_tuples)

        str_pattern_matches = unicode(self.tr("Pattern matches"))
        str_found = unicode(self.tr("found"))
        str_match = unicode(self.tr("match"))
        str_matches = unicode(self.tr("matches"))

        if len(allmatches) == 1:
            status = "%s (%s 1 %s)" % (str_pattern_matches,
                                       str_found,
                                       str_match)
        else:
            status = "%s (%s %d %s)" % (str_pattern_matches,
                                        str_found,
                                        len(allmatches),
                                        str_match)
            
        self.update_results(status, MATCH_OK)
        self.populate_code_textbrowser()

        spans = self.findAllSpans(compile_obj)
        if self.replace:
            self.populate_replace_textbrowser(spans, len(allmatches), compile_obj)
        self.populate_matchAll_textbrowser(spans)


    def findAllSpans(self, compile_obj):
        spans = []
        
        match_obj = compile_obj.search(self.matchstring)

        last_span = None
        
        while match_obj:
            start = match_obj.start()
            end   = match_obj.end()
            span = (start, end)
            if last_span == span: break
            
            spans.append(span)
            
            last_span = span
            match_obj = compile_obj.search(self.matchstring, end)

        return spans


    def closeEvent(self, ev):
        self.checkEditState(self.tr("&No, Just Exit Kodos"))
        saveWindowSettings(self, GEO)

        try:
            self.regexlibwin.close()
        except:
            pass

        try:
            self.ref_win.close()
        except:
            pass
        ev.accept()


    def fileNew(self):
        self.checkEditState()
        self.filename = ""
        
        self.regexMultiLineEdit.setText("")
        self.stringMultiLineEdit.setText("")
        self.replaceTextEdit.setText("")
        self.set_flags(0)
        self.editstate = 0


    def importURL(self):
        self.urldialog = URLDialog(self, self.url)


    def urlImported(self, html, url):
        self.url = url
        self.stringMultiLineEdit.setText(html)
        

    def importFile(self):
        fn = QFileDialog.getOpenFileName(self.filename, "All (*)",
                                         self, "Import File")
        
        if fn.isEmpty():
            self.updateStatus(self.tr("A file was not selected for import"),
                              -1,
                              5,
                              TRUE)
            return None

        filename = str(fn)
        
        try:
            fp = open(filename, "r")
        except:
            msg = self.tr("Could not open file for reading: ") + filename
            self.updateStatus(msg, -1, 5, TRUE)
            return None
        
        data = fp.read()
        fp.close()
        self.stringMultiLineEdit.setText(data)

        
    def fileOpen(self):       
        fn = QFileDialog.getOpenFileName(self.filename,
                                         "*.kds\nAll (*)",
                                         self,
                                         "Open",
                                         self.tr("Open Kodos File"))        
        if not fn.isEmpty():
            filename = str(fn)
            if self.openFile(filename):
                self.recent_files.add(filename)


    def openFile(self, filename):
        self.checkEditState()

        self.filename = None

        try:
            fp = open(filename, "r")
        except:
            msg = self.tr("Could not open file for reading: ") + filename
            self.updateStatus(msg, -1, 5, TRUE)
            return None

        try:
            u = cPickle.Unpickler(fp)
            self.matchNumberSpinBox.setValue(1)
            self.regex = u.load()
            self.regexMultiLineEdit.setText(self.regex)

            self.matchstring = u.load()
            self.stringMultiLineEdit.setText(self.matchstring)
            
            flags = u.load()
            self.set_flags(flags)

            try:
                replace = u.load()
            except:
                # versions prior to 1.7 did not have replace functionality
                # so kds files saved w/ these versions will throw exception
                # here.
                replace = ""
            self.replaceTextEdit.setText(replace)
            
            self.filename = filename
            msg = "%s %s" % (filename, unicode(self.tr("loaded successfully")))
            self.updateStatus(msg, -1, 5, TRUE)
            self.editstate = STATE_UNEDITED
            return 1
        except Exception, e:
            if self.debug:  print unicode(e)
            msg = "%s %s" % (unicode(self.tr("Error reading from file:")),
                             filename)
            self.updateStatus(msg, -1, 5, TRUE)
            return 0


    def fileSaveAs(self):
        while 1:
            self.filedialog = QFileDialog(self.filename,
                                          "*.kds\nAll (*)",
                                          self,
                                          "Save",
                                          TRUE)
            self.filedialog.setCaption(self.tr("Save Kodos File"))
            self.filedialog.setMode(QFileDialog.AnyFile)
            #self.filedialog.show()
            ok = self.filedialog.exec_loop()

            filename = unicode(self.filedialog.selectedFile())
            if not ok or not filename:
                self.updateStatus(self.tr("No file selected to save"), -1, 5, TRUE)
                return
            filename = os.path.normcase(filename)

            basename = os.path.basename(filename)
            if basename.find(".") == -1:
                filename += ".kds"

            if os.access(filename, os.F_OK):
                message = "%s, %s %s\n%s" % (unicode(self.tr("The file")),
                                         filename,
                                         unicode(self.tr("already exists.")),
                                         unicode(self.tr("Would you like to replace it?")))
                cancel = QMessageBox.information(None,
                                                 self.tr("Replace file?"),
                                                 message,
                                                 self.tr("&Replace"),
                                                 self.tr("&Cancel"))
                if cancel:
                    # allow user to choose another filename
                    continue

            self.filename = filename
            self.fileSave()
            break


    def fileSave(self):
        if not self.filename:
            self.fileSaveAs()
            return

        try:
            fp = open(self.filename, "w")
        except:
            msg = "%s: %s" % (unicode(self.tr("Could not open file for writing:")),
                              self.filename)
            self.updateStatus(msg, -1, 5, TRUE)
            return None

        self.editstate = STATE_UNEDITED
        p = cPickle.Pickler(fp)
        p.dump(self.regex)
        p.dump(self.matchstring)
        p.dump(self.flags)
        p.dump(self.replace)
        
        fp.close()
        msg = "%s %s" % (unicode(self.filename),
                         unicode(self.tr("successfully saved")))
        self.updateStatus(msg, -1, 5, TRUE)
        self.recent_files.add(self.filename)


    def paste_symbol(self, symbol):
        self.regexMultiLineEdit.insert(symbol)


    def process_embedded_flags(self, regex):
        # determine if the regex contains embedded regex flags.
        # if not, return 0 -- inidicating that the regex has no embedded flags
        # if it does, set the appropriate checkboxes on the UI to reflect the flags that are embedded
        #   and return 1 to indicate that the string has embedded flags
        match = self.embedded_flags_obj.match(regex)
        if not match:
            self.embedded_flags = ""
            self.regex_embedded_flags_removed = regex
            return 0

        self.embedded_flags = match.group('flags')
        self.regex_embedded_flags_removed = self.embedded_flags_obj.sub("", regex, 1)
        
        for flag in self.embedded_flags:
            if flag == 'i':
                self.ignorecaseCheckBox.setChecked(1)
            elif flag == 'L':
                self.localeCheckBox.setChecked(1)
            elif flag == 'm':
                self.multilineCheckBox.setChecked(1)
            elif flag == 's':
                self.dotallCheckBox.setChecked(1)
            elif flag == 'u':
                self.unicodeCheckBox.setChecked(1)
            elif flag == 'x':
                self.verboseCheckBox.setChecked(1)

        return 1


    def checkEditState(self, noButtonStr=None):
        if not noButtonStr: noButtonStr = self.tr("&No")
        
        if self.editstate == STATE_EDITED:
            message = self.tr("You have made changes. Would you like to save them before continuing")
            
            prompt = QMessageBox.warning(None,
                                         self.tr("Save changes?"),
                                         message,
                                         self.tr("&Yes, Save Changes"),
                                         noButtonStr)
            
            if prompt == 0:
                self.fileSave()
                if not self.filename: self.checkEditState(noButtonStr)


    def pasteFromRegexLib(self, d):
        self.filename = ""
        self.checkEditState()

        self.regexMultiLineEdit.setText(d.get('regex'), "")
        self.stringMultiLineEdit.setText(d.get('text'), "")
        self.replaceTextEdit.setText(d.get('replace'), "")

        try:
            # set the current page if applicable
            self.resultTabWidget.setCurrentPage(int(d['tab']))
        except:
            pass
        self.editstate = STATE_UNEDITED


    def revert_file_slot(self):
        if not self.filename:
            self.updateStatus(self.tr("There is no filename to revert"),
                              -1,
                              5,
                              TRUE)
            return

        self.openFile(self.filename)


    def getWidget(self):
        widget = qApp.focusWidget()
        if (widget == self.regexMultiLineEdit or
            widget == self.stringMultiLineEdit or
            widget == self.replaceTextEdit or
            widget == self.codeTextBrowser):
            return widget
        else:
            return None


    def widgetMethod(self, methodstr, anywidget=0):
        # execute the methodstr of widget only if widget
        # is one of the editable widgets OR if the method
        # may be applied to any widget.
        widget = qApp.focusWidget()
        if anywidget or (
            widget == self.regexMultiLineEdit or
            widget == self.stringMultiLineEdit or
            widget == self.replaceTextEdit or
            widget == self.codeTextBrowser):
            try:
                eval("widget.%s" % methodstr)
            except:
                pass
        

    def editUndo(self):
        self.widgetMethod("undo()")
        
    def editRedo(self):
        self.widgetMethod("redo()")
            
    def editCopy(self):
        self.widgetMethod("copy()", 1)

    def editCut(self):
        self.widgetMethod("cut()")

    def editPaste(self):
        self.widgetMethod("paste()")


    def preferences(self):
        self.prefs.showPrefsDialog()
            
    def setfont(self, font):
        #print "font: ",  font
        #return
        self.regexMultiLineEdit.setFont(font)
        self.stringMultiLineEdit.setFont(font)
        self.replaceTextEdit.setFont(font)

    def setMatchFont(self, font):
        self.groupTable.setFont(font)
        self.matchTextBrowser.setFont(font)
        self.matchAllTextBrowser.setFont(font)
        self.replaceTextBrowser.setFont(font)
        self.codeTextBrowser.setFont(font)


    def getfont(self):
        return self.regexMultiLineEdit.font()


    def getMatchFont(self):
        return self.groupTable.font()

    
    def helpHelp(self):
        self.helpWindow = help.Help(self, "kodos.html")


    def helpPythonRegex(self):
        self.helpWindow = help.Help(self,
                                    "python" + os.sep + "module-re.html",
                                    str(self.prefs.browserEdit.text()))
        

    def helpRegexLib(self):
        f = os.path.join("help", "regex-lib.xml")
        self.regexlibwin = RegexLibrary(self, f)
        self.regexlibwin.show()

        
    def helpAbout(self):
        self.aboutWindow = About()
        self.aboutWindow.show()


    def kodos_website(self):
        self.launch_browser_wrapper("http://kodos.sourceforge.net")

            
    def check_for_update(self):
        url = "http://sourceforge.net/project/showfiles.php?group_id=43860"
        try:
            fp = urllib.urlopen(url)
        except:
            self.status_bar.set_message(self.tr("Failed to open url"),
                                        5,
                                        TRUE)
            return

        lines = fp.readlines()
        html = string.join(lines)

        rawstr = r"""kodos-(?P<version>.*?)\<"""
        #rawstr = r"""release_id=.*\">.*(kodos-)(?P<version>.*?)</[aA]>"""
        match_obj = re.search(rawstr, html)
        if match_obj:
            latest_version = match_obj.group('version')
            if latest_version == VERSION:
                QMessageBox.information(None,
                                        self.tr("No Update is Available"),
                                        unicode(self.tr("You are currently using the latest version of Kodos")) + " (%s)" % VERSION)
            else:
                message =  "%s\n\n%s: %s.\n%s: %s.\n\n%s\n" % \
                          (unicode(self.tr("There is a newer version of Kodos available.")),
                           unicode(self.tr("You are using version:")),
                           VERSION,
                           unicode(self.tr("The latest version is:")),
                           latest_version,
                           unicode(self.tr("Press OK to launch browser")))

                self.launch_browser_wrapper(url,
                                            self.tr("Kodos Update Available"),
                                            message)
        else:
            message = "%s.\n\n%s" % \
                      (unicode(self.tr("Unable to get version info from Sourceforge")),
                       unicode(self.tr("Press OK to launch browser")))
            self.launch_browser_wrapper(url,
                                        self.tr("Unknown version available"),
                                        message)


    def launch_browser_wrapper(self, url, caption=None, message=None):
        browser = str(self.prefs.browserEdit.text())
        if launch_browser(browser, url, caption, message):
            self.status_bar.set_message(self.tr("Launching web browser"),
                                        3,
                                        TRUE)
        else:
            self.status_bar.set_message(self.tr("Cancelled web browser launch"),
                                        3,
                                        TRUE)


    def reference_guide(self):
        self.ref_win = Reference(self)
        self.ref_win.show()
        

    def report_bug(self):
        self.bug_report_win = reportBugWindow(self)
        

##############################################################################
#
#
##############################################################################

def usage():
    print "kodos.py [-f filename | --file=filename ] [ -d debug | --debug=debug ] [ -k kodos_dir ]"
    print
    print "  -f filename | --filename=filename  : Load filename on startup"
    print "  -d debug | --debug=debug           : Set debug to this debug level"
    print "  -k kodos_dir                       : Path containing Kodos images & help subdirs"
    print "  -l locale | --locale=locale        : 2-letter locale (eg. en)"
    print
    sys.exit(0)

def main():
    filename  = None
    debug     = 0
    kodos_dir = os.path.join(sys.prefix, "kodos")
    locale    = None

    args = sys.argv[1:]
    try:
        (opts, getopts) = getopt.getopt(args, 'd:f:k:l:?h',
                                        ["file=", "debug=",
                                         "help", "locale="])
    except:
        print "\nInvalid command line option detected."
        usage()

    for opt, arg in opts:
        if opt in ('-h', '-?', '--help'):
            usage()
        if opt == '-k':
            kodos_dir = arg
        if opt in ('-d', '--debug'):
            try:
                debug = int(arg)
            except:
                print "debug value must be an integer"
                usage()            
        if opt in ('-f', '--file'):
            filename = arg
        if opt in ('-l', '--locale'):
            locale = arg

    os.environ['KODOS_DIR'] = kodos_dir

    MigrateSettings()

    qApp = QApplication(sys.argv)

    if locale not in (None, 'en'):
        localefile = "kodos_%s.qm" % (locale or QTextCodec.locale())
        localepath = findFile(os.path.join("translations", localefile))
        if debug:
            print "locale changed to:", locale
            print localefile
            print localepath
    
        translator = QTranslator(qApp)
        translator.load(localepath)

        qApp.installTranslator(translator)

    kodos = Kodos(filename, debug)

    qApp.setMainWidget(kodos)

    qApp.exec_loop()    



if __name__ == '__main__':
    main()
