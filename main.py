from pynput.keyboard import Key, Listener, Controller 
from Core.Engine import Engine
from DataAccess.FileDB import FileDB

if __name__== "__main__":
    dObj = FileDB()
    c = Engine(dObj)