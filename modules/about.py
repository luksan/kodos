#  about.py: -*- Python -*-  DESCRIPTIVE TEXT.

from qt import *
from aboutBA import *
from util import getPixmap
import version

class About(AboutBA):
    def __init__(self):
        AboutBA.__init__(self)
        self.image0 = getPixmap("kodos.png")
        self.versionLabel.setText(version.VERSION)

