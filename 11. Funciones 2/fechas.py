"""
Módulo fechas.py
Contiene funciones para validar fechas y realizar cálculos de días en un año.
"""


def es_bisiesto(anyo):
    """
    Devuelve True si el año es bisiesto y False en caso contrario.
    Regla: divisible por 4 y no por 100, excepto si es divisible por 400.
    """
    return (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0)


def dias_del_mes(mes, anyo):
    """
    Devuelve el número de días de un mes (1 al 12).
    Tiene en cuenta si el año es bisiesto para el mes de febrero.
    """
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        if es_bisiesto(anyo):
            return 29
        else:
            return 28
    else:
        return 0  # Si se introduce un mes fuera del rango 1-12


def es_fecha_valida(dia, mes, anyo):
    """
    Comprueba si la combinación de día, mes y año forma una fecha correcta.
    """
    if anyo < 1:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_del_mes(mes, anyo):
        return False

    return True


def dia_del_anyo(dia, mes, anyo):
    """
    Calcula el número de día transcurrido en el año (ej. 1 de febrero -> 32).
    Si la fecha no es válida, devuelve None.
    """
    if not es_fecha_valida(dia, mes, anyo):
        return None

    # Sumamos los días de los meses completos anteriores al mes actual
    dias_acumulados = 0
    for m in range(1, mes):
        dias_acumulados += dias_del_mes(m, anyo)

    # Añadimos los días del mes actual
    dias_acumulados += dia
    return dias_acumulados
