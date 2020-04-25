import sys, time
from host_appWindows import currentApp
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from pywinauto.application import Application

class WindowSelect(QWidget):
    app_dict = currentApp()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        lbtitle = QLabel("current running process list")
        lbtitle.setAlignment(Qt.AlignCenter)
        vbox.addWidget(lbtitle)
        lbborder1 = QLabel("=============================================")
        lbborder1.setAlignment(Qt.AlignCenter)
        vbox.addWidget(lbborder1)

        for i in self.app_dict:
            lb = QLabel('{}' .format(i), self)
            lb.setAlignment(Qt.AlignCenter)
            vbox.addWidget(lb)

        vbox.addStretch()
        lbborder2 = QLabel("=============================================")
        lbborder2.setAlignment(Qt.AlignCenter)
        lbinput = QLabel("write process name what you want")
        lbinput.setAlignment(Qt.AlignCenter)
        vbox.addWidget(lbborder2)
        vbox.addWidget(lbinput)

        self.qle = QLineEdit(self)
        self.qle.editingFinished.connect(self.checkProcess)
        self.qle.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.qle)

        self.setLayout(vbox)
        self.setWindowTitle('Select window')
        self.resize(300, 150)
        self.center()
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def checkProcess(self):
        app = Application().connect(process=self.app_dict[self.qle.text()])
        #잘못입력했을때의 예외처리 필요########################################################################################################
        apptop = app.top_window().set_focus()
        time.sleep(1)
        apptop.CaptureAsImage().save("appimg.png")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowSelect()
    sys.exit(app.exec_())