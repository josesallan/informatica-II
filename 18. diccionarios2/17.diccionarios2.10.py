# ==============================================================================
# INFORMÁTICA II — 2º BACHILLERATO | IES Fco. Grande Covián
# Ejercicio: Simulador de Seleccionador con Validación de Pertenencia (in)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. DICCIONARIOS INICIALES (TITULARES Y SUPLENTES)
# ------------------------------------------------------------------------------
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

suplentes = {
    1:  {"posicion": "POR", "nombre": "David Raya"},
    2:  {"posicion": "DEF", "nombre": "Dani Carvajal"},
    4:  {"posicion": "DEF", "nombre": "Eric García"},
    6:  {"posicion": "MED", "nombre": "Mikel Merino"},
    7:  {"posicion": "DEL", "nombre": "Ferran Torres"},
    9:  {"posicion": "DEL", "nombre": "Joselu"},
    17: {"posicion": "DEL", "nombre": "Nico Williams"},
    18: {"posicion": "MED", "nombre": "Martín Zubimendi"},
    20: {"posicion": "MED", "nombre": "Pedri"},
    25: {"posicion": "DEF", "nombre": "Daniel Vivian"}
}


# ------------------------------------------------------------------------------
# 2. MEJORA 1: FUNCIÓN DE MOSTRADO CON UN ÚNICO PARÁMETRO
# ------------------------------------------------------------------------------
def mostrar_diccionario(diccionario):
    """Muestra el contenido del diccionario pasado como parámetro de forma tabulada."""
    print(f"{'Nº':<4} | {'POS':<4} | {'NOMBRE'}")
    print("=" * 40)
    
    # Recorremos secuencialmente los dorsales del 1 al 99
    for dorsal in range(1, 100):
        jugador = diccionario.get(dorsal)  # Lectura segura con .get()
        if jugador is not None:
            posicion = jugador.get("posicion", "---")
            nombre = jugador.get("nombre", "Desconocido")
            es_capitan = " (C)" if jugador.get("capitan", False) else ""
            print(f"{dorsal:<4} | {posicion:<4} -> {nombre}{es_capitan}")


# ------------------------------------------------------------------------------
# 3. BUCLE DE SUSTITUCIONES CON VALIDACIÓN DE PERTENENCIA ('in')
# ------------------------------------------------------------------------------
MAX_CAMBIOS = 6
num_cambio = 1

while num_cambio <= MAX_CAMBIOS:
    print("\n" + "=" * 40)
    print(f"       SUSTITUCIÓN {num_cambio} DE {MAX_CAMBIOS}")
    print("=" * 40)
    
    # Mostrar el estado actual de los diccionarios con la función creada
    print("\n--- TITULARES (EN EL CAMPO) ---")
    mostrar_diccionario(titulares)
    
    print("\n--- BANQUILLO (SUPLENTES) ---")
    mostrar_diccionario(suplentes)
    
    # 1. Comprobación del jugador que sale (debe estar presente en 'titulares')
    dorsal_sale = int(input(f"\n[{num_cambio}/{MAX_CAMBIOS}] Dorsal del titular que SALE: "))
    
    if dorsal_sale not in titulares:
        print(f"\n ERROR: El dorsal {dorsal_sale} no está actualmente en el terreno de juego.")
        print(" Por favor, elige un jugador que esté en la lista de TITULARES.")
        continue  # Vuelve a iniciar el bucle sin consumir una sustitución
        
    # 2. Comprobación del jugador que entra (debe estar presente en 'suplentes')
    dorsal_entra = int(input(f"[{num_cambio}/{MAX_CAMBIOS}] Dorsal del suplente que ENTRA: "))
    
    if dorsal_entra not in suplentes:
        print(f"\n ERROR: El dorsal {dorsal_entra} no está disponible en el banquillo.")
        print(" Por favor, elige un jugador que esté en la lista de SUPLENTES.")
        continue  # Vuelve a iniciar el bucle sin consumir una sustitución

    # 3. Intercambio mediante .pop() si ambos dorsales son válidos
    jugador_sale = titulares.pop(dorsal_sale)
    jugador_entra = suplentes.pop(dorsal_entra)
    
    titulares[dorsal_entra] = jugador_entra
    suplentes[dorsal_sale] = jugador_sale
    
    print(f"\n>> CAMBIO APLICADO: Sale {jugador_sale['nombre']} ({dorsal_sale}) -> Entra {jugador_entra['nombre']} ({dorsal_entra})")
    
    # Se avanza en el conteo de cambios únicamente cuando el intercambio es válido
    num_cambio += 1

# ------------------------------------------------------------------------------
# 4. ESTADO FINAL DE LOS DICCIONARIOS TRAS LAS 6 SUSTITUCIONES
# ------------------------------------------------------------------------------
print("\n" + "=" * 40)
print(f"   SE HAN REALIZADO LAS {MAX_CAMBIOS} SUSTITUCIONES")
print("=" * 40)

print("\n--- ALINEACIÓN TITULAR FINAL ---")
mostrar_diccionario(titulares)

print("\n--- BANQUILLO FINAL ---")
mostrar_diccionario(suplentes)