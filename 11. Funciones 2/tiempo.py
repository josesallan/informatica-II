def convertir_a_segundos(horas, minutos, segundos):
    """
    Recibe tres enteros (horas, minutos y segundos)
    y devuelve su equivalente en segundos.
    """
    return (horas * 3600) + (minutos * 60) + segundos


def convertir_a_hms(segundos_totales):
    """
    Recibe el total de segundos y devuelve una tupla con (horas, minutos, segundos).
    """
    # Usamos división entera (//) para obtener las horas completas
    horas = segundos_totales // 3600

    # El operador módulo (%) nos da el resto de segundos que no completan una hora
    resto = segundos_totales % 3600

    # De ese resto, obtenemos los minutos enteros
    minutos = resto // 60

    # El resto final son los segundos sueltos
    segundos = resto % 60

    return horas, minutos, segundos
