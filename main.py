# Importar funciones

from modulos.menu import login_sistema, mostrar_bienvenida, capturar_datos, menu_visualizacion, modificar_videojuego, eliminar_videojuego
from modulos.gestion_datos import videojuegos_inventario

# Ingreso al sistema con usuario y contraseña

acceso_permitido, nombre_usuario = login_sistema()

# Menu principal del sistema
if acceso_permitido: 
    mostrar_bienvenida(nombre_usuario) # Bienvenida al sistema de gestion de productos.
    while True:
        try:
            print("\n--- MENU PRINCIPAL ---")
            print("1. Ingresar datos | 2. Modificar datos | 3. Eliminar productos | 4. Visualización y Búsqueda de existencias | 5. Salir")
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                capturar_datos()
        
            elif opcion == "2":
                modificar_videojuego(videojuegos_inventario)

            elif opcion == "3":
                eliminar_videojuego(videojuegos_inventario)

            elif opcion == "4":
                menu_visualizacion(videojuegos_inventario)
               
            elif opcion == "5":
                print(f"¡Hasta luego {nombre_usuario.upper()}!")
                print("Saliendo del sistema...")
                break
            
            else:
                print("⚠️ Opción no válida. Intente de nuevo.")
        
        except KeyboardInterrupt:
            print("\n\n❌ Operación cancelada por el usuario.")
            print(f"¡Hasta luego {nombre_usuario.upper()}!")
            break