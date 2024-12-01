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
    # Check if any of the values in montos and cantidades are empty
    if any(not entry_monto.get() or not entry_cantidad.get() for entry_monto, entry_cantidad in zip(montos, cantidades)):
        messagebox.showwarning("Empty values", "Please enter values for all tolls and quantities.")
        return

    total = sum(float(monto.get()) * int(cantidad.get()) for monto, cantidad in zip(montos, cantidades))
    messagebox.showinfo("Total de peajes", f"El total de peajes es: {total}")

def reset_fields():
    for entry_monto in montos:
        entry_monto.delete(0, tk.END)
    for entry_cantidad in cantidades:
        entry_cantidad.delete(0, tk.END)

    # Remove any additional toll fields
    for widget in root.winfo_children():
        if widget not in [title_label, add_button, calculate_button, reset_button]:
            widget.destroy()

    # Reset the montos and cantidades lists
    montos.clear()
    cantidades.clear()

    # Add a new toll field (with default values)
    add_toll_fields()

# Create the main window
root = tk.Tk()
root.title("Calculadora de peajes")
root.bind("<Return>", lambda event: calculate_total_tolls())

# Title label
title_label = tk.Label(root, text="Calculadora de peajes", font=("Helvetica", 16))
title_label.pack()

# Button to add new toll fields
add_button = tk.Button(root, text="Agregar Peaje [Q]", command=add_toll_fields)
add_button.pack()
root.bind("<q>", lambda event: add_toll_fields())

# Button to calculate total tolls
calculate_button = tk.Button(root, text="Calcular Total [ENTER]", command=calculate_total_tolls)
calculate_button.pack()

# Button to reset fields
reset_button = tk.Button(root, text="Reset[W]", command=reset_fields)
reset_button.pack()
root.bind("<w>", lambda event: reset_fields())

if __name__ == "__main__":
    root.mainloop()

# Notes: The reset button just cleans the numbers / strings, it doesn't remove the toll and quantity fields
