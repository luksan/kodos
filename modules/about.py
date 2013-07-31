# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

#-----------------------------------------------------------------------------#
# Kodos modules

from . import aboutBA
from . import version

#-----------------------------------------------------------------------------#

class About(aboutBA.AboutBA):
    def __init__(self):
        aboutBA.AboutBA.__init__(self)
        self.versionLabel.setText(version.VERSION)
        return

#-----------------------------------------------------------------------------#
