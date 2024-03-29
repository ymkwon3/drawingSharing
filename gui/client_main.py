import sys, os, cv2
import numpy as np
from _thread import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datafile import CaptureData
from threading import Thread
from host_windowSelect import WindowSelect
import base64
import client_socket


class ClientMain(QWidget):
    def __init__(self):
        super().__init__()
        self.c = client_socket.ClientSocket(self)
        text, ok = QInputDialog.getText(self, 'ip', 'ip를 입력하세요.')
        if ok:
            self.text = text
        self.initUI()

    def initUI(self):

        self.c.connectServer(self.text, 9999)

        btn_selectwindow = QPushButton('Select Window', self)
        btn_selectwindow.clicked.connect(self.selectWindow)

        btn_sharing = QPushButton('Sharing', self)
        btn_sharing.clicked.connect(self.sendData)

        btn_showing = QPushButton('Showing', self)
        btn_showing.clicked.connect(self.showScreen)

        btnL = QHBoxLayout()
        btnL.addWidget(btn_selectwindow)
        btnL.addWidget(btn_sharing)
        btnL.addWidget(btn_showing)

        self.guest = QTableWidget()
        self.guest.setRowCount(10)
        self.guest.setColumnCount(1)
        self.guest.setHorizontalHeaderItem(0, QTableWidgetItem('ip'))

        rbox = QVBoxLayout()
        rbox.addLayout(btnL)
        rbox.addWidget(self.guest)

        self.setLayout(rbox)

        self.setWindowTitle('show image')
        self.show()

    def sendData(self):
        #if not self.s.bListen:
        #    self.sendmsg.clear()
        #    return
        with open("appimg.png", "rb") as imageFile:
            sendimage = base64.b64encode(imageFile.read())
        senddata = {"file":sendimage, "test":'testdatamm'}
        # sendimage = CaptureData.capturedata
        print(type(sendimage))
        self.c.send(senddata)

    def updateClient(self):
        self.guest.clearContents()
        i = 0
        for ip in self.c.ip:
            self.guest.setItem(i, 0, QTableWidgetItem(ip[0]))
            i += 1

    def closeEvent(self, e):
        self.c.stop()

    def selectWindow(self):
        self.ex = WindowSelect()

    def showScreen(self):
        try:
            img = cv2.imread("appimg.png")
            pixmap = QPixmap("appimg.png")
            if pixmap.size().width() > pixmap.size().height():
                reimg = cv2.resize(img, dsize=(0, 0), fx=0.7, fy=0.7, interpolation=cv2.INTER_LINEAR)
            else:
                reimg = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)
            cv2.imshow("appimg.png", reimg)
        except Exception as e:
            print("왜이리 에러가 뜨는 것이냐 ", e)


# 쓰레드에서 실행되는 코드입니다.

# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴합니다.

# 새로운 쓰레드에서 해당 소켓을 사용하여 통신을 하게 됩니다.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClientMain()
    sys.exit(app.exec_())
