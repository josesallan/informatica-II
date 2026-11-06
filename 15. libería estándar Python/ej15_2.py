def ejecutar():
    from random import sample, randint

    # Bucle principal que se repite hasta que el usuario decida salir
    while True:
        # 1. Generamos 6 números aleatorios del 1 al 49 (sin repetir)
        numeros_ganadores = sample(range(1, 50), 6)

        # 2. Ordenamos los 6 números de menor a mayor
        numeros_ganadores = sorted(numeros_ganadores)

        # 3. Generamos el número de reintegro (entre 0 y 9)
        reintegro = randint(0, 9)

        # 4. Presentación visual del boleto
        print("\n------------------------------")
        print("    TU BOLETO DE LA SUERTE    ")
        print("------------------------------")

        # Usamos end="" para que el siguiente print no salte de línea
        print("Números: ", end="")

        # Recorremos la lista elemento a elemento para imprimirlos limpitos
        for numero in numeros_ganadores:
            print(numero, end=" ")  # Separa cada número con un espacio

        print()  # Imprimimos una línea en blanco para hacer el salto de línea al final
        print("Reintegro:", reintegro)
        print("------------------------------\n")

        # 5. Preguntamos al usuario si desea continuar
        repetir = input("¿Quieres generar un nuevo boleto? (S/N): ")

        if repetir.upper() != "S":
            print("¡Gracias por jugar! Mucha suerte.")
            break
