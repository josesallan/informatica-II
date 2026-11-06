"""
Módulo estadisticas.py
Contiene funciones para el análisis estadístico de listas de datos numéricos.
"""


def calcular_media(lista_valores):
    """Calcula y devuelve la media aritmética de una lista de números."""
    if not lista_valores:
        return 0.0  # Control de seguridad si la lista está vacía

    suma = 0
    for elemento in lista_valores:
        suma += elemento  # Forma compacta de: suma = suma + elemento

    media = suma / len(lista_valores)
    return media


def obtener_extremos(lista_valores):
    """Devuelve una tupla con los valores mínimo y máximo: (minimo, maximo)."""
    if not lista_valores:
        return None, None

    # Usamos 'minimo' y 'maximo' para no sobrescribir las funciones integradas min() y max()
    minimo = lista_valores[0]
    maximo = lista_valores[0]

    for elemento in lista_valores:
        if elemento < minimo:
            minimo = elemento
        if elemento > maximo:
            maximo = elemento

    # Devuelve en el orden solicitado por el enunciado (mínimo, máximo)
    return minimo, maximo


def contar_bajo_media(lista_valores):
    """Cuenta cuántos elementos de la lista están estrictamente por debajo de la media."""
    # Reutilizamos la función calcular_media definida en este mismo módulo
    media = calcular_media(lista_valores)

    contador = 0
    for elemento in lista_valores:
        if elemento < media:
            contador += 1

    return contador
