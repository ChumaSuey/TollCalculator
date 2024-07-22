def calcular_total_peajes(montos, cantidades):
    """Calcula el total de peajes a partir de una lista de montos y una lista de cantidades."""
    total = 0
    for monto, cantidad in zip(montos, cantidades):
        total += monto * cantidad
    return total

def menu():
    """Muestra un menú interactivo para elegir entre diferentes opciones."""
    print("Calculadora de peajes")
    print("---------------------")
    print("1. Calcular total de peajes")
    print("2. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        montos = []
        cantidades = []
        while True:
            monto = float(input("Ingresa el monto: "))
            cantidad = int(input("Ingresa la cantidad de peajes: "))
            montos.append(monto)
            cantidades.append(cantidad)
            print("Montos:", montos)
            print("Cantidades:", cantidades)
            total = calcular_total_peajes(montos, cantidades)
            print("Total de peajes:", total)
            continuar = input("¿Deseas continuar? (s/n): ")
            if continuar.lower() != "s":
                break
        menu()  # Volver al menú después de terminar la opción 1

    elif opcion == "2":
        print("Saliendo de la calculadora de peajes...")
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

menu()