import sys, time
from functools import partial
from host_appWindows import currentApp
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from pywinauto.application import Application
from host_main import HostMain
from datafile import CaptureData

class WindowSelect(QWidget):
    app_dict = currentApp()
    btnList = []
    btnCnt = 0
    windowcapture = ""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        lbinput = QLabel("Select process name what you want")
        lbinput.setAlignment(Qt.AlignCenter)
        vbox.addWidget(lbinput)
        lbtitle = QLabel("[ current running process list ]")
        lbtitle.setAlignment(Qt.AlignCenter)
        vbox.addWidget(lbtitle)
        lbborder1 = QLabel("=============================================")
        lbborder1.setAlignment(Qt.AlignCenter)
        vbox.addWidget(lbborder1)

        for i in self.app_dict:
            self.btnList.append(QPushButton(i, self))
            print(self.btnList[self.btnCnt].text())
            self.btnList[self.btnCnt].clicked.connect(partial(self.checkProcess, self.btnList[self.btnCnt].text()))
            vbox.addWidget(self.btnList[self.btnCnt])
            self.btnCnt += 1

        vbox.addStretch()

        lbborder1 = QLabel("=============================================")
        lbborder1.setAlignment(Qt.AlignCenter)
        vbox.addWidget(lbborder1)

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

    def checkProcess(self, name):
        print(name)
        app = Application().connect(process=self.app_dict[name])

        #잘못입력했을때의 예외처리 필요########################################################################################################
        apptop = app.top_window().set_focus()
        time.sleep(1)
        CaptureData.capturedata = apptop.capture_as_image()
        apptop.minimize()

        self.ex = HostMain()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowSelect()
    sys.exit(app.exec_())