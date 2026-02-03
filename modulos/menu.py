# Importar funciones

from modulos.funciones_utiles import formatear_pesos, limpiar_pantalla
from modulos.validaciones import validar_entero, validar_float, verificar_credenciales
from modulos.gestion_datos import GENEROS, USUARIOS_SISTEMA, videojuegos_inventario

# Mensaje de bienvenida

def mostrar_bienvenida(usuario):
    # limpiar_pantalla()
    print("=" * 50)
    print(f"{'SISTEMA DE GESTIÓN DE THE SAVE POINT':^50}")
    print("=" * 50)
    print(f"Sesión iniciada como: {usuario.upper()}")
    print("-" * 50)

# Ingreso al sistema por usuario

def login_sistema():
    # limpiar_pantalla()
    print("\n" + "*"*30)
    print(f"{'ACCESO AL SISTEMA':^30}")
    print("*"*30)

    intentos = 3

    try:
        while intentos > 0:
            usuario = input("👤 Usuario: ").strip()
            clave = input("🔑 Contraseña: ").strip()
            
            if usuario in USUARIOS_SISTEMA and USUARIOS_SISTEMA[usuario] == clave:
                print(f"\n✅ ¡Acceso concedido! Bienvenido, {usuario}.")
                return True, usuario
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"❌ Credenciales incorrectas. Intentos restantes: {intentos}")
                else:
                    print("❌ Acceso denegado. Ha excedido el límite de intentos.")
                    return False, ""
    except KeyboardInterrupt:
        print("\n\n❌ Acceso cancelado por el usuario.")
        return False, ""

# Carga de datos e ingreso y de inventario se manejarán en este módulo.

def capturar_datos():
    print("\n--- Registro de Nuevo Videojuego ---")
    titulo = input("Título: ").strip().title()
    anio = input("Año: ").strip()
    plataforma = input("Plataforma: ").strip().title()
    editor = input("Editor: ").strip().title()
    formato = input("Formato (Físico/Digital): ").strip().title()
    print(f"Géneros permitidos: {GENEROS}")
    genero = input("Elija el Género: ").strip().capitalize()

    if genero not in GENEROS:
        print(f"⚠️ Nota: '{genero}' no es un género estándar, pero se guardará igual.")

    while True:
        try:
            precio = float(input("Precio: "))
            stock = int(input("Stock inicial: "))
            break
        except ValueError:
            print("❌ Error: Ingrese valores numéricos válidos para Precio y Stock.")

    nuevo_juego = {
        "Titulo": titulo, "Genero": genero, "Precio": precio, "Stock": stock,
        "Año": anio, "Plataforma": plataforma, "Editor": editor, "Formato": formato
    }
    videojuegos_inventario.append(nuevo_juego)
    print("✅ Registrado con éxito.")
    return nuevo_juego 

   
# Visualización de existencias de videojuegos.

# Función UNIFICADA: Maneja el sub-menú de visualización y búsqueda.

def menu_visualizacion(lista):
    while True:
        print("\n--- OPCIONES DE VISUALIZACIÓN ---")
        print("1. Ver todo el inventario")
        print("2. Buscar un videojuego específico")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione: ")
        if opcion == "1":
            mostrar_inventario(lista)
        elif opcion == "2":
            buscar_videojuego(lista)
        elif opcion == "3":
            break
        else:
            print("⚠️ Opción inválida.")

def mostrar_inventario(lista):
    if not lista:
        print("\n⚠️ El inventario está vacío.")
        return
    print("\n" + "="*60)
    print(f"{'INVENTARIO COMPLETO':^60}")
    print("="*60)
    for juego in lista:
        precio_clp = formatear_pesos(juego['Precio'])
        print(f"🎮 Título: {juego['Titulo']:<25} | Stock: {juego['Stock']}")
        print(f"   Género: {juego['Genero']:<25} | Precio: {precio_clp}")
        print("-" * 60)

# Busqueda de existencias por nombre

def buscar_videojuego(lista):
    termino = input("\n🔍 Nombre a buscar: ").strip().lower()
    encontrado = False
    for juego in lista:
        if termino in juego['Titulo'].lower():
            precio_clp = formatear_pesos(juego['Precio'])
            print(f"✅ Encontrado: {juego['Titulo']} | Stock: {juego['Stock']} | Precio: {precio_clp}")
            encontrado = True
    if not encontrado:
        print(f"❌ No se encontró: '{termino}'")

# Actualización de inventario se manejará en este módulo.        

def modificar_videojuego(lista):
    """Busca un juego y permite elegir qué campo actualizar."""
    if not lista:
        print("\n⚠️ El inventario está vacío.")
        return

    nombre_buscado = input("\n📝 Ingrese el nombre del juego a modificar: ").strip().lower()
    encontrado = False

    for juego in lista:
        if juego['Titulo'].lower() == nombre_buscado:
            encontrado = True
            print(f"\n🎮 Juego encontrado: {juego['Titulo']}")
            print("¿Qué desea modificar?")
            print("1. Precio")
            print("2. Stock")
            print("3. Cancelar")
            
            opcion_mod = input("Seleccione una opción: ")

            if opcion_mod == "1":
                nuevo_precio = float(input(f"Precio actual: ${juego['Precio']}. Nuevo precio: "))
                juego['Precio'] = nuevo_precio
                print("✅ Precio actualizado con éxito.")
            
            elif opcion_mod == "2":
                nuevo_stock = int(input(f"Stock actual: {juego['Stock']}. Nuevo stock: "))
                juego['Stock'] = nuevo_stock
                print("✅ Stock actualizado con éxito.")
            
            elif opcion_mod == "3":
                print("Operación cancelada.")
            
            else:
                print("⚠️ Opción no válida.")
            break
    
    if not encontrado:
        print(f"❌ No se encontró el juego: '{nombre_buscado}'")

# Eliminación de videojuegos del inventario

def eliminar_videojuego(lista):
    nombre = input("\n🗑️ Nombre del juego a eliminar: ").strip().lower()
    for juego in lista:
        if juego['Titulo'].lower() == nombre:
            confirmacion = input(f"¿Está seguro que desea eliminar '{juego['Titulo']}'? (Si/No): ").strip().upper()
            if confirmacion == "Si":
                lista.remove(juego)
                print(f"✅ '{juego['Titulo']}' eliminado del sistema.")
            else:
                print("❌ Eliminación cancelada.")
            return
    print("❌ Juego no encontrado.")