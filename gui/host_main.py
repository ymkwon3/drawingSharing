import sys
import cv2
import numpy as np
from _thread import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datafile import CaptureData
from threading import Thread
from host_windowSelect import WindowSelect
import host_server
import base64


class HostMain(QWidget):
    def __init__(self):
        super().__init__()
        self.s = host_server.ServerSocket(self)
        self.s.start() # 서버실행
        self.initUI()

    def initUI(self):
        self.imgscreen = QLabel(self)
        self.imgscreen.setStyleSheet("background-color: green")
        self.imgscreen.setText("ready")
        self.imgscreen.resize(1600, 900)

        lbox = QVBoxLayout()
        lbox.addWidget(self.imgscreen, alignment=Qt.AlignCenter)

        btn_selectwindow = QPushButton('Select Window', self)
        btn_selectwindow.clicked.connect(self.selectWindow)

        btn_sharing = QPushButton('Sharing', self)
        btn_sharing.clicked.connect(self.sendData)

        btnL = QHBoxLayout()
        btnL.addWidget(btn_selectwindow)
        btnL.addWidget(btn_sharing)

        self.guest = QTableWidget()
        self.guest.setRowCount(10)
        self.guest.setColumnCount(1)
        self.guest.setHorizontalHeaderItem(0, QTableWidgetItem('ip'))
        # self.userlist = QLabel(self)
        # self.userlist.setText("hello")
        # self.userlist.setStyleSheet("background-color: yellow")
        # self.userlist.resize(500, 500)


        rbox = QVBoxLayout()
        rbox.addLayout(btnL)
        rbox.addWidget(self.guest)

        mainlayout = QHBoxLayout()
        mainlayout.addLayout(lbox)
        mainlayout.addLayout(rbox)
        mainlayout.setStretchFactor(lbox, 4)
        mainlayout.setStretchFactor(rbox, 1)

        self.setLayout(mainlayout)

        self.setWindowTitle('show image')
        self.showMaximized()

    def sendData(self):
        if not self.s.bListen:
            self.sendmsg.clear()
            return
        CaptureData.capturedata.save("appimg.png")
        img = cv2.imread("appimg.png")


        pixmap = QPixmap("appimg.png")
        # with open("appimg.png", "rb") as imageFile:
        #     sendimage = base64.b64encode(imageFile.read())

        sendimage = CaptureData.capturedata
        print(type(sendimage))
        senddata = {"file":str(sendimage), "test":'testdatamm'}
        ####
        if pixmap.size().width() > pixmap.size().height():
            reimg = cv2.resize(img, dsize=(0, 0), fx=0.7, fy=0.7, interpolation=cv2.INTER_LINEAR)
            pixmap = pixmap.scaledToWidth(1600)
        else:
            reimg = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)
            pixmap = pixmap.scaledToHeight(900)
        cv2.imshow("appimg.png", reimg)
        self.imgscreen.setPixmap(pixmap)
        ####
        try:
            self.s.send(senddata)
            print(senddata)
        except Exception as e:
            print("여기좀봐줘요", e)

    def updateClient(self):
        self.guest.clearContents()
        i = 0
        for ip in self.s.ip:
            self.guest.setItem(i, 0, QTableWidgetItem(ip[0]))
            i += 1

    def closeEvent(self, e):
        self.s.stop()

    def selectWindow(self):
        self.ex = WindowSelect()

# 쓰레드에서 실행되는 코드입니다.

# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴합니다.

# 새로운 쓰레드에서 해당 소켓을 사용하여 통신을 하게 됩니다.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HostMain()
    sys.exit(app.exec_())
