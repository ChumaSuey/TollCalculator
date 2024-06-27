import tkinter as tk
from tkinter import messagebox

montos = []
cantidades = []

def add_toll_fields():
    new_label_monto = tk.Label(root, text="Monto:")
    new_label_monto.pack()
    new_entry_monto = tk.Entry(root)
    new_entry_monto.pack()

    new_label_cantidad = tk.Label(root, text="Cantidad de peajes:")
    new_label_cantidad.pack()
    new_entry_cantidad = tk.Entry(root)
    new_entry_cantidad.pack()

    montos.append(new_entry_monto)
    cantidades.append(new_entry_cantidad)

def calculate_total_tolls():
    total = sum(float(monto.get()) * int(cantidad.get()) for monto, cantidad in zip(montos, cantidades))
    messagebox.showinfo("Total de peajes", f"El total de peajes es: {total}")

def reset_fields():
    for entry_monto in montos:
        entry_monto.delete(0, tk.END)
    for entry_cantidad in cantidades:
        entry_cantidad.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculadora de peajes")

# Title label
title_label = tk.Label(root, text="Calculadora de peajes", font=("Helvetica", 16))
title_label.pack()

# Button to add new toll fields
add_button = tk.Button(root, text="Agregar Peaje", command=add_toll_fields)
add_button.pack()

# Button to calculate total tolls
calculate_button = tk.Button(root, text="Calcular Total", command=calculate_total_tolls)
calculate_button.pack()

# Button to reset fields
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack()

root.mainloop()

# Notes: The reset button just cleans the numbers / strings, it doesn't remove the toll and quantity fields