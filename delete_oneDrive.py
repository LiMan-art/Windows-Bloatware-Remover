import subprocess, os
#from app import one_or_app


# Скрыть хрень
CREATE_NO_WINDOWS = 0x08000000


def stop_OneDrive():
    # Останавливаем процесс
    subprocess.run(
        [
            "powershell.exe",
            "-Command",
            'Stop-Process -Name "OneDrive.Sync.Service" -Force',
        ],
        capture_output=True,
        text=True,
        creationflags=CREATE_NO_WINDOWS,
    )


def sear_uninstall_oneDrive():

    file_exe = [
        r"C:\Windows\SysWOW64\OneDriveSetup.exe",
        r"C:\Windows\System32\OneDriveSetup.exe",
    ]

    for real_exe in file_exe:
        if os.path.isfile(real_exe):
            return real_exe
    return None


def delete_OneDrive(real_exe):
    subprocess.run(
        ["powershell.exe", "-Command", f'& "{real_exe}" /uninstall'],
        creationflags=CREATE_NO_WINDOWS,
    )

    # = Убираем эту шляпу из панели навигации в проводнике
    subprocess.run(
        [
            "powershell.exe",
            "-Command",
            r'Remove-Item -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace\{018D5C66-4533-4307-9B53-224DE2ED1FE6}" -Recurse -ErrorAction SilentlyContinue',
        ],
        creationflags=CREATE_NO_WINDOWS,
    )

    subprocess.run(
        ["powershell.exe", "-Command", "Stop-Process -Name explorer -Force"],
        creationflags=CREATE_NO_WINDOWS,
    )

    print("[*] OneDrive удален")


def finish():
    stop_OneDrive()

    path_to_exe = sear_uninstall_oneDrive()

    if path_to_exe:
        delete_OneDrive(path_to_exe)
    #one_or_app()
