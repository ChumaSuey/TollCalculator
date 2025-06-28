import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sv_ttk as svttk
import darkdetect as dt
from pywinstyles import apply_theme_to_titlebar  # Import the function

# In one of my jobs i do administrative tasks, one of them is counting the tolls of our vehicles
# Each toll is a different amount, and each vehicle has a different quantity of peajes(travels)
# This is a multiplicative operation, so we can calculate the total tolls as a sum of all tolls * quantity

# Global variables that will work as lists
# Montos will be the tolls, and cantidades will be quantities of travels for each toll with that price.
montos = []
cantidades = []

# Validation function to allow only numeric input
def validate_numeric_input(P):
    if P.isdigit() or P == "":
        return True
    return False

# Add new toll fields (function)
def add_toll_fields():
    new_label_monto = ttk.Label(root, text="Monto:")
    new_label_monto.pack()
    new_entry_monto = ttk.Entry(root, validate="key", validatecommand=(root.register(validate_numeric_input), '%P'))
    new_entry_monto.pack()

    new_label_cantidad = ttk.Label(root, text="Cantidad de peajes:")
    new_label_cantidad.pack()
    new_entry_cantidad = ttk.Entry(root, validate="key", validatecommand=(root.register(validate_numeric_input), '%P'))
    new_entry_cantidad.pack()

    montos.append(new_entry_monto)
    cantidades.append(new_entry_cantidad)

# Calculate the total tolls (function)
def calculate_total_tolls():
    # Check if any of the values in montos and cantidades are empty (validation)
    if any(not entry_monto.get() or not entry_cantidad.get() for entry_monto, entry_cantidad in zip(montos, cantidades)):
        messagebox.showwarning("Empty values", "Please enter values for all tolls and quantities.")
        return
    # Calculate the total tolls
    total = sum(float(monto.get()) * int(cantidad.get()) for monto, cantidad in zip(montos, cantidades))
    messagebox.showinfo("Total de peajes", f"El total de peajes es: {total}")

# Reset the fields (function)
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

# Function to remove the latest added toll fields
def remove_latest_toll_fields():
    if montos and cantidades:  # Check if there are toll fields to remove
        # Remove the last toll field widgets
        latest_monto = montos.pop()
        latest_cantidad = cantidades.pop()
        latest_monto.destroy()
        latest_cantidad.destroy()
    else:
        messagebox.showinfo("No tolls to remove", "There are no toll fields to remove.")

# All buttons have a root bind so that they work with the keyboard
# Also within the Text labels, between [ ] is the keyboard shortcut indicated
# Create the main window
root = tk.Tk()
apply_theme_to_titlebar(root)
svttk.set_theme(dt.theme())
root.title("Calculadora de peajes")
root.bind("<Return>", lambda event: calculate_total_tolls())

# Title label
title_label = ttk.Label(root, text="Calculadora de peajes", font=("Helvetica", 16))
title_label.pack()

# Button to add new toll fields
add_button = ttk.Button(root, text="Agregar Peaje [Q]", command=add_toll_fields)
add_button.pack()
root.bind("<q>", lambda event: add_toll_fields())

# Button to calculate total tolls
calculate_button = ttk.Button(root, text="Calcular Total [ENTER]", command=calculate_total_tolls)
calculate_button.pack()

# Button to reset fields
reset_button = ttk.Button(root, text="Reset[W]", command=reset_fields)
reset_button.pack()
root.bind("<w>", lambda event: reset_fields())

# Function to remove the latest added toll fields
# Button to remove the latest toll fields
remove_button = ttk.Button(root, text="Remove [E]", command=remove_latest_toll_fields)
remove_button.pack()
root.bind("<e>", lambda event: remove_latest_toll_fields())

if __name__ == "__main__":
    root.mainloop()

# Note: The reset button makes the toll/monto to be a cleaned single entry.