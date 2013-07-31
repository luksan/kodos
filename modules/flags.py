# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

#-----------------------------------------------------------------------------#
# Built-in modules

from __future__ import print_function, absolute_import, unicode_literals

import re

#-----------------------------------------------------------------------------#

class reFlag(object):
    def __init__(self, flag_name, short_flag, checkbox):
        if not flag_name.startswith('re.'):
            raise ValueError('Invalid flag name {!r}'.format(flag_name))

        self.flagName = flag_name
        self.reFlag = getattr(re, flag_name[3:])
        self.shortFlag = short_flag
        self.checkBox = checkbox
        self.preEmbedState = None
        return


    def clear(self):
        self.preEmbedState = None
        self.checkBox.setEnabled(True)
        self.checkBox.setChecked(False)
        return


    def embed(self):
        """Set the state of the checkbox to show that it
           is set by the regexp text."""
        if self.preEmbedState == None:
            self.preEmbedState = self.checkBox.isChecked()
            self.checkBox.setChecked(True)
            self.checkBox.setDisabled(True)
        return


    def deembed(self):
        if self.preEmbedState != None:
            self.checkBox.setEnabled(True)
            self.checkBox.setChecked(self.preEmbedState)
            self.preEmbedState = None
        return


class reFlagList(list):
    def allFlagsORed(self):
        ret = 0
        for f in self:
            if f.checkBox.isChecked():
                ret |= f.reFlag
        return ret


    def clearAll(self):
        for f in self:
            f.clear()
        return

#-----------------------------------------------------------------------------#
