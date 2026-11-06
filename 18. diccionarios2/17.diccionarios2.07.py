# ==============================================================================
# INFORMÁTICA II — 2º BACHILLERATO | IES Fco. Grande Covián
# Ejercicio: Diccionarios de Titulares y Suplentes con Salida Tabulada (.get())
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. DICCIONARIO DE JUGADORES TITULARES (EJERCICIO 1)
# ------------------------------------------------------------------------------
# - Clave (índice externo): Número de dorsal (tipo entero 'int').
# - Valor: Diccionario interno con "posicion", "nombre" y "capitan".

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
# 2. DICCIONARIO DE JUGADORES SUPLENTES (NUEVO DICCIONARIO)
# ------------------------------------------------------------------------------
# - Clave (índice externo): Número de dorsal (tipo entero 'int').
# - Valor: Diccionario interno con "posicion" y "nombre".

suplentes = {
    1: {"posicion": "POR", "nombre": "David Raya"},
    2: {"posicion": "DEF", "nombre": "Dani Carvajal"},
    3: {"posicion": "DEF", "nombre": "Robin Le Normand"},
    5: {"posicion": "DEF", "nombre": "Daniel Vivian"},
    6: {"posicion": "MED", "nombre": "Mikel Merino"},
    7: {"posicion": "DEL", "nombre": "Álvaro Morata"},
    9: {"posicion": "DEL", "nombre": "Joselu"},
    11: {"posicion": "DEL", "nombre": "Ferran Torres"},
    17: {"posicion": "DEL", "nombre": "Nico Williams"},
    18: {"posicion": "MED", "nombre": "Martín Zubimendi"},
    20: {"posicion": "MED", "nombre": "Pedri"},
}

# ------------------------------------------------------------------------------
# 3. IMPRESIÓN DE TITULARES (FORMATO EJERCICIOS 2 Y 3)
# ------------------------------------------------------------------------------
print("=== ALINEACIÓN TITULAR ===")
print(f"{'Nº':<4} | {'POS':<4} | {'NOMBRE'}")
print("=" * 40)

# Recorrido de dorsales (1 a 99) de menor a mayor mediante .get()
for dorsal in range(1, 100):
    jugador = titulares.get(
        dorsal
    )  # Si existe el dorsal devuelve el diccionario; si no, None[cite: 1]
    if jugador is not None:
        posicion = jugador.get("posicion", "---")
        nombre = jugador.get("nombre", "Desconocido")
        es_capitan = " (C)" if jugador.get("capitan", False) else ""
        print(f"{dorsal:<4} | {posicion:<4} -> {nombre}{es_capitan}")

# Conteo dinámico con len() (Ejercicio 3)
total_titulares = len(titulares)
print(f"\nIniciaron el partido {total_titulares} jugadores.")

# ------------------------------------------------------------------------------
# 4. IMPRESIÓN DE SUPLENTES (FORMATO EJERCICIOS 2 Y 6)
# ------------------------------------------------------------------------------
print("\n" + "=" * 40)
print("=== JUGADORES SUPLENTES ===")
print(f"{'Nº':<4} | {'POS':<4} | {'NOMBRE'}")
print("=" * 40)

# Recorrido de dorsales (1 a 99) de menor a mayor mediante .get() en el diccionario 'suplentes'
for dorsal in range(1, 100):
    jugador = suplentes.get(dorsal)
    if jugador is not None:
        posicion = jugador.get("posicion", "---")
        nombre = jugador.get("nombre", "Desconocido")
        print(f"{dorsal:<4} | {posicion:<4} -> {nombre}")

# Conteo dinámico de suplentes con len()
total_suplentes = len(suplentes)
print(f"\nComenzaron en el banquillo {total_suplentes} jugadores.\n")
