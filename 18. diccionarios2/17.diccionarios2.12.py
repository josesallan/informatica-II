# ==============================================================================
# INFORMÁTICA II — 2º BACHILLERATO | IES Fco. Grande Covián
# Ejercicio: Visualización en Dos Columnas Paralelas (Titulares vs. Suplentes)
# ==============================================================================

import os

# ------------------------------------------------------------------------------
# 1. DICCIONARIOS INICIALES
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

suplentes = {
    1: {"posicion": "POR", "nombre": "David Raya", "sustituido": False},
    2: {"posicion": "DEF", "nombre": "Dani Carvajal", "sustituido": False},
    4: {"posicion": "DEF", "nombre": "Eric García", "sustituido": False},
    6: {"posicion": "MED", "nombre": "Mikel Merino", "sustituido": False},
    7: {"posicion": "DEL", "nombre": "Ferran Torres", "sustituido": False},
    9: {"posicion": "DEL", "nombre": "Joselu", "sustituido": False},
    17: {"posicion": "DEL", "nombre": "Nico Williams", "sustituido": False},
    18: {"posicion": "MED", "nombre": "Martín Zubimendi", "sustituido": False},
    20: {"posicion": "MED", "nombre": "Pedri", "sustituido": False},
    25: {"posicion": "DEF", "nombre": "Daniel Vivian", "sustituido": False},
}


# ------------------------------------------------------------------------------
# 2. FUNCIÓN DE IMPRESIÓN EN DOS COLUMNAS PARALELAS
# ------------------------------------------------------------------------------
def mostrar_dos_columnas(dict_titulares, dict_suplentes):
    """
    Genera y muestra en pantalla dos columnas alineadas horizontalmente:
    - Columna Izquierda: Titulares en el campo
    - Columna Derecha: Suplentes en el banquillo
    """
    # Lista de líneas formateadas para Titulares
    filas_titulares = []
    for dorsal in range(1, 100):
        jugador = dict_titulares.get(dorsal)
        if jugador:
            pos = jugador.get("posicion", "---")
            nom = jugador.get("nombre", "Desconocido")
            cap = " (C)" if jugador.get("capitan", False) else ""
            filas_titulares.append(f"{dorsal:<2} - {pos:<3} -> {nom}{cap}")

    # Lista de líneas formateadas para Suplentes
    filas_suplentes = []
    for dorsal in range(1, 100):
        jugador = dict_suplentes.get(dorsal)
        if jugador:
            pos = jugador.get("posicion", "---")
            nom = jugador.get("nombre", "Desconocido")
            sus = " (Sustituido)" if jugador.get("sustituido", False) else ""
            filas_suplentes.append(f"{dorsal:<2} - {pos:<3} -> {nom}{sus}")

    # Definimos el ancho de cada columna y dibujamos el marco
    ancho = 38
    borde_horizontal = "+" + "-" * (ancho + 2) + "+" + "-" * (ancho + 2) + "+"

    print(borde_horizontal)
    print(
        f"| {'JUGADORES EN EL CAMPO':<{ancho}} | {'SUPLENTES / BANQUILLO':<{ancho}} |"
    )
    print(borde_horizontal)

    # Imprimimos fila a fila combinando ambas listas
    total_filas = max(len(filas_titulares), len(filas_suplentes))
    for i in range(total_filas):
        txt_titular = filas_titulares[i] if i < len(filas_titulares) else ""
        txt_suplente = filas_suplentes[i] if i < len(filas_suplentes) else ""
        print(f"| {txt_titular:<{ancho}} | {txt_suplente:<{ancho}} |")

    print(borde_horizontal)


def borrar_pantalla():
    """Limpia la terminal según el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")


# ------------------------------------------------------------------------------
# 3. BUCLE INTERACTIVO DEL SIMULADOR
# ------------------------------------------------------------------------------
MAX_CAMBIOS = 6
num_cambio = 1

while num_cambio <= MAX_CAMBIOS:
    borrar_pantalla()

    quedan = MAX_CAMBIOS - num_cambio + 1
    print(
        f"=== PANEL DE CONTROL DEL SELECCIONADOR (CAMBIO {num_cambio}/{MAX_CAMBIOS}) ==="
    )
    print(f"Sustituciones restantes: {quedan}\n")

    mostrar_dos_columnas(titulares, suplentes)

    try:
        dorsal_sale = int(
            input(f"\n[{num_cambio}/{MAX_CAMBIOS}] Dorsal del titular que SALE: ")
        )

        if dorsal_sale not in titulares:
            print(f"\n ERROR: El dorsal {dorsal_sale} no está en el campo.")
            input("Presiona ENTER para intentar de nuevo...")
            continue

        dorsal_entra = int(
            input(f"[{num_cambio}/{MAX_CAMBIOS}] Dorsal del suplente que ENTRA: ")
        )

        if dorsal_entra not in suplentes:
            print(f"\n ERROR: El dorsal {dorsal_entra} no está en el banquillo.")
            input("Presiona ENTER para intentar de nuevo...")
            continue

        if suplentes[dorsal_entra].get("sustituido", False):
            print(f"\n ERROR: El dorsal {dorsal_entra} ya fue sustituido previamente.")
            input("Presiona ENTER para intentar de nuevo...")
            continue

        # Intercambio de diccionarios con .pop()
        jugador_sale = titulares.pop(dorsal_sale)
        jugador_entra = suplentes.pop(dorsal_entra)

        jugador_sale["sustituido"] = True

        titulares[dorsal_entra] = jugador_entra
        suplentes[dorsal_sale] = jugador_sale

        num_cambio += 1

    except ValueError:
        print("\n ERROR: Introduce un número entero válido.")
        input("Presiona ENTER para intentar de nuevo...")

# Estado final
borrar_pantalla()
print("=== FINAL DEL PARTIDO: ALINEACIÓN Y BANQUILLO DEFINITIVOS ===\n")
mostrar_dos_columnas(titulares, suplentes)
