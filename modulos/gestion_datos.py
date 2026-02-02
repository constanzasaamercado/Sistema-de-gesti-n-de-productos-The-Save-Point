# Definición de tuplas.

GENEROS = ("Acción", "Aventura", "RPG", "Estrategia", "Deportes", "Carreras", "Lucha", "Plataformas")

# Lista de diccionarios para almacenar los datos de los productos.

videojuegos_inventario = [
    {"Titulo": "Super Mario Bros.", "Genero": "Plataformas", "Anio":"1985", "Plataforma": "NES", "Editor": "Nintendo", "Formato": "Físico", "Precio": 15.000, "Stock": 5},
    {"Titulo": "Mario Kart Wii", "Genero": "Carreras", "Anio":"2008", "Plataforma": "Wii", "Editor": "Nintendo", "Formato": "Físico", "Precio": 25.000, "Stock": 3},
    {"Titulo": "Wii Sports Resort", "Genero": "Deportes", "Anio":"2009", "Plataforma": "Wii", "Editor": "Nintendo", "Formato": "Físico", "Precio": 20.000, "Stock": 2},
    {"Titulo": "Detective Pikachu", "Genero": "Aventura", "Anio":"2019", "Plataforma": "Switch", "Editor": "Nintendo", "Formato": "Digital", "Precio": 35.000, "Stock": 4},
    {"Titulo": "Mortal kombat 11", "Genero": "Lucha", "Anio":"2019", "Plataforma": "Pc", "Editor": "NetherRealm Studios", "Formato": "Digital", "Precio": 35.000, "Stock": 15},
    {"Titulo": "Alice Madness Returns", "Genero": "Acción", "Anio":"2011", "Plataforma": "Pc", "Editor": "Spicy Horse", "Formato": "Digital", "Precio": 10.000, "Stock": 8},
    {"Titulo": "The Witcher 3: Wild Hunt", "Genero": "RPG", "Anio":"2015", "Plataforma": "Pc", "Editor": "CD Projekt", "Formato": "Digital", "Precio": 40.000, "Stock": 12},
    {"Titulo": "Let's go Pikachu", "Genero": "Aventura", "Anio":"2018", "Plataforma": "Switch", "Editor": "Nintendo", "Formato": "Físico", "Precio": 30.000, "Stock": 15},
    {"Titulo": "Let's go Eevee", "Genero": "Aventura", "Anio":"2018", "Plataforma": "Switch", "Editor": "Nintendo", "Formato": "Físico", "Precio": 30.000, "Stock": 10},
    {"Titulo": "Untitled Goose Game", "Genero": "Aventura", "Anio":"2019", "Plataforma": "Pc", "Editor": "House House", "Formato": "Digital", "Precio": 15.000, "Stock": 20},
    {"Titulo": "God of War", "Genero": "Acción", "Anio":"2018", "Plataforma": "Pc", "Editor": "Santa Monica Studio", "Formato": "Digital", "Precio": 45.000, "Stock": 7},
    {"Titulo": "Mario kart 8 Deluxe", "Genero": "Carreras", "Anio":"2017", "Plataforma": "Switch", "Editor": "Nintendo", "Formato": "Físico", "Precio": 40.000, "Stock": 9}, 
] 

# Carga de datos e ingreso y de inventario se manejarán en este módulo.

def capturar_datos():
    print("\n--- Registro de Nuevo Videojuego ---")
    titulo = input("Título: ").strip().title()

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
# Valores por defecto si no se piden
    return {
        "Titulo": titulo, "Genero": genero, "Precio": precio, "Stock": stock,
        "Anio": "N/A", "Plataforma": "N/A" 
    }

# Visualización de existencias de videojuegos.

def mostrar_inventario(lista):
    if not lista:
        print("\n⚠️ El inventario está vacío.")
        return
    print("\n" + "="*60)
    print(f"{'INVENTARIO COMPLETO':^60}")
    print("="*60)
    for juego in lista:
        print(f"🎮 Título: {juego['Titulo']:<25} | Stock: {juego['Stock']}")
        print(f"   Género: {juego['Genero']:<25} | Precio: ${juego['Precio']}")
        print("-" * 60)

# Busqueda de existencias por nombre

def buscar_videojuego(lista):
    termino = input("\n🔍 Nombre a buscar: ").strip().lower()
    encontrado = False
    for juego in lista:
        if termino in juego['Titulo'].lower():
            print(f"✅ Encontrado: {juego['Titulo']} | Stock: {juego['Stock']} | Precio: ${juego['Precio']}")
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
            lista.remove(juego)
            print(f"✅ '{juego['Titulo']}' eliminado del sistema.")
            return
    print("❌ Juego no encontrado.")