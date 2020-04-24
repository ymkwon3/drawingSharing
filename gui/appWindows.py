import os
def currentApp():
    os.system('powershell "gps | where {$_.MainWindowHandle -ne 0 } | select id, name > app.txt')

    line_num = 1
    app_list = []
    f = open("app.txt", 'r', encoding="utf16")
    lines = f.readlines()
    for line in lines:
        if (line_num > 3):
             app_list.append(line[6:].rstrip() + ".exe")
        line_num += 1
    f.close()

    app_list = set(app_list)
    app_list = list(app_list)
    app_list.remove('ApplicationFrameHost.exe')
    app_list.remove('WindowsInternal.ComposableShell.Experiences.TextInput.InputApp.exe')
    app_list.remove('WinStore.App.exe')
    app_list.remove('.exe')

    return app_list