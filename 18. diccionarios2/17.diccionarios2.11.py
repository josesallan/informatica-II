# ==============================================================================
# INFORMÁTICA II — 2º BACHILLERATO | IES Fco. Grande Covián
# Ejercicio: Simulador de Seleccionador con Control de Reingreso y Contador
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
    1:  {"posicion": "POR", "nombre": "David Raya", "sustituido": False},
    2:  {"posicion": "DEF", "nombre": "Dani Carvajal", "sustituido": False},
    4:  {"posicion": "DEF", "nombre": "Eric García", "sustituido": False},
    6:  {"posicion": "MED", "nombre": "Mikel Merino", "sustituido": False},
    7:  {"posicion": "DEL", "nombre": "Ferran Torres", "sustituido": False},
    9:  {"posicion": "DEL", "nombre": "Joselu", "sustituido": False},
    17: {"posicion": "DEL", "nombre": "Nico Williams", "sustituido": False},
    18: {"posicion": "MED", "nombre": "Martín Zubimendi", "sustituido": False},
    20: {"posicion": "MED", "nombre": "Pedri", "sustituido": False},
    25: {"posicion": "DEF", "nombre": "Daniel Vivian", "sustituido": False}
}


# ------------------------------------------------------------------------------
# 2. MEJORA 2: FUNCIÓN DE MOSTRADO CON MARCA '(Sustituido)'
# ------------------------------------------------------------------------------
def mostrar_diccionario(diccionario):
    """
    Muestra el contenido del diccionario pasado como parámetro.
    Muestra '(C)' para capitán y '(Sustituido)' para jugadores cambiados.
    """
    print(f"{'Nº':<4} | {'POS':<4} | {'NOMBRE'}")
    print("=" * 45)
    
    # Recorremos los dorsales del 1 al 99
    for dorsal in range(1, 100):
        jugador = diccionario.get(dorsal)  # Lectura segura con .get()
        if jugador is not None:
            posicion = jugador.get("posicion", "---")
            nombre = jugador.get("nombre", "Desconocido")
            
            # Evaluación de marcas de capitán y sustituido[cite: 1]
            es_capitan = " (C)" if jugador.get("capitan", False) else ""
            es_sustituido = " (Sustituido)" if jugador.get("sustituido", False) else ""
            
            print(f"{dorsal:<4} | {posicion:<4} -> {nombre}{es_capitan}{es_sustituido}")


# ------------------------------------------------------------------------------
# 3. BUCLE DE SUSTITUCIONES CON REGLA DE REINGRESO Y CONTADOR (MEJORA 3)
# ------------------------------------------------------------------------------
MAX_CAMBIOS = 6
num_cambio = 1

while num_cambio <= MAX_CAMBIOS:
    # Mejora 3: Cálculo e información previa de cambios disponibles[cite: 1]
    cambios_restantes = MAX_CAMBIOS - num_cambio + 1
    
    print("\n" + "=" * 50)
    print(f"       SUSTITUCIÓN {num_cambio} DE {MAX_CAMBIOS}")
    print(f"       (Quedan {cambios_restantes} cambios disponibles)")
    print("=" * 50)
    
    # Mostrar el estado actual llamando a la función mejorada
    print("\n--- TITULARES (EN EL CAMPO) ---")
    mostrar_diccionario(titulares)
    
    print("\n--- BANQUILLO (SUPLENTES) ---")
    mostrar_diccionario(suplentes)
    
    # 1. Comprobación del jugador que sale del campo (debe estar en titulares)
    dorsal_sale = int(input(f"\n[{num_cambio}/{MAX_CAMBIOS}] Dorsal del titular que SALE: "))
    
    if dorsal_sale not in titulares:
        print(f"\n ERROR: El dorsal {dorsal_sale} no está en el terreno de juego.")
        continue
        
    # 2. Comprobación del jugador que entra al campo (debe estar en suplentes)
    dorsal_entra = int(input(f"[{num_cambio}/{MAX_CAMBIOS}] Dorsal del suplente que ENTRA: "))
    
    if dorsal_entra not in suplentes:
        print(f"\n ERROR: El dorsal {dorsal_entra} no está disponible en el banquillo.")
        continue
        
    # Regla de sustitución: Impedir que un jugador ya sustituido vuelva a entrar[cite: 1]
    if suplentes[dorsal_entra].get("sustituido", False):
        print(f"\n ERROR: El dorsal {dorsal_entra} ya fue sustituido previamente y no puede volver a entrar.")
        continue

    # 3. Intercambio de futbolistas mediante .pop()[cite: 1]
    jugador_sale = titulares.pop(dorsal_sale)
    jugador_entra = suplentes.pop(dorsal_entra)
    
    # Marcamos la clave "sustituido" en True para el jugador que abandona el campo[cite: 1]
    jugador_sale["sustituido"] = True
    
    # Asignamos las nuevas posiciones en los diccionarios
    titulares[dorsal_entra] = jugador_entra
    suplentes[dorsal_sale] = jugador_sale
    
    # Mejora 3: Feedback inmediato del cambio y recuento de cambios restantes[cite: 1]
    quedan = MAX_CAMBIOS - num_cambio
    print(f"\n>> CAMBIO APLICADO: Sale {jugador_sale['nombre']} ({dorsal_sale}) -> Entra {jugador_entra['nombre']} ({dorsal_entra})")
    print(f">> TE QUEDAN {quedan} CAMBIOS POR HACER.")
    
    num_cambio += 1

# ------------------------------------------------------------------------------
# 4. ESTADO FINAL DE LOS DICCIONARIOS TRAS AGOTAR LAS SUSTITUCIONES
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print(f"   SE HAN REALIZADO LAS {MAX_CAMBIOS} SUSTITUCIONES PERMITIDAS")
print("=" * 50)

print("\n--- ALINEACIÓN TITULAR FINAL ---")
mostrar_diccionario(titulares)

print("\n--- BANQUILLO FINAL ---")
mostrar_diccionario(suplentes)