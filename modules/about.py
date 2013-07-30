# -*- coding: utf-8 -*-
#  about.py: -*- Python -*-  DESCRIPTIVE TEXT.

from . import aboutBA
from . import version

class About(aboutBA.AboutBA):
    def __init__(self):
        aboutBA.AboutBA.__init__(self)
        self.versionLabel.setText(version.VERSION)
        return

