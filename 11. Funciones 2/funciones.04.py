import tiempo  # Importamos nuestro módulo para reutilizar la función de conversión

# Pedimos los datos generales de facturación
precio_por_segundo = float(input("¿Cuántos céntimos cuesta 1 segundo de alquiler?: "))
num_trayectos = int(input("¿Cuántos trayectos se van a facturar?: "))

# Procesamos cada trayecto uno a uno
for i in range(1, num_trayectos + 1):
    print(f"\nTrayecto {i}:")

    # Lectura de los datos del trayecto actual
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    # Usamos la función de tiempo.py para obtener el total de segundos
    duracion_segundos = tiempo.convertir_a_segundos(horas, minutos, segundos)

    # Calculamos el coste total en céntimos
    coste = duracion_segundos * precio_por_segundo

    # Mostramos los resultados del trayecto
    print(f"Duración: {duracion_segundos} segundos | Coste: {coste} c€")
