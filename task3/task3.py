import sys
from pathlib import Path
from colorama import init, Fore, Style
init()  # initialize colorama (for terminal)
print(Fore.YELLOW + "i'm yellow")
print(Fore.BLUE + "i'm blue")
print(Style.RESET_ALL + "i'm neitral")
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



