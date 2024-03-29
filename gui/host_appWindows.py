import os
def currentApp():
    os.system('powershell "gps | where {$_.MainWindowHandle -ne 0 } | select id, name > app.txt')

    line_num = 1
    tmp = []
    app_dict = {}
    f = open("app.txt", 'r', encoding="utf16")
    lines = f.readlines()
    for line in lines:
        if (line_num > 3):
            line = line.lstrip().rstrip()
            if line != "":
                tmp = line.split(' ')
                app_dict[tmp[1] + ".exe"] = int(tmp[0])
                print(app_dict)
        line_num += 1
    f.close()

    if 'ApplicationFrameHost.exe' in app_dict:
        del app_dict['ApplicationFrameHost.exe']
    if 'WindowsInternal.ComposableShell.Experiences.TextInput.InputApp.exe' in app_dict:
        del app_dict['WindowsInternal.ComposableShell.Experiences.TextInput.InputApp.exe']
    if 'WinStore.App.exe' in app_dict:
        del app_dict['WinStore.App.exe']
    if 'MicrosoftEdge.exe' in app_dict:
        del app_dict['MicrosoftEdge.exe']
    if 'MicrosoftEdgeCP.exe' in app_dict:
        del app_dict['MicrosoftEdgeCP.exe']
    if 'SystemSettings.exe' in app_dict:
        del app_dict['SystemSettings.exe']
    if 'Music.UI.exe' in app_dict:
        del app_dict['Music.UI.exe']
    if 'explorer.exe' in app_dict:
        del app_dict['explorer.exe']

    print(app_dict)
    return app_dict