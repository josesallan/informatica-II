# ==============================================================================
# INFORMÁTICA II — 2º BACHILLERATO | IES Fco. Grande Covián
# Ejercicio: Copia de diccionarios (.copy()) y Fusión de Plantilla (.update())
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. DICCIONARIO DE JUGADORES TITULARES
# ------------------------------------------------------------------------------
# - Clave: Dorsal (int)
# - Valor: Diccionario anidado con "posicion", "nombre" y "capitan"
titulares = {
    23: {"posicion": "POR", "nombre": "Unai Simón", "capitan": False},
    12: {"posicion": "DEF", "nombre": "Pedro Porro", "capitan": False},
    22: {"posicion": "DEF", "nombre": "Pau Cubarsí", "capitan": False},
    14: {"posicion": "DEF", "nombre": "Aymeric Laporte", "capitan": False},
    24: {"posicion": "DEF", "nombre": "Marc Cucurella", "capitan": False},
    16: {"posicion": "MED", "nombre": "Rodri Hernández", "capitan": True},
    10: {"posicion": "MED", "nombre": "Dani Olmo", "capitan": False},
    8:  {"posicion": "MED", "nombre": "Fabián Ruiz", "capitan": False},
    19: {"posicion": "DEL", "nombre": "Lamine Yamal", "capitan": False},
    21: {"posicion": "DEL", "nombre": "Mikel Oyarzabal", "capitan": False},
    15: {"posicion": "DEL", "nombre": "Álex Baena", "capitan": False}
}

# ------------------------------------------------------------------------------
# 2. DICCIONARIO DE JUGADORES SUPLENTES
# ------------------------------------------------------------------------------
# - Clave: Dorsal (int)
# - Valor: Diccionario anidado con "posicion" y "nombre"
suplentes = {
    1:  {"posicion": "POR", "nombre": "David Raya"},
    2:  {"posicion": "DEF", "nombre": "Dani Carvajal"},
    3:  {"posicion": "DEF", "nombre": "Robin Le Normand"},
    5:  {"posicion": "DEF", "nombre": "Daniel Vivian"},
    6:  {"posicion": "MED", "nombre": "Mikel Merino"},
    7:  {"posicion": "DEL", "nombre": "Álvaro Morata"},
    9:  {"posicion": "DEL", "nombre": "Joselu"},
    11: {"posicion": "DEL", "nombre": "Ferran Torres"},
    17: {"posicion": "DEL", "nombre": "Nico Williams"},
    18: {"posicion": "MED", "nombre": "Martín Zubimendi"},
    20: {"posicion": "MED", "nombre": "Pedri"}
}

# ------------------------------------------------------------------------------
# 3. CREACIÓN DE COPIA (.copy()) Y FUSIÓN (.update())
# ------------------------------------------------------------------------------

# Paso 1: Duplicamos el diccionario 'titulares' en una nueva variable llamada 'plantilla'.
# Usamos .copy() para crear un nuevo objeto independiente en memoria.
plantilla = titulares.copy()

# Paso 2: Añadimos todos los elementos del diccionario 'suplentes' a 'plantilla'.
# El método .update() incorpora pares clave-valor de un diccionario a otro.
plantilla.update(suplentes)


# ------------------------------------------------------------------------------
# 4. SALIDA TABULADA DE LA PLANTILLA COMPLETA (22 JUGADORES)
# ------------------------------------------------------------------------------
print("=== PLANTILLA COMPLETA CONVOCADA (TITULARES + SUPLENTES) ===")
print(f"{'Nº':<4} | {'POS':<4} | {'NOMBRE'}")
print("=" * 40)

# Bucle del 1 al 99 para recorrer los dorsales ordenados de menor a mayor
for dorsal in range(1, 100):
    # .get(dorsal) busca el número en el diccionario 'plantilla'[cite: 1, 2].
    # Si no existe, devuelve None y el condicional lo ignora sin dar error (KeyError)[cite: 1, 2].
    jugador = plantilla.get(dorsal)

    if jugador is not None:
        posicion = jugador.get("posicion", "---")
        nombre = jugador.get("nombre", "Desconocido")
        
        # .get("capitan", False) devuelve el valor de la clave 'capitan' si existe,
        # o False por defecto si la clave no está definida (como en los suplentes)[cite: 1, 2].
        es_capitan = " (C)" if jugador.get("capitan", False) else ""
        
        # Salida por consola formateada mediante f-strings
        print(f"{dorsal:<4} | {posicion:<4} -> {nombre}{es_capitan}")

# Conteo automático de elementos con len()[cite: 1, 2]
total_convocados = len(plantilla)
print(f"\nLa convocatoria total consta de {total_convocados} jugadores.\n")