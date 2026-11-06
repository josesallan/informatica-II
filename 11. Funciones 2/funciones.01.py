def convertir_a_segundos(horas, minutos, segundos):
    """
    Recibe tres enteros (horas, minutos y segundos)
    y devuelve su equivalente en segundos.
    """
    # 1 hora = 3600 segundos, 1 minuto = 60 segundos
    return (horas * 3600) + (minutos * 60) + segundos


suma_total_segundos = 0

# Pedimos tres valores de tiempo al usuario
for i in range(1, 4):
    entrada = input(f"Introduce el tiempo {i} (formato h:m:s, ej. 1:30:15): ")

    # Explicación de .split(':'):
    # En lugar de tres inputs, hago uno solo, texto con formato de tiempo
    # Split toma el texto ingresado y lo "rompe" cada vez que encuentra dos puntos ':'.
    # Si la entrada es "1:30:15", genera la lista ['1', '30', '15'].
    partes = entrada.split(":")

    # Extraemos cada elemento de la lista por su posición (índice) y lo convertimos a entero
    h = int(partes[0])
    m = int(partes[1])
    s = int(partes[2])

    # Llamamos a la función enviando los tres enteros como parámetros
    segundos = convertir_a_segundos(h, m, s)

    # Acumulamos el total
    suma_total_segundos += segundos

# Mostramos el resultado
print(f"\nLa suma total de los tres tiempos es: {suma_total_segundos} segundos.")
