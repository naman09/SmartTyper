# Import the required libraries
from tkinter import *
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
import threading
from Backend.main import run_app, stop_app
from pynput.keyboard import Key, Controller  

# Create an instance of tkinter frame or window
window=Tk()
start_stop_label = 'Stop'

# Define a function for quit the window
def quit_window(icon, item):
   stop_app()
   icon.stop()
   window.destroy()

# Define a function to show the window again
def add_data(icon, item):
   icon.stop()
   window.after(0,window.deiconify())

def start_stop_app(icon, item2):
    global start_stop_label
    print(item2)
    if start_stop_label == 'Start':
        start_stop_label = 'Stop'
        print("Pressed Start")
        icon.menu = (item('Exit', quit_window), item('Add Data', add_data), item(start_stop_label, start_stop_app))
        start_backend()

    elif start_stop_label == 'Stop':
        start_stop_label = 'Start'
        print("Pressed Stop")
        icon.menu=(item('Exit', quit_window), item('Add Data', add_data), item(start_stop_label, start_stop_app))
        stop_app()
        
    else:
        print('Error....')



# Hide the window and show on the system taskbar
def hide_window():   
    window.withdraw()
    image=Image.open("SmartTyperIcon.png")
    menu=(item('Exit', quit_window), item('Add Data', add_data), item(start_stop_label, start_stop_app))
    icon=pystray.Icon("name", image, "SmartTyper", menu)
    icon.run()


def start_ui():
    window.title("System Tray Application")
    # Set the size of the window
    window.geometry("700x350")

    window.protocol('WM_DELETE_WINDOW', hide_window)

    window.mainloop()

def start_backend():
    backend_thread = threading.Thread(target=run_app, args=())
    backend_thread.start() 

def start_app():
    start_backend()
    start_ui()


if __name__ == "__main__":
   start_app()
   