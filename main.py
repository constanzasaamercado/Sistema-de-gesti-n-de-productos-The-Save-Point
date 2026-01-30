# Encabezado

print("*******************************")
print("* BIENVENIDO/A A THE SAVE POINT *")
print("*******************************")

# Ingreso de usuario

nombre_usuario = input("Por favor, ingresa tu nombre de usuario: ")
print(f"¡Hola, {nombre_usuario}! iniciando sistema de gestión de productos.")

videojuegos_inventario = []

from modulos.gestion_datos import capturar_datos

nuevo_videojuego = capturar_datos()
videojuegos_inventario.append(nuevo_videojuego)

print(f"El videojuego {nuevo_videojuego['Titulo']} ha sido guardado!")
