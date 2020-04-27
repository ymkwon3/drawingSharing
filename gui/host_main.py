import socket, sys
from _thread import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datafile import CaptureData
import PIL

class HostMain(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.imgscreen = QLabel(self)
        if CaptureData.capturedata is not None:
            CaptureData.capturedata.save("appimg.png")
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
        lbox.addWidget(self.imgscreen, alignment=Qt.AlignCenter)

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

        while True:
            print('wait')

            client_socket, addr = server_socket.accept()
            start_new_thread(threaded, (client_socket, addr))

        server_socket.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HostMain()
    sys.exit(app.exec_())

# 쓰레드에서 실행되는 코드입니다.

# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다.
def threaded(client_socket, addr):
    print('Connected by :', addr[0], ':', addr[1])

    # 클라이언트가 접속을 끊을 때 까지 반복합니다.
    while True:

        try:

            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = CaptureData.capturedata
            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1])
                break

            print('Received from ' + addr[0], ':', addr[1])

            client_socket.send(data)

        except ConnectionResetError as e:

            print('Disconnected by ' + addr[0], ':', addr[1])
            break

    client_socket.close()


HOST = '172.30.1.54'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('server start')

# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴합니다.

# 새로운 쓰레드에서 해당 소켓을 사용하여 통신을 하게 됩니다.

