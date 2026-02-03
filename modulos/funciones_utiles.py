import os

# Formato en pesos para el precio

def formatear_pesos(valor):
    return f"${valor:,.0f}".replace(",", ".")

# Limpia la consola.

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')