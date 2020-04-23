import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QLabel, QInputDialog, QPushButton, QVBoxLayout


class MyApp(QWidget):
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

        self.setLayout(vbox)
        self.setWindowTitle('Select Enter ')
        self.resize(300, 300)
        self.center()
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def enterHost(self):
        print(self.qle.text())

    def enterClient(self):
        print(self.qle.text())

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())