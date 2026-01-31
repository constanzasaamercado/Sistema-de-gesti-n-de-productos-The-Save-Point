# Importar módulo de gestión de datos
import modulos.gestion_datos as gestion
from modulos.gestion_datos import capturar_datos, mostrar_inventario, eliminar_videojuego, videojuegos_inventario, buscar_videojuego


# Encabezado

print("*******************************")
print("* BIENVENIDO/A A THE SAVE POINT *")
print("*******************************")

# Ingreso de usuario

nombre_usuario = input("Por favor, ingresa tu nombre de usuario: ")
print(f"¡Hola, {nombre_usuario}! iniciando sistema de gestión de productos.")


# videojuegos_inventario = []

# Menu del sistema de gestión

while True:
        print("\n--- GESTIÓN DE PRODUCTOS---")
        print("1. Ingresar datos de nuevo videojuego")
        print("2. Modificar datos de videojuego")
        print("3. Eliminar videojuego")
        print("4. Visualización de inventario")
        print("5. Buscar un videojuego especifico")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nuevo_videojuego = capturar_datos()
            videojuegos_inventario.append(nuevo_videojuego)
            print(f"El videojuego {nuevo_videojuego['Titulo']} ha sido guardado!")
        
        elif opcion == "2":
            print("Funcionalidad de modificación de datos aún no implementada.")

        elif opcion == "3":
            eliminar_videojuego(videojuegos_inventario)


        elif opcion == "4":
            mostrar_inventario(videojuegos_inventario)
        
        elif opcion == "5":
            buscar_videojuego(videojuegos_inventario)
        
        elif opcion == "6":
            print(f"¡Hasta luego {nombre_usuario}! Cerrando The Save Point...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# nuevo_videojuego = capturar_datos()
# videojuegos_inventario.append(nuevo_videojuego)

# print(f"El videojuego {nuevo_videojuego['Titulo']} ha sido guardado!")
