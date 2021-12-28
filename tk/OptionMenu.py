from tkinter import *

root = Tk()
root.title("Hola mundo: OptionMenu")
root.geometry("500x500")


lista = ['hola', 'mundo', 'como', 'estas']
value = StringVar()
value.set(lista[0])
drop = OptionMenu(root, value, *lista)
drop.pack()
btn = Button(root, text="Click me", command=lambda: print(value.get()))
btn.pack()
root.mainloop()
