from tkinter import *

root = Tk()
root.title("Hola mundo")

# frame = LabelFrame(root, text="Login", padx=50, pady=50, borderwidth=10)
frame = Frame(root, padx=50, pady=50, borderwidth=10)
frame.pack(padx=50, pady=50)
l = Label(frame, text="Estoy dentro de un frame: ")
btn = Button(frame, text="Click me",command=root.quit)
l.pack()
btn.pack()
root.mainloop()