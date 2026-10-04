import subprocess, os
from onedrive import sear_uninstall_oneDrive

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


def delete_OneDrive():
    real_exe = sear_uninstall_oneDrive()
    if real_exe:
        subprocess.run(
            ["powershell.exe", "-Command", f'& "{real_exe}" /uninstall'],
            creationflags=CREATE_NO_WINDOWS,
        )

        # Убираем эту шляпу из панели навигации в проводнике
        subprocess.run(
            [
                "powershell.exe",
                "-Command",
                r'Remove-Item -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace\{018D5C66-4533-4307-9B53-224DE2ED1FE6}" -Recurse -ErrorAction SilentlyContinue',
            ],
            creationflags=CREATE_NO_WINDOWS,
        )

        print("[*] OneDrive удален")
    else: 
        print("[*] Uninstall файл НЕ найден")
