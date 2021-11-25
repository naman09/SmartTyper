import tkinter as tk
from tkinter import ttk

# define keys and mappings
ITEMS = ['Item 1', 'Item 2', 'Item 3']
MAPPING = {'Item 1' : 1, 'Item 2' : 2, 'Item 3' : 3}

def onSelect(event):
    print(MAPPING[cmb.get()])

root = tk.Tk()

cmb = ttk.Combobox(root, state = 'readonly', values = ITEMS)
cmb.set(ITEMS[0])
cmb.bind('<<ComboboxSelected>>', onSelect)
cmb.pack()

root.mainloop()