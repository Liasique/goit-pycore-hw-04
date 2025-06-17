import sys
from pathlib import Path
from colorama import Fore, init

import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Please provide a folder path")
    sys.exit()

folder = Path(sys.argv[1])

if not folder.exists() or not folder.is_dir():
    print("Invalid folder path")
    sys.exit()

print(" Folder is valid:", folder)

#TEST: (base) ➜  goit-pycore-hw-04 git:(main) ✗ python task3/task3.py task2 
#  Folder is valid: task2

#   i   I sguess that it could be better to create run_task3.sh first
# 	1.	Create virtual environment -> python -m venv venv
# 	2.	Activate environment -> source venv/bin/activate
# 	3.	Install colorama -> pip install colorama:   
#          init()init() - activation colors
#          Fore - colors -> 🔵 - for folders and 🟡 - for files
#          Style.RESET_ALL 
# 	4.	Create file hw03.py and write the scrip

#   5.  Write script
# 	6. Save dependencies to requirements.txt -> pip freeze > requirements.txt



"""
Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.



Вимоги до завдання:

Створіть віртуальне оточення Python для ізоляції залежностей проекту.
Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
Використання бібліотеки colorama для реалізації кольорового виведення.
Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.




"""