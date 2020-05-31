from threading import *
from socket import *
from PyQt5.QtCore import Qt, pyqtSignal, QObject
import pickle


class Signal(QObject):
    recv_signal = pyqtSignal(str)

class ClientSocket:

    def __init__(self, parent):
        self.parent = parent

        self.recv = Signal()
        self.recv.recv_signal.connect(self.parent.updateClient)
        self.bConnect = False

    def __del__(self):
        self.stop()

    def connectServer(self, ip, port):
        self.client = socket(AF_INET, SOCK_STREAM)

        try:
            self.client.connect((ip, port))
        except Exception as e:
            print('Connect Error : ', e)
            return False
        else:
            self.bConnect = True
            self.t = Thread(target=self.receive, args=(self.client,))
            self.t.start()
            print('Connected')

        return True

    def stop(self):
        self.bConnect = False
        if hasattr(self, 'client'):
            self.client.close()
            del (self.client)
            print('Client Stop')

    def receive(self, client):
        data = b""
        while self.bConnect:
            packet = client.recv(4096)
            if not packet: break
            data += packet
            print(packet)
        data_arr = pickle.loads(data)
        print(data_arr)

    def send(self, msg):
        if not self.bConnect:
            return

        try:
            dumpfile = pickle.dumps(msg)
            self.client.send(dumpfile)
        except Exception as e:
            print('Send() Error : ', e)