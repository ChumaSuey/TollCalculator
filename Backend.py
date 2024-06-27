#def calcular_total_peajes_backend(montos, cantidades):
#    """Calcula el total de peajes a partir de una lista de montos y una lista de cantidades."""
#    total = 0
#    for monto, cantidad in zip(montos, cantidades):
#        total += monto * cantidad
#    return total

def calcular_total_peajes_backend(montos, cantidades):
    """Calcula el total de peajes a partir de una lista de montos y una lista de cantidades."""
    total = sum(monto * cantidad for monto, cantidad in zip(montos, cantidades))
    return total