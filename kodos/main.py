# -*- coding: utf-8 -*-

import re
import types
import signal
import string
import urllib
import cPickle

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from kodosBA import *
from util import *
from about import *
from . import help
from status_bar import *
from reference import *
from prefs import *
from version import VERSION
from recent_files import RecentFiles
from urlDialog import URLDialog
from regexLibrary import RegexLibrary
from newUserDialogBA import NewUserDialog
from flags import reFlag, reFlagList

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
        self.regex_embedded_flags_removed = ""

        self.createStatusBar()

        self.MSG_NA     = self.tr("Enter a regular expression and a string to match against")
        self.MSG_PAUSED = self.tr("Kodos regex processing is paused.  Click the pause icon to unpause")
        self.MSG_FAIL   = self.tr("Pattern does not match")


        self.statusPixmapsDict = {  MATCH_NA: QPixmap(":images/yellow.png"),
                                    MATCH_OK: QPixmap(":images/green.png"),
                                    MATCH_FAIL: QPixmap(":images/red.png"),
                                    MATCH_PAUSED: QPixmap(":images/pause.png"),
                                }


        self.updateStatus(self.MSG_NA, MATCH_NA)

        self.reFlags = reFlagList([
                    reFlag("re.IGNORECASE", "i", self.ignorecaseCheckBox),
                    reFlag("re.MULTILINE",  "m", self.multilineCheckBox),
                    reFlag("re.DOTALL",     "s", self.dotallCheckBox),
                    reFlag("re.VERBOSE",    "x", self.verboseCheckBox),
                    reFlag("re.LOCALE",     "L", self.localeCheckBox),
                    reFlag("re.UNICODE",    "u", self.unicodeCheckBox),
                    ])
        self.reFlags.clearAll()

        restoreWindowSettings(self, GEO)

        self.show()

        self.prefs = Preferences(self, 1)
        self.recent_files = RecentFiles(self,
                                        self.prefs.recentFilesSpinBox.value(),
                                        self.debug)

        if filename and self.openFile(filename):
            qApp.processEvents()

        self.fileMenu.triggered.connect(self.fileMenuHandler)

        kodos_toolbar_logo(self.toolBar)
        if self.replace:  self.show_replace_widgets()
        else:             self.hide_replace_widgets()

        self.checkIfNewUser()


    def checkIfNewUser(self):
        s = QSettings()
        if s.value('New User', "true").toPyObject() != "false":
            self.newuserdialog = NewUserDialog()
            self.newuserdialog.show()
        s.setValue('New User', "false")


    def createStatusBar(self):
        self.status_bar = Status_Bar(self, FALSE, "")


    def updateStatus(self, status_string, status_value, duration=0, replace=FALSE, tooltip=''):
        pixmap = self.statusPixmapsDict.get(status_value)

        self.status_bar.set_message(status_string, duration, replace, tooltip, pixmap)


    def fileMenuHandler(self, menuid):
        if self.recent_files.isRecentFile(menuid):
            fn = str(menuid.text())
            if self.openFile(fn):
                self.recent_files.add(fn)

    def prefsSaved(self):
        if self.debug: print "prefsSaved slot"
        self.recent_files.setNumShown(self.prefs.recentFilesSpinBox.value())


    def kodos_edited_slot(self):
        # invoked whenever the user has edited something
        self.editstate = STATE_EDITED


    def checkbox_slot(self):
        self.process_regex()


    def set_flags(self, flags):
        # from the given integer value of flags, set the checkboxes
        # this is used when loading a saved file
        for f in self.reFlags:
            f.checkBox.setChecked(flags & f.reFlag)


    def get_flags_string(self):
        flags_str = ""

        for f in self.reFlags:
            if f.checkBox.isChecked():
                flags_str += "| " + f.flagName

        if flags_str:
            flags_str = ", " + flags_str[1:]
        return flags_str


    def get_embedded_flags_string(self):
        flags_str = flags = ""

        for f in self.reFlags:
            if f.checkBox.isChecked():
                flags += f.shortFlag

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
            self.regexMultiLineEdit.setReadOnly(1)
            self.stringMultiLineEdit.setReadOnly(1)
            self.replaceTextEdit.setReadOnly(1)
            for i in range(length, 0,  -1):
                regex = regex[:i]
                self.process_embedded_flags(self.regex)
                try:
                    m = re.search(regex, self.matchstring, self.reFlags.allFlagsORed())
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
        pal = QPalette()
        pal.setColor(pal.Base, base_qcolor)
        self.regexMultiLineEdit.setPalette(pal)

        self.regexMultiLineEdit.blockSignals(1)
        self.regexMultiLineEdit.clear()
        self.regexMultiLineEdit.blockSignals(0)
        self.regexMultiLineEdit.setPlainText(regex)


    def match_num_slot(self, num):
        self.match_num = num
        self.process_regex()


    def replace_num_slot(self, num):
        self.replace_num = num
        self.process_regex()


    def regex_changed_slot(self):
        self.regex = unicode(self.regexMultiLineEdit.toPlainText())
        self.process_regex()


    def string_changed_slot(self):
        self.matchstring = unicode(self.stringMultiLineEdit.toPlainText())
        self.process_regex()

    def helpContents(self, x = None):
        pass #FIXME
    def helpIndex(self, x = None):
        pass #FIXME

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
        self.replace = unicode(self.replaceTextEdit.toPlainText())
        self.process_regex()
        if not self.replace:
            self.hide_replace_widgets()
        else:
            self.show_replace_widgets()


    def update_results(self, msg, val):
        self.updateStatus(msg, val)


    def populate_group_table(self, tuples):
        rows = len(tuples)
        # Remove old rows for groups that no longer exist
        for i in range(rows, self.groupTable.rowCount()):
            self.groupTable.removeRow(i)

        self.groupTable.setRowCount(rows)
        row = 0
        for t in tuples:
            self.groupTable.setItem(row, 0, QTableWidgetItem(t[1]))
            self.groupTable.setItem(row, 1, QTableWidgetItem(t[2]))
            row += 1


    def populate_code_textbrowser(self):
        self.codeTextBrowser.clear()

        code =  "import re\n\n"
        code += "# common variables\n\n"
        code += "rawstr = r\"\"\"" + self.regex_embedded_flags_removed + "\"\"\"\n"
        code += "embedded_rawstr = r\"\"\"" + self.get_embedded_flags_string() + \
                self.regex_embedded_flags_removed + "\"\"\"\n"
        code += 'matchstr = \"\"\"' + self.matchstring + '\"\"\"'
        code += "\n\n"
        code += "# method 1: using a compile object\n"
        code += "compile_obj = re.compile(rawstr"
        code += self.get_flags_string()
        code += ")\n"
        code += "match_obj = compile_obj.search(matchstr)\n\n"

        code += "# method 2: using search function (w/ external flags)\n"
        code += "match_obj = re.search(rawstr, matchstr"
        code += self.get_flags_string()
        code += ")\n\n"

        code += "# method 3: using search function (w/ embedded flags)\n"
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

        self.codeTextBrowser.setPlainText(code)


    def colorize_strings(self, strings, widget, cursorOffset=0):
        widget.clear()

        colors = (QBrush(QColor(Qt.black)), QBrush(QColor(Qt.blue)) )
        cur = widget.textCursor()
        format = cur.charFormat()

        pos = cur.position()
        i = 0
        for s in strings:
            format.setForeground(colors[i%2])
            cur.insertText(s, format)
            if i == cursorOffset:
                pos = cur.position()
            i += 1

        cur.setPosition(pos)
        widget.setTextCursor(cur)
        widget.centerCursor()


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

        replace_text = unicode(self.replaceTextEdit.toPlainText())
        if RX_BACKREF.search(replace_text):
            # if the replace string contains a backref we just use the
            # python regex methods for the substitution
            replaced = compile_obj.subn(replace_text, text, num)[0]
            self.replaceTextBrowser.setPlainText(replaced)
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
        # .clear() destroys the headers, and .clearContents() doesn't do
        # anything at all, so remove the rows one by one
        for i in range(self.groupTable.rowCount()):
            self.groupTable.removeRow(i)

        self.codeTextBrowser.clear()
        self.matchTextBrowser.clear()
        self.matchNumberSpinBox.setEnabled(FALSE)
        self.replaceNumberSpinBox.setEnabled(FALSE)
        self.replaceTextBrowser.clear()
        self.matchAllTextBrowser.clear()


    def process_regex(self):
        def timeout(signum, frame):
            return

        if self.is_paused:
            return

        self.process_embedded_flags(self.regex)

        if not self.regex or not self.matchstring:
            self.update_results(self.MSG_NA, MATCH_NA)
            self.clear_results()
            return

        if HAS_ALARM:
            signal.signal(signal.SIGALRM, timeout)
            signal.alarm(TIMEOUT)

        try:
            compile_obj = re.compile(self.regex, self.reFlags.allFlagsORed())
            allmatches = compile_obj.findall(self.matchstring)

            if allmatches and len(allmatches):
                self.matchNumberSpinBox.setMaximum(len(allmatches))
                self.matchNumberSpinBox.setEnabled(TRUE)
                self.replaceNumberSpinBox.setMaximum(len(allmatches))
                self.replaceNumberSpinBox.setEnabled(TRUE)
            else:
                self.matchNumberSpinBox.setEnabled(FALSE)
                self.replaceNumberSpinBox.setEnabled(FALSE)

            match_obj = compile_obj.search(self.matchstring)

        except Exception, e:
            self.update_results(unicode(e), MATCH_FAIL)
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

            self.populate_group_table(self.group_tuples)
        else:
            # clear the group table
            self.populate_group_table([])

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
                                        str_matches)

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
        if not self.checkEditState():
            ev.ignore()
            return

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
        if not self.checkEditState():
            return
        self.filename = ""

        self.regexMultiLineEdit.setPlainText("")
        self.stringMultiLineEdit.setPlainText("")
        self.replaceTextEdit.setPlainText("")
        self.set_flags(0)
        self.editstate = STATE_UNEDITED


    def importURL(self):
        self.urldialog = URLDialog(self, self.url)
        self.urldialog.urlImported.connect(self.urlImported)


    def urlImported(self, html, url):
        self.url = url
        self.stringMultiLineEdit.setPlainText(html)


    def importFile(self):
        fn = QFileDialog.getOpenFileName(self,
                                         self.tr("Import File"),
                                         self.filename,
                                         self.tr("All (*)"))

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
        self.stringMultiLineEdit.setPlainText(data)


    def fileOpen(self):
        filename = self.filename
        if filename == None:
            filename = ""
        fn = QFileDialog.getOpenFileName(self,
                                         self.tr("Open Kodos File"),
                                         filename,
                                         self.tr("Kodos file (*.kds);;All (*)"))
        if not fn.isEmpty():
            filename = str(fn)
            if self.openFile(filename):
                self.recent_files.add(filename)


    def openFile(self, filename):
        if not self.checkEditState():
            return

        self.filename = None

        try:
            fp = open(filename, "r")
        except:
            msg = self.tr("Could not open file for reading: ") + filename
            self.updateStatus(msg, -1, 5, TRUE)
            return None

        try:
            u = cPickle.Unpickler(fp)
            self.regex = u.load()
            self.matchstring = u.load()
            flags = u.load()
        except Exception, e: #FIXME: don't catch everything
            if self.debug:
                print unicode(e)
            msg = "%s %s" % (unicode(self.tr("Error reading from file:")),
                             filename)
            self.updateStatus(msg, -1, 5, TRUE)
            return 0

        self.matchNumberSpinBox.setValue(1)
        self.regexMultiLineEdit.setPlainText(self.regex)
        self.stringMultiLineEdit.setPlainText(self.matchstring)

        self.set_flags(flags)

        try:
            replace = u.load()
        except:
            # versions prior to 1.7 did not have replace functionality
            # so kds files saved w/ these versions will throw exception
            # here.
            replace = ""
        self.replaceTextEdit.setPlainText(replace)

        self.filename = filename
        msg = "%s %s" % (filename, unicode(self.tr("loaded successfully")))
        self.updateStatus(msg, -1, 5, TRUE)
        self.editstate = STATE_UNEDITED
        return 1


    def fileSaveAs(self):
        filename = self.filename
        if filename == None:
            filename = ""
        filedialog = QFileDialog(self,
                                 self.tr("Save Kodos File"),
                                 filename,
                                 "Kodos file (*.kds);;All (*)")
        filedialog.setAcceptMode(QFileDialog.AcceptSave)
        filedialog.setDefaultSuffix("kds")
        ok = filedialog.exec_()

        if ok == QDialog.Rejected:
            self.updateStatus(self.tr("No file selected to save"), -1, 5, TRUE)
            return

        filename = os.path.normcase(unicode(filedialog.selectedFiles().first()))

        self.filename = filename
        self.fileSave()


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
        p.dump(self.reFlags.allFlagsORed())
        p.dump(self.replace)

        fp.close()
        msg = "%s %s" % (unicode(self.filename),
                         unicode(self.tr("successfully saved")))
        self.updateStatus(msg, -1, 5, TRUE)
        self.recent_files.add(self.filename)


    def paste_symbol(self, symbol):
        self.regexMultiLineEdit.insertPlainText(symbol)


    def process_embedded_flags(self, regex):
        # determine if the regex contains embedded regex flags.
        # if it does, set the appropriate checkboxes on the UI to reflect the flags that are embedded
        match = self.embedded_flags_obj.match(regex)
        if not match:
            embedded_flags = ""
            self.regex_embedded_flags_removed = regex
        else:
            embedded_flags = match.group('flags')
            self.regex_embedded_flags_removed = self.embedded_flags_obj.sub("", regex, 1)

        for f in self.reFlags:
            if f.shortFlag in embedded_flags:
                f.embed()
            else:
                f.deembed()


    def checkEditState(self):
        if self.editstate == STATE_EDITED:
            message = self.tr("You have made changes. Would you like to save them before continuing?")

            prompt = QMessageBox.warning(None,
                                         self.tr("Save changes?"),
                                         message,
                                         QMessageBox.Save |
                                         QMessageBox.Cancel |
                                         QMessageBox.Discard)

            if prompt == QMessageBox.Cancel:
                return False

            if prompt == QMessageBox.Save:
                self.fileSave()
                if not self.filename: self.checkEditState()

        return True


    def pasteFromRegexLib(self, d):
        if not self.checkEditState():
            return

        self.filename = ""

        self.regexMultiLineEdit.setPlainText(d.get('regex', ""))
        self.stringMultiLineEdit.setPlainText(d.get('text', ""))
        self.replaceTextEdit.setPlainText(d.get('replace', ""))

        try:
            # set the current page if applicable
            self.resultTabWidget.setCurrentIndex(int(d['tab']))
        except KeyError:
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
        self.prefs.prefsSaved.connect(self.prefsSaved)

    def setfont(self, font):
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
        self.helpWindow = help.Help(self, os.path.join("python", "module-re.html"))


    def helpRegexLib(self):
        f = os.path.join("help", "regex-lib.xml")
        self.regexlibwin = RegexLibrary(f)
        self.regexlibwin.pasteRegexLib.connect(self.pasteFromRegexLib)
        self.regexlibwin.show()


    def helpAbout(self):
        self.aboutWindow = About()
        self.aboutWindow.show()


    def kodos_website(self):
        self.launch_browser_wrapper('https://github.com/luksan/kodos',
                                    message=self.tr('Launch web browser to go to the kodos project page?'))


    def launch_browser_wrapper(self, url, caption=None, message=None):
        if launch_browser(url, caption, message):
            self.status_bar.set_message(self.tr("Launching web browser"),
                                        3,
                                        TRUE)
        else:
            self.status_bar.set_message(self.tr("Cancelled web browser launch"),
                                        3,
                                        TRUE)


    def reference_guide(self):
        self.ref_win = Reference(self)
        self.ref_win.pasteSymbol.connect(self.paste_symbol)
        self.ref_win.show()


    def report_bug(self):
        self.launch_browser_wrapper('https://github.com/luksan/kodos/issues',
                                    message=self.tr("Launch web browser to report a bug in kodos?"))
