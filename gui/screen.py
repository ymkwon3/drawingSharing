import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.imgscreen = QLabel(self)
        if True:
            pixmap = QPixmap("appimg.png")
            if pixmap.size().width() > pixmap.size().height():
                pixmap = pixmap.scaledToWidth(1600)
            else:
                pixmap = pixmap.scaledToHeight(900)
            self.imgscreen.setPixmap(pixmap)
        else:
            self.imgscreen.setStyleSheet("background-color: green")
            self.imgscreen.setText("ready")

        self.imgscreen.resize(1600, 900)

        lbox = QVBoxLayout()
        lbox.addWidget(self.imgscreen)#, laignment=Qt.AlignCenter)

        self.userlist = QLabel(self)
        self.userlist.setText("hello")
        self.userlist.setStyleSheet("background-color: yellow")
        self.userlist.resize(500, 500)

        rbox = QHBoxLayout()
        rbox.addWidget(self.userlist)


        mainlayout = QHBoxLayout()
        mainlayout.addLayout(lbox)
        mainlayout.addLayout(rbox)
        mainlayout.setStretchFactor(lbox, 4)
        mainlayout.setStretchFactor(rbox, 1)

        self.setLayout(mainlayout)

        self.setWindowTitle('show image')
        self.showMaximized()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Screen()
    sys.exit(app.exec_())