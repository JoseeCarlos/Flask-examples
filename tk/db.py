from tkinter import *
import sqlite3 
from tkmacosx import Button

root = Tk()
root.title("Hola mundo: Todo List")
root.geometry("500x500")


conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT NOT NULL,
    COMPLETED BOOLEAN NOT NULL
    );
    """)

conn.commit()

def remove(id):
    def _remove():
        c.execute("DELETE FROM todo WHERE id=?", (id,))
        conn.commit()
        render_todo()
    return _remove
    
#currying
def complete(id):
    def _complete():
       todo = c.execute("SELECT * FROM todo WHERE id=?", (id,)).fetchone()
       c.execute("UPDATE todo SET COMPLETED=? WHERE id=?", (not todo[3], id))
       conn.commit()
       print(id)
    return _complete

def render_todo():
    rows = c.execute("SELECT * FROM todo").fetchall()
    for widget in frame.winfo_children():
        widget.destroy()
    for row in range(0, len(rows)):
        id = rows[row][0]
        completed = rows[row][3]
        description = rows[row][2]
        color = "#555555" if completed else "black"
        l = Checkbutton(frame, text=description,fg=color , width=42, anchor=W, command=complete(id))
        l.grid(row=row, column=0, sticky=W)
        btn = Button(frame, text="X", command=remove(id))
        btn.grid(row=row, column=1, sticky=W)
        l.select() if completed else l.deselect()


def add_todo():
    if len(e.get()) > 0:
        c.execute("INSERT INTO todo (description, COMPLETED) VALUES (?, ?)",
                  (e.get(), False))
        conn.commit()
        e.delete(0, END)
        render_todo()
    else:
        print("No hay nada que agregar")
    

#Formulario
l = Label(root, text="Tarea")
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='Agregar', command=add_todo)
btn.grid(row=0, column=2)

frame = LabelFrame(root, text="Mis Tareas", padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nsew',padx=5)

e.focus()

root.bind('<Return>', lambda x :add_todo())
render_todo()
root.mainloop()
