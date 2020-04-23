import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        lbl = QLabel(self)
        lbl.setText("접속하실 IP를 입력하세요.")
        lbl.move(5, 5)

        self.qle = QLineEdit(self)
        self.qle.move(5, 25)

        btn1 = QPushButton('&Enter', self)
        btn1.setCheckable(True)
        btn1.move(165, 24)
        btn1.clicked.connect(self.enter)

        self.setWindowTitle('Draw')
        self.resize(250, 50)
        self.center()
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def enter(self):
        print(self.qle.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())