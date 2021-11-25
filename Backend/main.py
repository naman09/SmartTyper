from pynput.keyboard import Key, Listener, Controller 
from Core.Engine import Engine
from Core.KeyboardTyper import KeyboardTyper
from DataAccess.FileDB import FileDB
import sys

def run_app():
    print('Backend started!')
    dObj = FileDB()
    Engine(dObj)

def stop_app():
    print('Backend stopped!')
    KeyboardTyper().esc()


if __name__== "__main__":
    if sys.argv[1] == 'stop':
        stop_app()
    else:
        run_app()


