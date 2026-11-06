def ejecutar():
    import random
    import time

    lista = ["🍒", "🍋", "🔔", "💎", "7️⃣"]

    while True:
        resultado = []

        print("\n--- MÁQUINA TRAGAPERRAS ---")
        print("Girando rodillos...")

        for i in range(3):
            elemento = random.choice(lista)
            resultado.append(elemento)
            # Usamos corchetes simples para darle forma de casilla
            print("[", elemento, "] ", end="", flush=True)
            time.sleep(0.5)

        print("\n")  # Salto de línea para separar la tirada del resultado

        # Evaluación de resultados
        if (resultado[0] == resultado[1]) and (resultado[1] == resultado[2]):
            print("🎉 ¡¡¡GRAN PREMIO!!! 🎉")
        elif (
            resultado[0] == resultado[1]
            or resultado[1] == resultado[2]
            or resultado[0] == resultado[2]
        ):
            print("✨ ¡PREMIO MENOR! ✨")
        else:
            print("❌ ¡Has perdido!")

        # Pregunta de continuación
        volver_a_jugar = input("\n¿Deseas volver a jugar? (S/n): ")
        if volver_a_jugar.upper() == "N":
            break

    print("\n¡Gracias por jugar! Programa terminado.")
