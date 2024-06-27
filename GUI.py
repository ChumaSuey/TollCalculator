from Backend import calcular_total_peajes_backend
import tkinter as tk
from functools import partial

def validate_float(entry):
    if entry.get().strip() == '':
        return False
    try:
        float(entry.get())
        return True
    except ValueError:
        return False

def get_entry_value(entrybox):
    entry_value = entrybox.get()
    if not entry_value:
        return 0
    return entry_value


def on_validate(entrybox):
    entry_value = entrybox.get()

    if not entry_value:  # Check if entry is empty
        return True

    try:
        float(entry_value)  # Attempt to convert to float
        return True
    except ValueError:
        return False


def handle_user_input():
    """Handles the user input and calculates the total tolls."""
    if validate_float(entry_monto) and validate_float(entry_monto2) and validate_float(entry_monto3):
        montos = [float(entry_monto.get()), float(entry_monto2.get()), float(entry_monto3.get())]
        cantidades = [int(entry_cantidad.get()), int(entry_cantidad2.get()), int(entry_cantidad3.get())]
        total_peajes = calcular_total_peajes_backend(montos, cantidades)
        label_result.config(text=f"Total de peajes: {total_peajes}")
    else:
        # Handle the case where the input is not a valid float
        print("Please enter valid numerical values")


# Create the main window
window = tk.Tk()
window.title("Calculadora de Peajes")
entry_monto = tk.Entry()
entry_monto2 = tk.Entry()
entry_monto3 = tk.Entry()

vcmd = (window.register(on_validate), '%P')

# Create labels and entry fields
label_monto1 = tk.Label(window, text="Monto 1:")
label_monto1.pack()
entry_monto = tk.Entry(window, validate="key", validatecommand=(lambda P, entrybox=entry_monto: on_validate(entry_monto), '%P'))
entry_monto.pack()

label_cantidad1 = tk.Label(window, text="Cantidad 1:")
label_cantidad1.pack()
entry_cantidad = tk.Entry(window)
entry_cantidad.pack()

label_monto2 = tk.Label(window, text="Monto 2:")
label_monto2.pack()
entry_monto2 = tk.Entry(window, validate="key", validatecommand=(lambda P, entrybox=entry_monto2: on_validate(entry_monto2), '%P'))
entry_monto2.pack()


label_cantidad2 = tk.Label(window, text="Cantidad 2:")
label_cantidad2.pack()
entry_cantidad2 = tk.Entry(window)
entry_cantidad2.pack()

label_monto3 = tk.Label(window, text="Monto 3:")
label_monto3.pack()
entry_monto3 = tk.Entry(window, validate="key", validatecommand=(lambda P, entrybox=entry_monto3: on_validate(entry_monto3), '%P'))
entry_monto3.pack()

label_cantidad3 = tk.Label(window, text="Cantidad 3:")
label_cantidad3.pack()
entry_cantidad3 = tk.Entry(window)
entry_cantidad3.pack()

# Create a button to calculate the total
button_calcular = tk.Button(window, text="Calcular", command=handle_user_input)
button_calcular.pack()

# Create a label to display the result
label_result = tk.Label(window, text="")
label_result.pack()

# Start the main event loop
window.mainloop()