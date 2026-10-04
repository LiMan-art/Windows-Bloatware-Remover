from sear_programm import sea_programm

import subprocess

# скрить синию хрень
CREATE_NO_WINDOWS = 0x08000000


pr_app, del_app = sea_programm()


def finish_delete_App():
    print(f"[*] Всего было найдено {len(pr_app)} программ(ы).")

    for i, app in enumerate(pr_app, start=1):
        print(f"{i}. {app}")

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
