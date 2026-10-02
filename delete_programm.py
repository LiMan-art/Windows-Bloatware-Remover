from sear_programm import sea_programm
#from app import one_or_app
import subprocess

# скрить синию хрень
CREATE_NO_WINDOWS = 0x08000000


def finish_delete_App():

    while True:

        inp_user = input("[*] Хотите удалить (Да/Нет)? ").strip().lower()

        if inp_user == "да":

            delete_powershell()
            break

        elif inp_user == "нет":

            print("[*] Удаление отменено")
            break

        print("[*] Некорректный ввод ")


def delete_powershell():
    delete_app = sea_programm()
    for i in range(len(delete_app)):
        subprocess.run(
            [
                "powershell.exe",
                "-Command",
                f"Get-AppxPackage -Name {delete_app[i]} | Remove-AppxPackage",
            ],
            capture_output=True,
            text=True,
            creationflags=CREATE_NO_WINDOWS,
        )
        print(f"Программа {delete_app[i]} удалена!")
    #one_or_app()
