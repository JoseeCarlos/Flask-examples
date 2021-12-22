from tkinter import *
from tkmacosx import Button

root = Tk()
root.configure(background="#333333")
root.title("Calculadora")
root.geometry("386x168")

equation = StringVar()
expression_entry = Entry(root,textvariable=equation)
expression_entry.grid(row=0, columnspan=4, sticky=W+E+N+S)

def press(num):
    equation.set(equation.get() + str(num))

def equalpress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set("Error")

def clear():
    equation.set("")

btn7 = Button(root, text="7", command=lambda: press(7),fg="#fff",bg="#666")
btn7.grid(row=1, column=0,sticky=W+E+N+S)
btn8 = Button(root, text="8", command=lambda: press(8),fg="#fff",bg="#666")
btn8.grid(row=1, column=1,sticky=W+E+N+S)
btn9 = Button(root, text="9", command=lambda: press(9),fg="#fff",bg="#666")
btn9.grid(row=1, column=2,sticky=W+E+N+S)
btn4 = Button(root, text="4", command=lambda: press(4),fg="#fff",bg="#666")
btn4.grid(row=2, column=0,sticky=W+E+N+S)
btn5 = Button(root, text="5", command=lambda: press(5),fg="#fff",bg="#666")
btn5.grid(row=2, column=1,sticky=W+E+N+S)
btn6 = Button(root, text="6", command=lambda: press(6),fg="#fff",bg="#666")
btn6.grid(row=2, column=2,sticky=W+E+N+S)
btn1 = Button(root, text="1", command=lambda: press(1),fg="#fff",bg="#666")
btn1.grid(row=3, column=0,sticky=W+E+N+S)
btn2 = Button(root, text="2", command=lambda: press(2),fg="#fff",bg="#666")
btn2.grid(row=3, column=1,sticky=W+E+N+S)
btn3 = Button(root, text="3", command=lambda: press(3),fg="#fff",bg="#666")
btn3.grid(row=3, column=2,sticky=W+E+N+S)
btn0 = Button(root, text="0", command=lambda: press(0),fg="#fff",bg="#666")
btn0.grid(row=4, column=0,sticky=W+E+N+S,columnspan=2)
btn_dot = Button(root, text=".", command=lambda: press("."),fg="#fff",bg="#666")
btn_dot.grid(row=4, column=2,sticky=W+E+N+S)

plus = Button(root, text="+", command=lambda: press("+"),fg="#fff",bg="#fe9727")
plus.grid(row=1, column=3,sticky=W+E+N+S)
minus = Button(root, text="-", command=lambda: press("-"),fg="#fff",bg="#fe9727")
minus.grid(row=2, column=3,sticky=W+E+N+S)
multiply = Button(root, text="*", command=lambda: press("*"),fg="#fff",bg="#fe9727")
multiply.grid(row=3, column=3,sticky=W+E+N+S)
divide = Button(root, text="/", command=lambda: press("/"),fg="#fff",bg="#fe9727")
divide.grid(row=4, column=3,sticky=W+E+N+S)
equals = Button(root, text="=", command=equalpress ,fg="#fff",bg="#fe9727")
equals.grid(row=5, column=3,sticky=W+E+N+S,columnspan=2)
clear = Button(root, text="Clear", command=clear,fg="#fff",bg="#999")
clear.grid(row=5, column=2,sticky=W+E+N+S)


root.mainloop()