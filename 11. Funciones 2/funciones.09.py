import estadisticas  # Importamos el módulo creado previamente

tiempos = []

print("--- REGISTRO DE TIEMPOS DE ATLETISMO ---")
print("Introduce los tiempos en segundos de cada atleta.")
print("Escribe -1 para finalizar la entrada de datos.\n")

# 1. ENTRADA DE DATOS
while True:
    tiempo = int(input("Introduce tiempo en segundos: "))

    if tiempo == -1:
        break  # Finaliza la lectura de datos
    elif tiempo < 0:
        print("  [!] Un tiempo no puede ser negativo. Inténtalo de nuevo.")
    else:
        tiempos.append(tiempo)

# 2. COMPROBACIÓN DE DATOS Y SALIDA
if not tiempos:
    # Requisito: Si no se introdujo ningún tiempo válido, mostrar aviso
    print("\n[AVISO] No se ha introducido ningún tiempo válido.")
else:
    # A) Tiempo medio en formato m:s
    media_seg = estadisticas.calcular_media(tiempos)
    minutos = int(media_seg // 60)
    segundos = int(media_seg % 60)

    # B) Mejor tiempo (mínimo) y peor tiempo (máximo)
    mejor_tiempo, peor_tiempo = estadisticas.obtener_extremos(tiempos)

    # C) Atletas por debajo de la media
    bajo_media = estadisticas.contar_bajo_media(tiempos)

    # 3. MOSTRAR RESULTADOS
    print("\n--- RESUMEN ESTADÍSTICO ---")
    print(f"• Tiempo medio: {minutos}m {segundos}s (media exacta: {media_seg:.2f} s)")
    print(f"• Mejor tiempo (mínimo): {mejor_tiempo} s")
    print(f"• Peor tiempo (máximo): {peor_tiempo} s")
    print(f"• Atletas por debajo de la media: {bajo_media}")
