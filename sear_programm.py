import subprocess

# скрить синию хрень
CREATE_NO_WINDOWS = 0x08000000


def sea_programm():
    del_programm = {
        "Media player": "Microsoft.ZuneMusic",
        "Microsoft 365 copilot": "Microsoft.Copilot",
        "Microsoft 365 copilo old": "Microsoft.549981C3F5F10",
        "Microsoft clipchamp": "Clipchamp.Clipchamp",
        "Microsoft Teams": "MSTeams",
        "Microsoft To Do": "Microsoft.Todos",
        "Power automate": "Microsoft.PowerAutomateDesktop",
        "Быстрая подержка": "MicrosoftCorporationII.QuickAssist",
        "Погода": "Microsoft.BingWeather",
        "Основное приложение Xbox": "Microsoft.XboxApp",
        "1-я Игровая панель": "Microsoft.XboxGamingOverlay",
        "Преобразование речи Xbox в текст": "Microsoft.XboxSpeechToTextOverlay",
        "Компонент для авторизации в профиль Xbox": "Microsoft.XboxIdentityProvider",
        "2-я Игровая панель": "Microsoft.XboxGameOverlay",
        "Вызов интерфейса Xbox внутри игр": "Microsoft.XboxGameCallableUI",
        "Центр отзывов": "Microsoft.WindowsFeedbackHub",

    }

    result = subprocess.run(
        ["powershell.exe", "-Command", "Get-AppxPackage | Select-Object Name"],
        capture_output=True,
        text=True,
        creationflags=CREATE_NO_WINDOWS,
    )

    outpu_result = result.stdout
    app_result = outpu_result.split()

    pr_app = []
    del_app = []

    for i, b in del_programm.items():
        if b in app_result:
            pr_app.append(i)
            del_app.append(b)

    print(f"[*] Всего было найдено {len(pr_app)} программ(ы).")
    
    for i, app in enumerate(pr_app, start=1):
        print(f"{i}. {app}")

    return del_app




