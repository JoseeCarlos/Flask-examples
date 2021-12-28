from tkinter import *

root = Tk()
root.title("Hola mundo: Checkbox")
root.geometry("500x500")

var = StringVar()
var.set("no")
c = Checkbutton(root, text="Soy un checkbox", variable=var, onvalue='si', offvalue='no')
c.pack()

btn = Button(root, text="Click me", command=lambda: print(var.get()))
btn.pack()


root.mainloop()