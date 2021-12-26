from tkinter import *

root = Tk()
root.title("Hola mundo")

exit = Button(root, text="Salir", command=root.quit)
exit.pack()

root.mainloop()