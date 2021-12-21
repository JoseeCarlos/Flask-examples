from tkinter import *

root = Tk()
root.title("Inputs")
root.geometry("500x500")

e= Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your name")

def click():
    texto = e.get()
    textvariable.set(texto)
    # l = Label(root, text=texto)
    # l.pack()
    e.delete(0, END)
    # l.configure(text=texto)

btn = Button(root, text="Click Me!", command=click)
btn.pack()

textvariable = StringVar()

l = Label(root, textvariable=textvariable)
l.pack()
root.mainloop()