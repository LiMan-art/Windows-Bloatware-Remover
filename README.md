# Windows Bloatware Remover

Скрипт для автоматического удаления OneDrive и предустановленных приложений Windows.

## Возможности
- Проверка наличия PowerShell
- Удаление OneDrive (с остановкой процесса)
- Удаление предустановленных приложений:
  - Microsoft Copilot
  - Clipchamp
  - Microsoft Teams
  - Xbox (все компоненты)
  - Погода, Центр отзывов и другие
## Требования
- Windows 10/11
- Python 3.x

## Важно
- Создайте точку восстановления системы перед использованием
- Некоторые удаленные приложения нельзя будет восстановить через стандартные средства
- Скрипт не удаляет ваш личный OneDrive, только само приложение

## Установка и использование
```bash
git clone https://github.com/LiMan-art/windows-bloatware-remover.git
cd windows-bloatware-remover
python app.py


