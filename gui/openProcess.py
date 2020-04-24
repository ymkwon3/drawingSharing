from pywinauto.application import Application

# def openWindow():
app = Application(backend="uia").start("notepad.exe")
# app['Dialog']['Edit'].set_text("Sample")
# app = Application(backend="uia").connect(path="chrome.exe")
# app['Dialog']['Edit'].set_text("")

