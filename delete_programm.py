from sear_programm import sea_programm

import subprocess

# скрить синию хрень
CREATE_NO_WINDOWS = 0x08000000


def finish_delete_App():
    pr_app, del_app = sea_programm()

    if len(pr_app) != 0:
        print(f"[*] Всего было найдено {len(pr_app)} программ(ы).")

        for i, app in enumerate(pr_app, start=1):
            print(f"{i}. {app}")

        while True:

            inp_user = input("[*] Хотите удалить (Да/Нет)? ").strip().lower()

            if inp_user == "да":

                delete_powershell(del_app)
                break

            elif inp_user == "нет":

                print("[*] Удаление отменено")
                break

            print("[*] Некорректный ввод ")
    else:
        print("[*] Программ для удаления не обнаружено!")


def delete_powershell(del_app):
    for i in range(len(del_app)):

        try:
            subprocess.run(
                [
                    "powershell.exe",
                    "-Command",
                    f"Get-AppxPackage -Name {del_app[i]} | Remove-AppxPackage",
                ],
                capture_output=True,
                text=True,
                creationflags=CREATE_NO_WINDOWS,
            )
            print(f"Программа {del_app[i]} удалена!")
        except NameError as a:
            print(a)
