# Diccionario para almacenar los datos de los productos

videojuegos_inventario =[
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

# Carga de datos, ingreso y actualización de inventario se manejarán en este módulo.


def capturar_datos():
    print("Ingrese los datos del nuevo videojuego:")

    Titulo = input("Titulo: ")
    Genero = input("Género: ")
    Anio = input("Anio: ")
    Plataforma = input("Plataforma: ")
    Editor = input("Editor: ")
    Formato = input("Formato (Físico/Digital): ")
    Precio = float(input("Precio: "))
    Stock = int(input("Stock inicial: "))

    return {
        "Titulo": Titulo,"Genero": Genero,"Anio": Anio,
        "Plataforma": Plataforma,"Editor": Editor,"Formato": Formato,
        "Precio": Precio,"Stock": Stock
    }

# Generar un nuevo ID para el videojuego
# nuevo_id = str(int(max(videojuegos_inventario.keys())) + 1).zfill(3)

# Mostrar la existencia de inventario
def mostrar_inventario(lista):

    if not lista:
        print("\n El inventario esta vacío actualmente.")
        return
    
    print("\n"+("="*60))
    print(f"{"INVENTARIO DE THE SAVE POINT":^60}") 
    print("="*60)

    for Videojuego in lista:
        print(f"Titulo:{Videojuego["Titulo"]:<25} | Stock: {Videojuego["Stock"]}")
        print(f"Genero: {Videojuego["Genero"]:<25} | Precio: ${Videojuego["Precio"]}")
        print("-" * 60)

def eliminar_videojuego(lista):
    
    nombre_a_eliminar = input("\n Ingrese el nombre del videojuego a eliminar: ").strip().lower()
    encontrado = False

    for videojuego_id in lista:
        if videojuego["Titulo"].lower() == nombre_a_eliminar:
            lista.remove(videojuego)
            print(f"El juego '{videojuego['Titulo']}' ha sido eliminado del inventario.")
            encontrado = True
            break
    if not encontrado:
        print(f"No se encontró el juego '{nombre_a_eliminar}' en el inventario.")