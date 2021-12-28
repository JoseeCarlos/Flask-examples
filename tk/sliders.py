from tkinter import *

root = Tk()
root.title("Hola mundo: Sliders")

vertical = Scale(root, from_=0, to=100, orient=VERTICAL, command=lambda x: print(x))
vertical.pack()

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
horizontal.pack()

btn = Button(root, text="Click me", command=lambda: print(vertical.get(), horizontal.get()))
btn.pack()
root.mainloop()
