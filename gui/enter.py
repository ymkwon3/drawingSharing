import sys, os
from PyQt5.QtWidgets import *

class Enter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('&Host', self)
        btn1.clicked.connect(self.enterHost)

        btn2 = QPushButton('&Client', self)
        btn2.clicked.connect(self.enterClient)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)
        self.setWindowTitle('Select Enter')
        self.resize(300, 150)
        self.center()
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def enterHost(self):
        self.close()
        os.system("python host_main.py")

    def enterClient(self):
        self.close()
        os.system("python client_inputIP.py")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Enter()
    sys.exit(app.exec_())