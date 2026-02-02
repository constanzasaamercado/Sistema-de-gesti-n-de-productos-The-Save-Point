# Importar funciones

from modulos.gestion_datos import (
    capturar_datos, 
    eliminar_videojuego, 
    modificar_videojuego,
    login_sistema,
    menu_visualizacion,
    videojuegos_inventario
)

# Bienvenida al sistema de gestion de productos.

print("¡BIENVENIDO A THE SAVE POINT!")
nombre_usuario = input("Usuario: ")

# Ingreso al sistema con usurio y contraseña

acceso_permitido, nombre_usuario = login_sistema()

# Menu principal del sistema

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Ingresar datos | 2. Modificar datos| 3. Eliminar productos | 4. Visualización y Búsqueda de existencias | 5. Salir")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        nuevo = capturar_datos()
        videojuegos_inventario.append(nuevo)
        print(f"✅ {nuevo['Titulo']} guardado!")
    
    elif opcion == "2":
       
        modificar_videojuego(videojuegos_inventario)

    elif opcion == "3":
        eliminar_videojuego(videojuegos_inventario)

    if opcion == "4":
        menu_visualizacion(videojuegos_inventario)
               
    elif opcion == "5":
        print(f"¡Hasta luego {nombre_usuario}!")
        break