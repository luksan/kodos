# Form implementation generated from reading ui file '/www/kodos/modules/quickhelperBA.ui'
#
# Created: Fri Jan 11 13:40:02 2002
#      by: The Python User Interface Compiler (pyuic)
#
# WARNING! All changes made in this file will be lost!


from qt import *


class referenceBA(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if name == None:
            self.setName('referenceBA')

        self.resize(535,450)
        self.setCaption(self.tr('Form2'))

        self.ListView2 = QListView(self,'ListView2')
        self.ListView2.addColumn(self.tr('Symbol'))
        self.ListView2.addColumn(self.tr('Definition'))
        item = QListViewItem(self.ListView2,None)
        item.setText(0,self.tr('.'))
        item.setText(1,self.tr('Matches any character'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('*'))
        item.setText(1,self.tr('Matches 0 or more repetition of preceeding RE'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('+'))
        item.setText(1,self.tr('Matches 1 or more repetition of preceeding RE'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('?'))
        item.setText(1,self.tr('Matches 0 or 1 repetition of preceeding RE'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('^'))
        item.setText(1,self.tr('Matches start of string'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('$'))
        item.setText(1,self.tr('Matches the end of the string'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\A'))
        item.setText(1,self.tr('Matches only at the start of the string'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\B'))
        item.setText(1,self.tr('Matches the empty string, but only when it is not at the beginning or end of a  word'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\b'))
        item.setText(1,self.tr('Matches the empty string, but only at the beginning or end of a word'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\d'))
        item.setText(1,self.tr('Matches any decimal digit'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\D'))
        item.setText(1,self.tr('Matches any non-digit character'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\z'))
        item.setText(1,self.tr('Matches only at the end of the string'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\W'))
        item.setText(1,self.tr('Matches any non-word'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\w'))
        item.setText(1,self.tr('Matches any word'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\S'))
        item.setText(1,self.tr('Matches any non-whitespace character'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\s'))
        item.setText(1,self.tr('Matches any whitespace character'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('\\\\'))
        item.setText(1,self.tr('Matches a literal backslash'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('??'))
        item.setText(1,self.tr('Non-greedy ?'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('*?'))
        item.setText(1,self.tr('Non-greedy *'))

        item = QListViewItem(self.ListView2,item)
        item.setText(0,self.tr('+?'))
        item.setText(1,self.tr('Non-greedy +'))

        self.ListView2.setGeometry(QRect(5,30,525,410))
        self.ListView2.setAllColumnsShowFocus(1)
