import os


# Узнаем установлен ли OneDrive
def sear_OneDrive():
    file_oneDrive = [
        r"%LocalAppData%\Microsoft\OneDrive\OneDrive.exe",
        r"%ProgramFiles%\Microsoft OneDrive\OneDrive.exe",
        r"%ProgramFiles(x86)%\Microsoft OneDrive\OneDrive.exe",
    ]

    for i in file_oneDrive:

        dr_oneDrive = os.path.expandvars(i)
        if os.path.isfile(dr_oneDrive):
            print("[*] OneDrive установлен")
            return dr_oneDrive

    print("[*] OneDrive НЕ установлен")
    return None


# Узнаем где лежит ununstall файл
def sear_uninstall_oneDrive():
    dr_oneDrive = sear_OneDrive()
    if dr_oneDrive:
        file_exe = [
            r"C:\Windows\SysWOW64\OneDriveSetup.exe",
            r"C:\Windows\System32\OneDriveSetup.exe",
        ]

        for real_exe in file_exe:
            if os.path.isfile(real_exe):
                print("[*] Uninstall файл найден")
                return real_exe

        print("[*] Uninstall файл НЕ найден")
        return None
