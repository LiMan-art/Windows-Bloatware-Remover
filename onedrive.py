import os
from delete_oneDrive import finish


def sear_OneDrive():
    file_oneDrive = [
        r"%LocalAppData%\Microsoft\OneDrive\OneDrive.exe",
        r"%ProgramFiles%\Microsoft OneDrive\OneDrive.exe",
        r"%ProgramFiles(x86)%\Microsoft OneDrive\OneDrive.exe",
    ]

    for i in file_oneDrive:

        a = os.path.expandvars(i)
        if os.path.isfile(a):

            return a

    return None


def finish_delete_OneDrive():

    path_to_exe = sear_OneDrive()

    if path_to_exe:
        print("[*] OneDrive установлен \nНачинаю удаление...")
        finish()
    else:
        print("[*] OneDrive не найден")
