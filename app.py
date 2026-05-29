import subprocess
import win32process
from pathlib import Path


# скрить синию хрень
CREATE_NO_WINDOWS = 0x08000000


def output_mess():

    print('Проверка на PoserShell!')
    # ==== ПРОВЕРКА УСТАНОВЛЕН ЛИ POWERSHELL ====
    try:
        subprocess.run(['powershell.exe','-Command','exit'],creationflags=CREATE_NO_WINDOWS)
        print('PowerShell установлен!')
    except FileNotFoundError:
        input('Powershell не установлен. Ничего не получится, делай все руками! \nДля вохода нажмите Enter')
        exit(1)

    # ==== ВВОИМ КОМАНДУ ДЛЯ ПОЛУЧЕНИЯ РУЗУЛЬТАТА УСТАНОВЛЕН ЛИ ONEDRIVE ИЛИ НЕТ =====
    print('Проверка на установленый OneDrive!')
    
    result_oneDrive = subprocess.run(['powershell.exe', '-Command', r'[bool](Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall* | Where { $_.DisplayName -like "OneDrive*"})'], capture_output=True,text=True,creationflags=CREATE_NO_WINDOWS)

    output_result_oneDrive = result_oneDrive.stdout
    result_install_oneDrive = output_result_oneDrive.splitlines()

    # ==== ЕСЛИ ONEDRIVE УСТАНОВЛЕН ТО УДАЛЯЕМ ====
    if 'False' in result_install_oneDrive:
        print('OneDrive не установлен!')
    else:
        print('OneDrive установлен!')

        # ОСТАНАВЛИВАЕМ ПРОЦЕСС 
        subprocess.run(['powershell.exe','-Command','Stop-Process -Name "OneDrive" -Force'], capture_output=True,text=True,creationflags=CREATE_NO_WINDOWS)

        # ПРОВЕРЯЕМ ЧТО ONEDRIVE ДЕЙСТВИТЕЛЬНО ОСТАНОВИЛИ
        check = subprocess.run(['powershell.exe', '-Command', 'Get-Process -Name "OneDrive"'], capture_output=True, text=True,creationflags=CREATE_NO_WINDOWS)

        if check.returncode == 0:
            input('Не удалось остановить процесс OneDrive, его удаление остановлено /nДля продолжения нажмите Enter...')

        else:
            # Смотрим где хранится диистолятор
            file_exe = [r'C:\Windows\SysWOW64\OneDriveSetup.exe', r'C:\Windows\System32\OneDriveSetup.exe']

            for i in file_exe:
                if Path(i).is_file():
                    fileOnedrive_uininstall = i
                    break

            if fileOnedrive_uininstall:
                print('Начинаю удаление... \nЭто может занять 1-2 минуты, ЖДЕМ!')
                subprocess.run(['powershell.exe','-Command',f'& "{fileOnedrive_uininstall}" /uninstall'],creationflags=CREATE_NO_WINDOWS)
                

            # = Убираем эту шляпу из панели навигации в проводнике
            subprocess.run(['powershell.exe','-Command',r'Remove-Item -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace\{018D5C66-4533-4307-9B53-224DE2ED1FE6}" -Recurse -ErrorAction SilentlyContinue'],creationflags=CREATE_NO_WINDOWS)
            
            print('OneDrive удален \nДля продолжения нажмите Enter')
            input()

    # ==== СПИСОК ПРИЛОЖЕНИЙ НА УДАЛЕНИЕ БEЗ ONEDRIVE ====
    del_programm = {'media player':'Microsoft.ZuneMusic',
                    'microsoft 365 copilot': 'Microsoft.Copilot',
                    'microsoft 365 copilo old':'Microsoft.549981C3F5F10',
                    'microsoft clipchamp':'Clipchamp.Clipchamp',
                    'microsoft Teams':'MSTeams',
                    'microsoft To Do':'Microsoft.Todos',
                    'power automate':'Microsoft.PowerAutomateDesktop',
                    'Быстрая подержка':'MicrosoftCorporationII.QuickAssist',
                    'Погода':'Microsoft.BingWeather',
                    'Xbox(все компоненты)': 'Xbox',
                    'центр отзывов':'Microsoft.WindowsFeedbackHub'}

    # ==== ПОЛУЧЕНИЯ СТРОКУ УСТАНОВЛЕНЫХ ПРИЛОЖЕНИЙ ====
    result = subprocess.run(['powershell.exe', '-Command', 'Get-AppxPackage | Select-Object Name'],capture_output=True, text=True,creationflags=CREATE_NO_WINDOWS)
    output_result = result.stdout
    install_programm = output_result.splitlines()
    
    # ==== ЧИСТИМ СПИСОК ОТ ЛИШНИХ ПРОБЕЛОВ ====
    install_programm = [i.strip() for i in install_programm]

    # ==== Создаем 2 списка для себя и для вывода пользователю и отдельный список для xbox
    cod_name = []
    user_name= []
    xbox_programm =[]

    for i in install_programm:
        for nam, cod in del_programm.items():
            if i == cod:
                cod_name.append(cod)
                user_name.append(nam)
                break

    # === ОТДЕЛЬНО ИЩЕМ КОМПОНЕНТЫ XBOX ===
    for i in install_programm:
        if 'Xbox' in i:
            xbox_programm.append(i)


    # ==== ЕСЛИ ПРОГРАММ ДЛЯ УДАЛЕНИЯ НЕ НАШЛИ ВЫХОДИ ====
    if not cod_name:
        input('Программ для удаления нету \nДля завершения нажмите Enter...')
        exit(0)

    # === ДЕЛАЕМ 2 РАЗНЫХ ВЫВОДА С XBOX И БЕЗ
    if not xbox_programm:
        inp_user = input(f'Были найдены следующие программы:{user_name} \nХотите их удалить(Да/Нет)? ')

    else:
        user_name.append('Xbox')
        inp_user = input(f'Были найдены следующие программы:{user_name} \nХотите их удалить(Да/Нет)? ')

    # === УДАЛЯЕМ ПРИЛОЖЕНИЯ ===
    if inp_user == 'Да':
        for i in range(len(cod_name)):
            try:
                subprocess.run(['powershell.exe','-Command',f'Get-AppxPackage -Name {cod_name[i]} | Remove-AppxPackage'], capture_output=True, text=True,creationflags=CREATE_NO_WINDOWS)
                print(f'Программа {user_name[i]} удалена!')

            except Exception as a:
                input(f'При удалении программы {i} произошла ошибка \n{a}')

        # === ЕСЛИ В ПЕРЕМЕННОЙ ЕСТЬ XBOX УДАЛАЕМ ЕГО К ЧЕРТЯМ ===
        if xbox_programm:
            try:
                subprocess.run(['powershell.exe', f'Get-AppxPackage -Name *Xbox* | Remove-AppxPackage'], capture_output=True, text=True,creationflags=CREATE_NO_WINDOWS)
                print(f'Программа Xbox удалена!')

            except Exception as a:
                input(f'При удалении программы xbox произошла ошибка \n{a}')

    elif inp_user == 'Нет':
        print('Удаление отменено')
        exit(0)

    else:
        print('Некоректный ввод!')
        output_mess()



output_mess()

