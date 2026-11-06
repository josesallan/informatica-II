import tiempo  # Importamos nuestro módulo para realizar las conversiones de tiempo

# Pedimos los datos iniciales
precio_por_segundo = float(input("¿Cuántos céntimos cuesta 1 segundo de alquiler?: "))
num_trayectos = int(input("¿Cuántos trayectos se van a facturar?: "))

# Variables acumuladoras para los totales del día
total_segundos_acumulados = 0
total_centimos_acumulados = 0.0

# Procesamos cada trayecto
for i in range(1, num_trayectos + 1):
    print(f"\nTrayecto {i}:")

    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    # 1. Obtenemos la duración del trayecto actual en segundos
    duracion_segundos = tiempo.convertir_a_segundos(horas, minutos, segundos)

    # 2. Calculamos el coste del trayecto en céntimos
    coste_centimos = duracion_segundos * precio_por_segundo

    # 3. Acumulamos los valores para el resumen final
    total_segundos_acumulados += duracion_segundos
    total_centimos_acumulados += coste_centimos

    # 4. Desglosamos el coste del trayecto en euros y céntimos
    # 100 céntimos = 1 euro
    euros_trayecto = int(coste_centimos // 100)
    centimos_trayecto = int(coste_centimos % 100)

    # Mostramos el resultado individual del trayecto
    print(
        f"Duración: {duracion_segundos} segundos | Coste: {euros_trayecto}€, {centimos_trayecto}cts"
    )

# --- RESUMEN FINAL ---

# Convertimos el tiempo total acumulado a formato (h, m, s) usando nuestro módulo
h_tot, m_tot, s_tot = tiempo.convertir_a_hms(total_segundos_acumulados)

# Desglosamos el importe acumulado en euros y céntimos
euros_totales = int(total_centimos_acumulados // 100)
centimos_totales = int(total_centimos_acumulados % 100)

print("\n--- Resumen Final ---")
# Usamos :02d en las f-strings para formatear los números a dos dígitos con cero a la izquierda (ej. 01)
print(f"Duración total combinada: {h_tot:02d} h : {m_tot:02d} m : {s_tot:02d} s")
print(f"Coste total a cobrar: {euros_totales}€, {centimos_totales} cts.")
