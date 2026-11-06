# ==============================================================================
# INFORMÁTICA II — 2º BACHILLERATO | IES Fco. Grande Covián
# Ejercicio: Registro de 6 Sustituciones usando del y .setdefault()
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. DICCIONARIO DE ALINEACIÓN TITULAR INICIAL
# ------------------------------------------------------------------------------
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
# 2. CREACIÓN DE LA COPIA 'FINAL' (.copy())
# ------------------------------------------------------------------------------
# Duplicamos 'titulares' para no alterar los datos de la alineación inicial.
final = titulares.copy()

# ------------------------------------------------------------------------------
# 3. EJECUCIÓN DE LAS 6 SUSTITUCIONES CON del Y .setdefault()
# ------------------------------------------------------------------------------

# --- CAMBIOS MINUTO 62' ---
# Salen: Fabián Ruiz (8) y Mikel Oyarzabal (21) -> Eliminación con 'del'
del final[8]
del final[21]
# Entran: Ferran Torres (7) y Pedri (20) -> Inserción con '.setdefault()'[cite: 1]
final.setdefault(7, {"posicion": "DEL", "nombre": "Ferran Torres", "capitan": False})
final.setdefault(20, {"posicion": "MED", "nombre": "Pedri", "capitan": False})

# --- CAMBIOS MINUTO 75' ---
# Salen: Dani Olmo (10) y Álex Baena (15) -> Eliminación con 'del'
del final[10]
del final[15]
# Entran: Nico Williams (17) y Mikel Merino (6) -> Inserción con '.setdefault()'[cite: 1]
final.setdefault(17, {"posicion": "DEL", "nombre": "Nico Williams", "capitan": False})
final.setdefault(6, {"posicion": "MED", "nombre": "Mikel Merino", "capitan": False})

# --- CAMBIOS MINUTO 99' (PRÓRROGA) ---
# Salen: Aymeric Laporte (14) y Rodri Hernández (16) -> Eliminación con 'del'
del final[14]
del final[16]
# Entran: Martín Zubimendi (18) y Eric García (4) -> Inserción con '.setdefault()'[cite: 1]
final.setdefault(
    18, {"posicion": "MED", "nombre": "Martín Zubimendi", "capitan": False}
)
final.setdefault(4, {"posicion": "DEF", "nombre": "Eric García", "capitan": False})

# ------------------------------------------------------------------------------
# 4. SALIDA TABULADA Y ORDENADA POR DORSAL (1 a 99) MEDIANTE .get()
# ------------------------------------------------------------------------------
print("=== ALINEACIÓN FINAL DEL PARTIDO (TRAS LAS 6 SUSTITUCIONES) ===")
print(f"{'Nº':<4} | {'POS':<4} | {'NOMBRE'}")
print("=" * 40)

# Recorrido de los dorsales de menor a mayor (del 1 al 99)
for dorsal in range(1, 100):
    # Búsqueda segura con .get()[cite: 1]
    jugador = final.get(dorsal)

    if jugador is not None:
        posicion = jugador.get("posicion", "---")
        nombre = jugador.get("nombre", "Desconocido")
        es_capitan = " (C)" if jugador.get("capitan", False) else ""

        # Salida por pantalla formateada con alineación a la izquierda
        print(f"{dorsal:<4} | {posicion:<4} -> {nombre}{es_capitan}")

# Conteo dinámico de los jugadores que terminan en el terreno de juego
total_final = len(final)
print(f"\nTerminaron el partido {total_final} jugadores en el terreno de juego.\n")
