#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4; truncate-lines: 0 -*-
# vi: set fileencoding=utf-8 filetype=python expandtab tabstop=4 shiftwidth=4 softtabstop=4 cindent:
# :mode=python:indentSize=4:tabSize=4:noTabs=true:

"""
this should be invoked by a pyuic wrapper
it looks for the arg after the -o cmd line flag
which is used as the source AND destination file.
"""

#-----------------------------------------------------------------------------#
# Built-in modules

import sys
import os
import re

#-----------------------------------------------------------------------------#

filename = None
args = sys.argv[1:]

for i in range(len(args)):
    arg = args[i]
    if arg == '-o':
        filename = args[i+1]
        break

if not filename:
    print("Error: could not extract filename from: {0}".format(args))
    sys.exit(0)

fp = open(filename, "r")
pycode = fp.read()
fp.close()


# regex from Kodos (of course!)
rx = re.compile(r"""self\.clearWState\(Qt\.WState_Polished\)""")
repl = """try:
            self.clearWState(Qt.WState_Polished)
        except AttributeError:
            pass
"""
pycode = rx.sub(repl, pycode)


rx = re.compile(r"""\.setAccel\((?P<tr>.*)""")
pos = 0
while 1:
    m = rx.search(pycode, pos)
    if not m: break
    pos = m.end()
    tr = m.group(1)
    pycode = pycode[:m.start()] + \
             ".setAccel(QKeySequence(" + \
             tr + \
             ")" + \
             pycode[m.end():]


fp = open(filename, "w")
fp.write(pycode)
fp.close()

#-----------------------------------------------------------------------------#
