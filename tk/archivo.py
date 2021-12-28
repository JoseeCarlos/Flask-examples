from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Hola mundo: Archivo")

# root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select Photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
# l = Label(root, text=root.filename)
# l.pack()
# img = Image.open(root.filename)
# imgTk = ImageTk.PhotoImage(img)
# l2 = Label(root, image=imgTk)
# l2.pack()

def open():
    global imgTk
    root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select Photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    l = Label(root, text=root.filename)
    l.pack()
    img = Image.open(root.filename)
    imgTk = ImageTk.PhotoImage(img)
    l2 = Label(root, image=imgTk)
    l2.pack()

btn = Button(root, text='Cargar imagen', command=open )
btn.pack()
root.mainloop()

