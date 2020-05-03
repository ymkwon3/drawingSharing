import sys, time
from functools import partial
from host_appWindows import currentApp
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from pywinauto.application import Application
from datafile import CaptureData
import win32gui
import win32ui
from ctypes import windll
from PIL import Image

class WindowSelect(QWidget):
    app_dict = currentApp()
    btnList = []
    btnCnt = 0
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

        lbborder2 = QLabel("=============================================")
        lbborder2.setAlignment(Qt.AlignCenter)
        vbox.addWidget(lbborder2)

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
        apptop = app.top_window().set_focus()
        time.sleep(1)
        CaptureData.capturedata = apptop.capture_as_image()
        apptop.minimize()
        self.btnList = []
        self.close()
        # try:
        #
        #     hwnd = win32gui.FindWindow(name, None)
        #     # Change the line below depending on whether you want the whole window
        #     # or just the client area.
        #     #left, top, right, bot = win32gui.GetClientRect(hwnd)
        #
        #     left, top, right, bot = win32gui.GetWindowRect(hwnd)
        #     w = right - left
        #     h = bot - top
        #
        #     hwndDC = win32gui.GetWindowDC(hwnd)
        #     mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        #     saveDC = mfcDC.CreateCompatibleDC()
        #
        #     saveBitMap = win32ui.CreateBitmap()
        #     saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        #
        #     saveDC.SelectObject(saveBitMap)
        #
        #     # Change the line below depending on whether you want the whole window
        #     # or just the client area.
        #     # result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
        #     result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
        #     print(result)
        #
        #     bmpinfo = saveBitMap.GetInfo()
        #     bmpstr = saveBitMap.GetBitmapBits(True)
        #
        #     im = Image.frombuffer(
        #         'RGB',
        #         (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        #         bmpstr, 'raw', 'BGRX', 0, 1)
        #
        #     win32gui.DeleteObject(saveBitMap.GetHandle())
        #     saveDC.DeleteDC()
        #     mfcDC.DeleteDC()
        #     win32gui.ReleaseDC(hwnd, hwndDC)
        #
        #     if result == 1:
        #         # PrintWindow Succeeded
        #         im.save("appimg.png")
        #         CaptureData.capturedata = im
        #
        #     self.close()
        # except Exception as err:
        #     print(err)