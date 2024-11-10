import tkinter as tk

ventana = tk.Tk()
marco = tk.Frame(ventana)
marco.grid(row=0, column=0)

Item1 = tk.Entry(marco)
Item1.grid(row=0, column=1)

Item2 = tk.Label(marco, text="¡Hola! ¿Qué tal?")
Item2.grid(row=1, column=2)

button = tk.Button(marco, text="Púlsame")
button.grid(row=2, column=3, columnspan=2)

ventana.mainloop()

