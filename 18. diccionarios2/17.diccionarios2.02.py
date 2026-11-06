# ==============================================================================
# INFORMÁTICA II — 2º BACHILLERATO | IES Fco. Grande Covián
# Ejercicio: Recorrido y salida tabulada mediante .items() y formateo de cadenas
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. ESTRUCTURA DE DATOS: DICCIONARIO ANIDADO
# ------------------------------------------------------------------------------
# El diccionario principal se llama 'titulares'.
# - CLAVE EXTERNA: Número de dorsal (tipo entero 'int', ej: 23, 12, 16...).
# - VALOR ASOCIADO: Un segundo diccionario (anidado) con 3 claves fijas[cite: 1, 2]:
#     * "posicion": Tipo 'str' (demarcación en el campo: POR, DEF, MED, DEL).
#     * "nombre"  : Tipo 'str' (nombre y apellidos del jugador).
#     * "capitan" : Tipo 'bool' (True si es el capitán, False en caso contrario)[cite: 1, 2].

titulares = {
    23: {"posicion": "POR", "nombre": "Unai Simón", "capitan": False},
    12: {"posicion": "DEF", "nombre": "Pedro Porro", "capitan": False},
    22: {"posicion": "DEF", "nombre": "Pau Cubarsí", "capitan": False},
    14: {"posicion": "DEF", "nombre": "Aymeric Laporte", "capitan": False},
    24: {"posicion": "DEF", "nombre": "Marc Cucurella", "capitan": False},
    16: {"posicion": "MED", "nombre": "Rodri Hernández", "capitan": True},
    10: {"posicion": "MED", "nombre": "Dani Olmo", "capitan": False},
    8: {"posicion": "MED", "nombre": "Fabián Ruiz", "capitan": False},
    19: {"posicion": "DEL", "nombre": "Lamine Yamal", "capitan": False},
    21: {"posicion": "DEL", "nombre": "Mikel Oyarzabal", "capitan": False},
    15: {"posicion": "DEL", "nombre": "Álex Baena", "capitan": False},
}

# ------------------------------------------------------------------------------
# 2. IMPRESIÓN DE LA CABECERA DE LA TABLA
# ------------------------------------------------------------------------------
# Formateo de cabecera con f-strings y alineación:
# - {'Nº':^4}  -> Imprime el texto 'Nº' CENTRADO (^) en una columna de 4 caracteres.
# - {'POS':<4} -> Imprime 'POS' ALINEADO A LA IZQUIERDA (<) en 4 caracteres.
# - {'NOMBRE'} -> Imprime 'NOMBRE' con su ancho natural (última columna)[cite: 1].
print(f"{'Nº':^4} | {'POS':<4} | {'NOMBRE'}")

# Operador de repetición de cadenas:
# Multiplica la cadena "=" por 40 para trazar la línea divisoria horizontal.
print("=" * 40)

# ------------------------------------------------------------------------------
# 3. RECORRIDO DEL DICCIONARIO CON BUCLE FOR Y MÉTODO .items()
# ------------------------------------------------------------------------------
# El método .items() devuelve en cada iteración una tupla (clave, valor)[cite: 1]:
# - 'dorsal' -> Asimila la clave externa (el número entero del dorsal)[cite: 1].
# - 'dato'   -> Asimila el valor (el diccionario interno con la ficha del jugador)[cite: 1].
for dorsal, dato in titulares.items():

    # Acceso a los campos internos mediante sus claves entre corchetes [][cite: 1]
    posicion = dato["posicion"]  # Obtiene la demarcación ("POR", "DEF", etc.)[cite: 1]
    nombre = dato["nombre"]  # Obtiene el nombre completo del jugador[cite: 1]

    # Evaluación del estado de capitán:
    # Se evalúa la clave "capitan" (que almacena un valor booleano True o False)[cite: 1, 2]
    if dato["capitan"] == True:
        es_capitan = "(C)"  # Asigna la marca distintiva para el capitán
    else:
        es_capitan = ""  # Asigna una cadena vacía si no es capitán

    # Salida por consola formateada mediante f-string:
    # - {dorsal:^5}   -> Imprime el número de dorsal CENTRADO en 5 espacios[cite: 1].
    # - |             -> Dibuja la barra separadora.
    # - {posicion:^6} -> Imprime la posición CENTRADA en 6 espacios[cite: 1].
    # - ->            -> Muestra la flecha separadora hacia el nombre.
    # - {nombre}      -> Muestra el nombre completo del jugador.
    # - {es_capitan}  -> Añade "(C)" si es capitán o nada si es vacía.
    print(f"{dorsal:^5}|{posicion:^6}-> {nombre}{es_capitan}")
