from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Hola mundo")

# image = Image.open("x.png")
# image.show()

img = ImageTk.PhotoImage(Image.open("x.png"))
l = Label(root, image=img)
l.pack()

root.mainloop()
