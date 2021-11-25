import tkinter as tk
from tkinter import *
from tkinter import ttk
from typing import Any

class App:
    def __init__(self, root):
        self.root = root
        root.geometry("600x500")
        root.title('SmartTyper')
        root.resizable(0, 0)

        # configure the grid
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=3)

        # label1 = ttk.Label(root, text="letiable")
        # label1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        # label2 = ttk.Label(root, text="Value")
        # label2.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        # separator = ttk.Separator(root, orient='vertical')
        # separator.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)


        self.scroll_bar = ttk.Scrollbar(root)
        self.scroll_bar.grid(row=1, column=3, rowspan=10)
        self.key_value_list = Listbox(root, yscrollcommand=self.scroll_bar.set)
        self.add_label("@name", "Naman")
        self.add_label("@aadhaar", "XXX-XXXX-XXXXX")
        self.key_value_list.grid(row=2,column=0, columnspan=2)
        self.scroll_bar.config( command = self.key_value_list.yview)
        ttk.Button(root, text="Delete", command=self.delete).grid(row=4,column=2)
        ttk.Button(root, text="Add", command=self.add_label).grid(row=4,column=1)
        ttk.Button(root, text="Edit", command=self.edit).grid(row=5,column=1)

    def add_label(self, key="@name", value="Naaaa"):
        self.key_value_list.insert(END, key + "  " + value)
    
    def delete(self):
        for item in self.key_value_list.curselection():
            self.key_value_list.delete(item)
    
    def edit(self):
        for item in self.key_value_list.curselection():
            self.key_value_list.delete(item)
            self.key_value_list.insert(item, "@Name  Shubham")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
