# ==============================================================================
# INFORMÁTICA II — 2º BACHILLERATO | IES Fco. Grande Covián
# Ejercicio: Recorrido y salida tabulada mediante .get() y ordenación de dorsales
# ==============================================================================

# Diccionario principal de titulares
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
# CONTEO Y PRESENTACIÓN DEL TOTAL DE JUGADORES (CÁLCULO DINÁMICO)
# ------------------------------------------------------------------------------

# 1. Función len():
#    Calcula el número total de elementos (pares clave-valor) almacenados 
#    en el diccionario 'titulares' (en este caso, 11).
# 2. Variable 'total_jugadores':
#    Guarda el entero devuelto por len() para poder reutilizarlo posteriormente.
total_jugadores = len(titulares)

# 3. Salida por pantalla con f-string y secuencias de escape:
#    - f"..."          -> Cadena formateada (f-string) para intercalar variables entre llaves {}.
#    - \n              -> Secuencia de escape de salto de línea (añade una línea en blanco).
#    - {total_jugadores} -> Sustituye la variable por su valor numérico (11).
print(f"\nIniciaron el partido {total_jugadores} jugadores.\n")

# ------------------------------------------------------------------------------
# CABECERA TABULADA
# ------------------------------------------------------------------------------
print(f"{'Nº':<4} | {'POS':<4} | {'NOMBRE'}")
print("=" * 40)

# ------------------------------------------------------------------------------
# Bucle en rango 1 a 99 usando .get()
# Como el menor dorsal es 1 y el mayor tiene 2 cifras (máximo 99),
# comprobamos cada número de dorsal en orden secuencial (range(1, 100)).
# Si el dorsal no existe en el diccionario, .get() devuelve None y no da error.
# ------------------------------------------------------------------------------
for dorsal in range(1, 100):
    # .get(dorsal) busca la clave; si no la encuentra, devuelve None por defecto
    jugador = titulares.get(dorsal)

    # Si la búsqueda devuelve datos (distinto de None), se imprime la fila
    if jugador is not None:
        # Lectura segura de los campos internos mediante .get()
        posicion = jugador.get("posicion", "---")
        nombre = jugador.get("nombre", "Desconocido")

        # Condicional para añadir el distintivo de capitán
        es_capitan = " (C)" if jugador.get("capitan", False) else ""

        # Salida formateada con alineación de columnas mediante f-strings
        print(f"{dorsal:<4} | {posicion:<4} -> {nombre}{es_capitan}")
