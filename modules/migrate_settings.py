
import os
import os.path
import sys
from util import *
from stat import *
from shutil import copytree

OLD_SETTINGS = getHomeDirectory() + os.sep + ".kodos"
TMP_SETTINGS = OLD_SETTINGS + "1"
NEW_SETTINGS = OLD_SETTINGS + os.sep + "prefs"

class MigrateSettings1:
    def __init__(self):
        if os.path.exists(OLD_SETTINGS):
            stat = os.stat(OLD_SETTINGS)
            mode = stat[ST_MODE]
            if S_ISDIR(mode):
                # settings have already been migrated
                return

        self.migrate_settings()

    def migrate_settings(self):
        print "Migrating Kodos preferences..."

        # move current settings
        try:
            os.rename(OLD_SETTINGS, TMP_SETTINGS)
        except:
            print "Couldn't rename %s to %s" % (OLD_SETTINGS, TMP_SETTINGS)

        # mkdir settings subdir
        try:
            os.mkdir(OLD_SETTINGS, 0750)
        except:
            print "Couldn't create dir %s" % OLD_SETTINGS
                 
        # move tmp settings to subir
        try:
            os.rename(TMP_SETTINGS, NEW_SETTINGS)
        except:
            print "Couldn't rename %s to %s" % (TMP_SETTINGS, NEW_SETTINGS)
            
        print "...Done migrating Kodos preferences"


class MigrateSettings:
    def __init__(self):
        # Kodos 2.1 -> .kodos dir moved from \ to environ HOMEDRIVE\HOMEDIR
        # on win32
        if sys.platform != 'win32': return

        oldkodosdir = os.path.join("\\", ".kodos")
        newkodosdir = os.path.join(getHomeDirectory(), ".kodos")

        if oldkodosdir == newkodosdir: return
        
        try:
            copytree(oldkodosdir, newkodosdir)
        except Exception, e:
            pass
        
