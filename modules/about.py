# -*- coding: utf-8 -*-
#  about.py: -*- Python -*-  DESCRIPTIVE TEXT.

from aboutBA import *
import version

class About(AboutBA):
    def __init__(self):
        AboutBA.__init__(self)
        self.versionLabel.setText(version.VERSION)

