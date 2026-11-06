def ejecutar():
    import random

    import string

    # Bucle principal para permitir al usuario generar tantas contraseñas como desee
    while True:
        print("\n----------------------------------------")
        print("    GENERADOR DE CONTRASEÑAS SEGURAS    ")
        print("----------------------------------------")

        # 1. Bucle de validación para solicitar la longitud
        while True:
            longitud = int(input("Introduce la longitud de la contraseña (mínimo 8): "))

            if longitud >= 8:
                break  # Si cumple el requisito, salimos del bucle de validación

            print(
                "⚠️  Advertencia: Una contraseña con menos de 8 caracteres es poco segura. Inténtalo de nuevo.\n"
            )

        # 2. Preparamos el conjunto con todos los caracteres permitidos
        # Combinamos letras (mayúsculas y minúsculas), dígitos y símbolos de puntuación
        caracteres = string.ascii_letters + string.digits + string.punctuation

        # 3. Bucle acumulador para construir la contraseña
        contrasena = ""
        for i in range(longitud):
            # Elegimos un carácter aleatorio del total disponible
            caracter_aleatorio = random.choice(caracteres)
            # Lo añadimos a la contraseña en cada vuelta
            contrasena = contrasena + caracter_aleatorio

        # 4. Presentación de la contraseña generada
        print("\n========================================")
        print("Tu nueva contraseña es:", contrasena)
        print("========================================\n")

        # 5. Control de continuidad
        repetir = input("¿Quieres generar otra contraseña? (S/N): ")
        if repetir.upper() != "S":
            print("\n¡Gracias por utilizar el generador! Hasta pronto.")
            break
