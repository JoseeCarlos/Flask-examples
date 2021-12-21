from tkinter import *

root = Tk()
root.title("Intro to Tkinter")
root.geometry("400x400")
Label1 = Label(root, text="Hello World")
Label2 = Label(root, text="Hello World")
label3 = Label(root, text="Hello World")



Label1.grid(row=0, column=0)
label3.grid(row=1, column=0)
Label2.grid(row=10, column=10)

root.mainloop()