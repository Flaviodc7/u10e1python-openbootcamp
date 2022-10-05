import tkinter
from tkinter import ttk


def sel():
    selection = "Has seleccionado la opción: " + str(seleccionado.get())
    label.config(text=selection)


def deseleccionar():
    seleccionado.set('')
    label.config(text="No hay ninguna selección realizada")


window = tkinter.Tk()

seleccionado = tkinter.StringVar()


rb1 = ttk.Radiobutton(window, text='Verde', value='Verde', variable=seleccionado, command=sel)
rb1.grid(column=1, row=0, pady=5, padx=5)

rb2 = ttk.Radiobutton(window, text='Azul', value='Azul', variable=seleccionado, command=sel)
rb2.grid(column=2, row=0, pady=5, padx=5)

rb3 = ttk.Radiobutton(window, text='Rojo', value='Rojo', variable=seleccionado, command=sel)
rb3.grid(column=3, row=0, pady=5, padx=5)

label = ttk.Label(window, text="No hay ninguna selección realizada")
label.grid(column=2, row=2, padx=5, pady=5)

btnReestablecer = tkinter.Button(window, text="Reestablecer", command=deseleccionar)
btnReestablecer.grid(column=2, row=4, pady=5, padx=5)

window.mainloop()
