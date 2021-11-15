from pynput.keyboard import Key, Listener, Controller 
from Backend.Core.Engine import Engine
from Backend.Core.KeyboardTyper import KeyboardTyper
from Backend.DataAccess.FileDB import FileDB


def run_app():
    dObj = FileDB()
    Engine(dObj)

def stop_app():
    KeyboardTyper().esc()


if __name__== "__main__":
    run_app()