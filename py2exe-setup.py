#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.version import VERSION
from distutils.core import setup
#from distutils.sysconfig import get_python_lib
import os
import os.path
import sys
from glob import glob
try:
     import py2exe
except:
     pass

args = sys.argv[1:]

if sys.platform == 'win32':
#     libpath = '.\\'
     libpath = r"lib\site-packages\kodos"
else:
     #libpath = "/usr/local/kodos" # 2.4.0 and prior
     libpath = "/usr/share/kodos"  # as of 2.4.1

for arg in args:
    if arg == "--formats=wininst":
        libpath = "kodos"
        break

HELP_DIR = os.path.join(libpath, "help")
HELP_PY_DIR = os.path.join(libpath,  "help", "python")
IMAGES_DIR = os.path.join(libpath, "images")
SCREENSHOTS_DIR = os.path.join(libpath, "screenshots")
MODULES_DIR = os.path.join(libpath, "modules")
TRANSLATIONS_DIR = os.path.join(libpath, "translations")

#########################################################################

setup(name="kodos",
      version=VERSION,
      description="Kodos is a visual regular expression editor",
      author="Phil Schwartz",
      author_email="phil_schwartz@users.sourceforge.net",
      url="http://kodos.sourceforge.net",
      scripts=['kodos.py'],
      windows=[{"script": 'kodos.py',
                "icon_resources": [(1, "images\kodos_icon.ico")]
                }],
      console=[{"script": "kodos.py"}],
      ##package_dir={'': 'modules'},
      packages=['modules', "."],
      data_files=[(HELP_DIR, glob(os.path.join("help", "*.*ml"))),
                  (HELP_PY_DIR, glob(os.path.join("help", "python", "*.html"))),
                  (IMAGES_DIR, glob(os.path.join("images", "*.png"))),
                  (SCREENSHOTS_DIR, glob(os.path.join("screenshots", "*.png"))),
                  (TRANSLATIONS_DIR, glob(os.path.join("translations", "*"))),
                  (MODULES_DIR, glob("modules/*.ui"))
                  ],
      license="GPL",
      extra_path='kodos',
      long_description="""
      Kodos is a visual regular expression editor and debugger.
      """
      )

