from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("CRM :Libreta de clientes")

conn = sqlite3.connect('crm.db')

c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS cliente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            empresa TEXT NOT NULL
            );""")

def render_cliente():
    rows = c.execute("SELECT * FROM cliente").fetchall()
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", END, row[0], values=(row[1], row[2], row[3]))

def insertar(cliente):
    c.execute("INSERT INTO cliente VALUES (NULL, :nombre, :telefono, :empresa)", cliente)
    conn.commit()
    render_cliente()

def agregar_cliente():
    def guardar_cliente():
        if not nombre.get() or not telefono.get() or not empresa.get():
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
        cliente = {
            'nombre': nombre.get(), 
            'telefono': telefono.get(),
            'empresa': empresa.get()
        }
        insertar(cliente)
        top.destroy()
    top = Toplevel()
    top.title("Agregar cliente")

    lnombre = Label(top, text="Nombre: ")
    nombre = Entry(top,width=40)
    lnombre.grid(row=0, column=0, sticky=W)
    nombre.grid(row=0, column=1, sticky=W)

    ltelefono = Label(top, text="Telefono: ")
    telefono = Entry(top,width=40)
    ltelefono.grid(row=1, column=0, sticky=W)
    telefono.grid(row=1, column=1, sticky=W)

    lempresa = Label(top, text="Empresa: ")
    empresa = Entry(top,width=40)
    lempresa.grid(row=2, column=0, sticky=W)
    empresa.grid(row=2, column=1, sticky=W)

    guardar = Button(top, text="Guardar", command=lambda: guardar_cliente())
    guardar.grid(row=3, column=1, sticky=W)

    top.mainloop()

def eliminar_cliente():
    id = tree.selection()[0]
    cliente = c.execute("SELECT * FROM cliente WHERE id=?", (id,)).fetchone()

    respuesta = messagebox.askokcancel("Eliminar", "¿Está seguro de eliminar el cliente {}?".format(cliente[1]))
    if respuesta:
        c.execute("DELETE FROM cliente WHERE id=:id", {'id': id})
        conn.commit()
        render_cliente()
    else:
        messagebox.showinfo("Eliminar", "El cliente no se ha eliminado")


btn = Button(root, text="Agregar Cliente", command=agregar_cliente)
btn.grid(row=0, column=0)

btn_eliminar = Button(root, text="Eliminar Cliente", command=eliminar_cliente)
btn_eliminar.grid(row=0, column=1)

tree = ttk.Treeview(root)
tree ["columns"] = ("Nombre", "Telefono", "Empresa")
tree.column("#0", width=0,stretch=NO)
tree.column("Nombre", width=100)
tree.column("Telefono", width=100)
tree.column("Empresa", width=100)

tree.heading("Nombre", text="Nombre")
tree.heading("Telefono", text="Telefono")
tree.heading("Empresa", text="Empresa")

tree.grid(row=1, column=0, sticky=NSEW,columnspan=2)
render_cliente()
root.mainloop()