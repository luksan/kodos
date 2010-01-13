#  status_bar.py: -*- Python -*-  DESCRIPTIVE TEXT.

from tooltip import *

class Status_Bar:
    def __init__(self, parent, progress_bar=FALSE, message=''):
        self.parent = parent

        self.statusBar = parent.statusBar()
        self.__statusTimer = QTimer(self.parent)

        self.parent.connect(self.__statusTimer, SIGNAL("timeout()"), self.reset_message)
        
        self.__statusLabel = QLabel(self.statusBar, "msg")
        self.tooltip = Tooltip('')
        self.tooltip.addWidget(self.__statusLabel)
        
        self.last_status_message = ''

        pixmap = getPixmap("yellow.png", "PNG")

        self.pixmapLabel = QLabel("image", self.statusBar)
        self.pixmapLabel.setPixmap(pixmap)
        
        self.statusBar.addWidget(self.pixmapLabel, 0, TRUE)
        self.statusBar.addWidget(self.__statusLabel, 1, TRUE)
        if progress_bar:
            self.progressBar = QProgressBar(self.statusBar)
            self.statusBar.addWidget(self.progressBar, 1, TRUE)

        if message:
            self.set_message(message)
    

    def set_message(self, message='', duration=0, replace=FALSE, tooltip='', pixmap=''):
        """sets the status bar message label to message.

        if duration is > 0 than the message is displayed for duration seconds.

        if duration is > 0 and replace is true then after duration seconds
        have elapsed, the previous message is displayed. 
        """

        self.__statusTimer.stop()
        self.last_status_message = unicode(self.__statusLabel.text())
        self.replace_status_message = replace

        self.__statusLabel.setText(message)

        if duration > 0:
            self.__statusTimer.start(1000 * duration, TRUE)

        if tooltip:
            self.tooltip.set_tooltip(tooltip)
        else:
            self.tooltip.clear_tooltip()

        if pixmap:
            self.pixmapLabel.setPixmap(pixmap)
        

    
    def reset_message(self):
        self.__statusTimer.stop()
        if self.replace_status_message:
            self.__statusLabel.setText(self.last_status_message)
        else:
            self.__statusLabel.setText('')



    def geometry(self):
        return self.statusBar.geometry()
