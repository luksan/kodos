# -*- coding: utf-8 -*-
#  about.py: -*- Python -*-  DESCRIPTIVE TEXT.

from PyQt5.QtWidgets import QDialog
from . import aboutBA
from . import version


class About(QDialog, aboutBA.Ui_AboutBA):
    def __init__(self):
        super(About, self).__init__()
        self.setupUi(self)
        self.versionLabel.setText(version.VERSION)

