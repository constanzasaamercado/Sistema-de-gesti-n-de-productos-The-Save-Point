# Importar módulo de gestión de datos
import modulos.gestion_datos as gestion
from modulos.gestion_datos import capturar_datos, mostrar_inventario, eliminar_videojuego

# Encabezado

print("*******************************")
print("* BIENVENIDO/A A THE SAVE POINT *")
print("*******************************")

# Ingreso de usuario

nombre_usuario = input("Por favor, ingresa tu nombre de usuario: ")
print(f"¡Hola, {nombre_usuario}! iniciando sistema de gestión de productos.")


videojuegos_inventario = []



while True:
        print("\n--- GESTIÓN DE PRODUCTOS---")
        print("1. Ingresar datos")
        print("2. Visualización de inventario")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nuevo_videojuego = capturar_datos()
            videojuegos_inventario.append(nuevo_videojuego)
            print(f"El videojuego {nuevo_videojuego['Titulo']} ha sido guardado!")

        elif opcion == "2":
            mostrar_inventario(videojuegos_inventario)
        
        elif opcion == "3":
            eliminar_videojuego(videojuegos_inventario)
        elif opcion == "5":
            print(f"¡Hasta luego {nombre_usuario}! Cerrando The Save Point...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# nuevo_videojuego = capturar_datos()
# videojuegos_inventario.append(nuevo_videojuego)

# print(f"El videojuego {nuevo_videojuego['Titulo']} ha sido guardado!")
