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


# Lista para mostrar "primer", "segundo", "tercer" en cada iteración
ordinales = ["primer", "segundo", "tercer"]
suma_total_segundos = 0

# Pedimos los datos de tiempo tres veces (en lugar de utilizar split como antes)
for i in range(3):
    print(f"Introduce el {ordinales[i]} tiempo")
    h = int(input("horas: "))
    m = int(input("minutos: "))
    s = int(input("segundos: "))

    # Convertimos a segundos acumulados
    suma_total_segundos += convertir_a_segundos(h, m, s)

# Convertimos los segundos acumulados de nuevo al formato h:m:s
h_total, m_total, s_total = convertir_a_hms(suma_total_segundos)

# Mostramos el resultado
print(f"\nTiempo total: {h_total} h: {m_total} m: {s_total} s")
