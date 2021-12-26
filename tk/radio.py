from tkinter import *

root = Tk()
root.title("Hola mundo")

# r = IntVar()
# r.set(2)

CHANCHITOS = [
    ("Chancla", 1),
    ("Pizza", 2),
    ("Torta", 3),
    ("Hamburguesa", 4),
    ("Pollo", 5) 
]     

chanchito = StringVar()
chanchito.set("Chancla")
for text, value in CHANCHITOS:
    Radiobutton(root, text=text, variable=chanchito, value=value).pack(anchor=W)

l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()