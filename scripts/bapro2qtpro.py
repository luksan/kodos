#!/bin/env python
import os, sys, re

# regular expressions from Kodos (http://kodos.sourceforge.net)
rx_folder = re.compile(r'''\<folder name="(?P<folder>.*?)" \>
(?P<data>.*?)
 *\</folder\>''', re.DOTALL)

rx_modules = re.compile(r'''name="(?P<module>.*\.py)"''')

rx_translations = re.compile(r'''TRANSLATIONS *= *(?P<files>.*)''')

class Convert:
    def __init__(self, infile, outfile):
        modules = self.getModules(infile)
        translations = self.getTranslations(outfile)
        self.saveQtFile(outfile, modules, translations)


    def getTranslations(self, outfile):
        translations = ""
        try:
            fp = open(outfile, "r")
            data = fp.read()
            fp.close()

            m = rx_translations.search(data)
            if m:
                translations = m.group("files")
        except:
            pass

        return translations


    def getModules(self, infile):
        fp = open(infile, "r")
        data = fp.read()
        fp.close()

        modules = []

        m = rx_folder.search(data)
        if m:
            start = m.start()
        else:
            start = len(data)

        while m:
            folder = m.group("folder")
            moduledata = m.group("data")

            modules += self.__getModules(folder, moduledata)
            pos = m.end()
            m = rx_folder.search(data, pos)

        modules += self.__getModules(None, data, start)
        return modules


    def __getModules(self, folder, moduledata, end=None):
        modules = []
        pos = 0

        while 1:
            if end:
                m = rx_modules.search(moduledata, pos, end)
            else:
                m = rx_modules.search(moduledata, pos)

            if not m: break

            pos = m.end()
            name = m.group("module")

            if folder:
                modules.append( os.path.join(folder, name) )
            else:
                modules.append(name)

        return modules


    def saveQtFile(self, outfile, modules, translations):
        fp = open(outfile, "w")
        fp.write("# This file was produced by a script -- editing is not recommended\n")
        fp.write("SOURCES = ");

        for module in modules:
            fp.write("%s " % module)

        fp.write("\n")
        fp.write("TRANSLATIONS = %s\n" % translations)


##################################################################################

def usage():
    print "Usage: ", sys.argv[0], " ba.pro qt.pro"
    sys.exit(1)

def convert():
    try:
        infile = sys.argv[1]
        outfile = sys.argv[2]

        if infile == outfile:
            print "ba.pro and qt.pro must refer to different filenames\n"
            usage()
    except:
        usage()

    c = Convert(infile, outfile)

##################################################################################

if __name__ == '__main__':
    convert()

