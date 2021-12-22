from tkinter import *

root = Tk()
root.title("Calculadora Pies a metros")

frame = Frame(root, padx=10, pady=10)
frame.grid(row=0, column=0)

pies = StringVar()
input_pies = Entry(frame, textvariable=pies, width=10)
input_pies.grid(row=0, column=1)

metros = StringVar()
metros.set("ingresa valor")
Label(frame, textvariable=metros).grid(row=1, column=1)

Button(frame, text="Convertir", command=lambda: convertir(pies, metros)).grid(row=2, column=2)

def convertir(pies, metros):
    try:
        metros.set(float(pies.get()) * 0.3048)
    except ValueError:
        metros.set("Error")

Label(frame, text="Pies").grid(row=0, column=0)
Label(frame, text="es igual a").grid(row=1, column=0)
Label(frame, text="Metros").grid(row=1, column=3)

input_pies.focus()
root.bind("<Return>", lambda event: convertir(pies, metros))
root.mainloop()

