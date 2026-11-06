def ejecutar():
    import time

    import random

    # Bucle principal para repetir el test tantas veces como se desee
    while True:
        print("\n----------------------------------------")
        print("      TEST DE TIEMPO DE REACCIÓN        ")
        print("----------------------------------------")

        # 1. Mensaje inicial de aviso
        print("Preparado...")

        # 2. Generamos una pausa aleatoria entre 2.0 y 5.0 segundos
        tiempo_espera = random.uniform(2.0, 5.0)
        time.sleep(tiempo_espera)

        # 3. Registramos la marca de tiempo exacta JUSTO ANTES de la señal
        tiempo_inicial = time.time()

        # 4. Lanzamos el aviso y esperamos a que el usuario presione ENTER
        input("¡¡¡YA!!! Pulsa ENTER rápidamente ")

        # 5. Registramos la marca de tiempo exacta JUSTO DESPUÉS de pulsar ENTER
        tiempo_final = time.time()

        # 6. Restamos ambos instantes y redondeamos a 3 decimales (según el enunciado)
        tiempo_reflejos = round(tiempo_final - tiempo_inicial, 3)

        # 7. Mostramos la marca conseguida
        print(f"\n-> ¡Tu tiempo de reacción ha sido de {tiempo_reflejos} segundos!")
        print("----------------------------------------\n")

        # 8. Preguntamos si desea realizar un nuevo intento
        repetir = input("¿Quieres intentar mejorar tu marca? (S/N): ")

        # Si introduce cualquier cosa que no sea 'S' o 's', salimos del bucle
        if repetir.upper() != "S":
            print("\n¡Gracias por participar! Hasta la próxima.")
            break
