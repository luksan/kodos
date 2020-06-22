# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

#-----------------------------------------------------------------------------#
# Built-in modules

from __future__ import absolute_import, print_function, unicode_literals

#-----------------------------------------------------------------------------#
# Installed modules

from PyQt4 import QtGui, QtCore

#-----------------------------------------------------------------------------#
# Kodos modules

from .newUserDialogBA import Ui_NewUserDialog

#-----------------------------------------------------------------------------#

class NewUserDialog(QtGui.QDialog, Ui_NewUserDialog):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)

#-----------------------------------------------------------------------------#
