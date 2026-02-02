# Importar funciones

from modulos.gestion_datos import (
    capturar_datos, 
    mostrar_inventario, 
    eliminar_videojuego, 
    buscar_videojuego,
    modificar_videojuego,
    videojuegos_inventario 
)

# Bienvenida al sistema de gestion de productos.

print("¡BIENVENIDO A THE SAVE POINT!")
nombre_usuario = input("Usuario: ")

# Menu principal del sistema

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Ingresar datos | 2. Modificar datos| 3. Eliminar productos | 4. Visualizar inventario | 5. Buscar videojuego | 6. Salir")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        nuevo = capturar_datos()
        videojuegos_inventario.append(nuevo)
        print(f"✅ {nuevo['Titulo']} guardado!")
    
    elif opcion == "2":
       
        modificar_videojuego(videojuegos_inventario)

    elif opcion == "3":
        eliminar_videojuego(videojuegos_inventario)

    elif opcion == "4":
        mostrar_inventario(videojuegos_inventario)
        
    elif opcion == "5":
        buscar_videojuego(videojuegos_inventario)
        
    elif opcion == "6":
        print(f"¡Hasta luego {nombre_usuario}!")
        break