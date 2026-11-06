# ==============================================================================
# INFORMÁTICA II — 2º BACHILLERATO | IES Fco. Grande Covián
# Ejercicio: Copia de diccionarios (.copy()) y salida tabulada mediante .get()
# ==============================================================================

# Diccionario principal original (Ejercicio 1)
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
# 1. CREACIÓN DE LA COPIA DEL DICCIONARIO (.copy())
# ------------------------------------------------------------------------------
# El método .copy() duplicará la estructura del diccionario 'titulares'
# y guardará la nueva copia en la variable 'plantilla'.
# Esto permite modificar 'plantilla' en el futuro sin alterar los datos originales de 'titulares'.
plantilla = titulares.copy()

# ------------------------------------------------------------------------------
# 2. IMPRESIÓN TABULADA Y ORDENADA POR DORSAL (FORMATO EJERCICIO 2)
# ------------------------------------------------------------------------------
# Impresión de la cabecera tabulada mediante f-strings
print(f"{'Nº':<4} | {'POS':<4} | {'NOMBRE'}")
print("=" * 40)

# Bucle secuencial de 1 a 99 para recorrer los números de dorsal en orden ascendente
for dorsal in range(1, 100):
    # Consultamos el diccionario 'plantilla' usando el método seguro .get()
    # Si el dorsal existe, nos devuelve su diccionario interno; si no existe, devuelve None sin fallar.
    jugador = plantilla.get(dorsal)

    # Si se ha encontrado un jugador registrado para ese dorsal
    if jugador is not None:
        # Lectura de la posición y nombre con .get() por seguridad
        posicion = jugador.get("posicion", "---")
        nombre = jugador.get("nombre", "Desconocido")

        # Asignación de la etiqueta de capitán mediante un condicional simple
        es_capitan = " (C)" if jugador.get("capitan", False) else ""

        # Impresión de la fila con alineación tabulada a la izquierda (<)
        print(f"{dorsal:<4} | {posicion:<4} -> {nombre}{es_capitan}")