from tkinter import *

root = Tk()
root.title("Buttons")
l = Label(root, text="Hello ")
def click_me():
    l.pack()

btn = Button(root, text="Click me", command=click_me, fg="red", bg="yellow")
btn.pack()

root.mainloop()