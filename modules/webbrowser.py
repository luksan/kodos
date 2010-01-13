#  webbrowser.py: -*- Python -*-  DESCRIPTIVE TEXT.

from os import access, X_OK, spawnv, P_NOWAIT 
from qt import QMessageBox
import sys

def launch_browser(browser, url, caption=None, message=None):
    if not caption: caption = "Info"
    if not message: message = "Launch web browser?"
    
    if not browser or not access(browser, X_OK):
        QMessageBox.warning(None, "Warning", "You must properly configure your web browser path in Preferences (within the Edit menu).")
        return 0


    cancel = QMessageBox.information(None, caption, message, "&Ok", "&Cancel")
    if cancel: return 0

    if sys.platform == 'win32':
        return spawnv(P_NOWAIT, browser, (" ", url))
    else:
        return spawnv(P_NOWAIT, browser, (browser, url))

        
