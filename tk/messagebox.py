from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hola mundo")

def click():
    messagebox.showwarning("Popup", "Hola mundo")

def click2():
    messagebox.showinfo("Popup", "Hola mundo")

def click3():
    messagebox.showerror("Popup", "Hola mundo :(")

def click4():
    #Devuelve una cadena
    res = messagebox.askquestion("Popup", "Hola mundo")
    if res == "yes":
        messagebox.showinfo("Respuesta", "Respuesta fue "+res)
    else:
        messagebox.showinfo("Respuesta", "Respuesta fue "+res)

def click5():
    #devuelve una cadena
    res = messagebox.askyesno("Popup", "Hola mundo")
    if res == True:
        messagebox.showinfo("Respuesta", "Respuesta fue "+str(res))
    else:
        messagebox.showinfo("Respuesta", "Respuesta fue "+str(res))

def click6():
    #devuele booleano
    res = messagebox.askokcancel("Popup", "Desea realizar la accion?")
    if res:
        messagebox.showinfo("Respuesta", "Respuesta fue "+str(res))
    else:
        messagebox.showinfo("Respuesta", "Respuesta fue "+str(res))

def click7():
    #devuelve una cadena
    res = messagebox.askretrycancel("Popup", "Desea realizar la accion?")
    if res:
        messagebox.showinfo("Respuesta", "Respuesta fue "+str(res))
    else:
        messagebox.showinfo("Respuesta", "Respuesta fue "+str(res))

btn = Button(root, text="Presioname", command=click5)
btn.pack()

root.mainloop()