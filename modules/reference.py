#  reference.py: -*- Python -*-  DESCRIPTIVE TEXT.

from qt import *
from referenceBA import *
from util import *
import xpm
#from tooltip import *
#from status_bar import *

GEO = "regex-ref_geometry"

class Reference(ReferenceBA):
    def __init__(self, parent):
        ReferenceBA.__init__(self, None)
        self.parent = parent

        restoreWindowSettings(self, GEO)
        kodos_toolbar_logo(self.toolBar)


    def closeEvent(self, ev):
        saveWindowSettings(self, GEO)
        ev.accept()


    def editPaste(self):
        list_view_item = self.referenceListView.selectedItem()
        if list_view_item == None:
            return
        
        symbol = str(list_view_item.text(0))
        self.parent.emit(PYSIGNAL('pasteSymbol()'), (symbol,))


    def help_slot(self):
        self.parent.helpHelp()

    def help_python_slot(self):
        self.parent.helpPythonRegex()
