import eel
import os
from subprocess import call



eel.init('Login')

def open_py_file():
    call(["python","main.py"])
open_py_file



eel.start('.\index.html')