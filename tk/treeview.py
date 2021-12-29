from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hola mundo: Treeview")

tree = ttk.Treeview(root)
tree["columns"] = ("one", "two", "three")

tree.column('#0', width=100)
tree.column("one", width=100)
tree.column("two", width=100)
tree.column("three", width=100)

tree.heading("#0", text="Item")
tree.heading("one", text="one")
tree.heading("two", text="two")
tree.heading("three", text="three") 

tree.grid(row=0, column=0, sticky=NSEW)

tree.insert("", END, 'lala', values=("1a", "1b", "1c"), text="Chanchito feliz")
tree.insert("", END, 'lele', values=("2a", "2b", "2c"), text="Chanchito triste")
tree.insert("lele", END, 'lili', values=("3a", "3b", "3c"), text="Hijo")



root = mainloop()