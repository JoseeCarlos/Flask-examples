from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hola mundo")

#Solucion 1
# def open():
#     img= ImageTk.PhotoImage(Image.open("images/1.png"))
#     top = Toplevel()
#     top.title("Hola mundo, nueva ventana")
#     l = Label(top, text="soy un texto en una seguna ventana")
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()

#solucion 2
# def open():
#     global img
#     img= ImageTk.PhotoImage(Image.open("images/1.png"))
#     top = Toplevel()
#     top.title("Hola mundo, nueva ventana")
#     l = Label(top, text="soy un texto en una seguna ventana")
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()

#solucion 3
def open(img):
    top = Toplevel()
    top.title("Hola mundo, nueva ventana")
    l = Label(top, text="soy un texto en una seguna ventana")
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()


img= ImageTk.PhotoImage(Image.open("images/1.png"))
btn = Button(root, text="Click me", command=lambda: open(img)).pack()
root.mainloop()

