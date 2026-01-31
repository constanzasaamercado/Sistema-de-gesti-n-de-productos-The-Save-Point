# Diccionario para almacenar los datos de los productos

videojuegos_inventario ={
    "001": {"Titulo": "Super Mario Bros.", "Genero": "Plataformas", "Anio":"1985", "Plataforma": "NES", "Editor": "Nintendo", "Formato": "Físico", "Precio": 15.000, "Stock": 5},
    "002": {"Titulo": "Mario Kart Wii", "Genero": "Carreras", "Anio":"2008", "Plataforma": "Wii", "Editor": "Nintendo", "Formato": "Físico", "Precio": 25.000, "Stock": 3},
    "003": {"Titulo": "Wii Sports Resort", "Genero": "Deportes", "Anio":"2009", "Plataforma": "Wii", "Editor": "Nintendo", "Formato": "Físico", "Precio": 20.000, "Stock": 2},
    "004": {"Titulo": "Detective Pikachu", "Genero": "Aventura", "Anio":"2019", "Plataforma": "Switch", "Editor": "Nintendo", "Formato": "Digital", "Precio": 35.000, "Stock": 4},
    "005": {"Titulo": "Mortal kombat 11", "Genero": "Lucha", "Anio":"2019", "Plataforma": "Pc", "Editor": "NetherRealm Studios", "Formato": "Digital", "Precio": 35.000, "Stock": 15},
    "006": {"Titulo": "Alice Madness Returns", "Genero": "Acción", "Anio":"2011", "Plataforma": "Pc", "Editor": "Spicy Horse", "Formato": "Digital", "Precio": 10.000, "Stock": 8},
    "007": {"Titulo": "The Witcher 3: Wild Hunt", "Genero": "RPG", "Anio":"2015", "Plataforma": "Pc", "Editor": "CD Projekt", "Formato": "Digital", "Precio": 40.000, "Stock": 12},
    "008": {"Titulo": "Let's go Pikachu", "Genero": "Aventura", "Anio":"2018", "Plataforma": "Switch", "Editor": "Nintendo", "Formato": "Físico", "Precio": 30.000, "Stock": 15},
    "009": {"Titulo": "Let's go Eevee", "Genero": "Aventura", "Anio":"2018", "Plataforma": "Switch", "Editor": "Nintendo", "Formato": "Físico", "Precio": 30.000, "Stock": 10},
    "010": {"Titulo": "Untitled Goose Game", "Genero": "Aventura", "Anio":"2019", "Plataforma": "Pc", "Editor": "House House", "Formato": "Digital", "Precio": 15.000, "Stock": 20},
    "011": {"Titulo": "God of War", "Genero": "Acción", "Anio":"2018", "Plataforma": "Pc", "Editor": "Santa Monica Studio", "Formato": "Digital", "Precio": 45.000, "Stock": 7},
    "012": {"Titulo": "Mario kart 8 Deluxe", "Genero": "Carreras", "Anio":"2017", "Plataforma": "Switch", "Editor": "Nintendo", "Formato": "Físico", "Precio": 40.000, "Stock": 9}, 
}

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
        "Titulo": Titulo,
        "Genero": Genero,
        "Anio": Anio,
        "Plataforma": Plataforma,
        "Editor": Editor,
        "Formato": Formato,
        "Precio": Precio,
        "Stock": Stock
    }

# Generar un nuevo ID para el videojuego
nuevo_id = str(int(max(videojuegos_inventario.keys())) + 1).zfill(3)

# Mostrar la existencia de inventario
def mostrar_inventario(videojuegos_inventario):

    if not videojuegos_inventario:
        print("\n El inventario esta vacío actualmente.")
        return
    
    print("\n"+("="*60))
    print(f"{"INVENTARIO DE THE SAVE POINT":^60}") 
    print("="*60)

    for Videojuego in videojuegos_inventario:
    
        print(f" Videojuego ID: {Videojuego}")
        print(f"Genero: {videojuegos_inventario[Videojuego]['Genero']}")

def eliminar_videojuego(videojuegos_inventario):
    
    nombre_a_eliminar = input("\n Ingrese el nombre del videojuego a eliminar: ").strip().lower()
    encontrado = False

    for videojuego_id, videojuego in videojuegos_inventario.items():
        if videojuego["Titulo"].lower() == nombre_a_eliminar:
            del videojuegos_inventario[videojuego_id]
            print(f"El juego '{videojuego['Titulo']}' ha sido eliminado del inventario.")
            encontrado = True
            break
    if not encontrado:
        print(f"No se encontró el juego '{nombre_a_eliminar}' en el inventario.")