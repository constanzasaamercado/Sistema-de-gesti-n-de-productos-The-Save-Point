# Asegura que el usuario ingrese un número entero (para Stock).

def validar_entero(mensaje):

    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0: raise ValueError
            return valor
        except ValueError:
            print("❌ Error: Ingrese un número entero positivo.")

# Asegura que el usuario ingrese un número decimal (para Precio).

def validar_float(mensaje):

    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0: raise ValueError
            return valor
        except ValueError:
            print("❌ Error: Ingrese un valor numérico válido.")

# Valida si el usuario y clave existen en la base de datos.

def verificar_credenciales(usuario, clave, base_usuarios):

    if usuario in base_usuarios and base_usuarios[usuario] == clave:
        return True
    return False