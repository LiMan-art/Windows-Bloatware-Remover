from delete_programm import finish_delete_App
from delete_oneDrive import delete_OneDrive


def one_or_app():

    while True:
        inp = input("[*] Что вы хотите удалить? \n[1] - OneDrive \n[2] - Мусор ОС \n[3] - Выход\n")

        if inp == "1":
            delete_OneDrive()

        elif inp == "2":
            finish_delete_App()
            
        elif inp == "3":
            break
        else:
            print("[*] Некорректный ввод")


if __name__ == "__main__":
    one_or_app()
