import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["tkinter", "ttkthemes", "tkcalendar"], "include_files": ["tasks.db"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("main.py", base=base, icon="icon.ico")  # Замените "your_icon.ico" на путь к вашей иконке (если есть)
]

setup(
    name="DailyTasks",
    version="1.0",
    description="Your Daily Tasks App",
    options={"build_exe": build_exe_options},
    executables=executables
)
