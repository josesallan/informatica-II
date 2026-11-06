# Importamos los tres módulos
import ej15_1
import ej15_2
import ej15_3
import ej15_4

while True:
    print("\n========================================")
    print("      SUITE DE UTILIDADES PYTHON        ")
    print("========================================")
    print("1. Máquina tragaperras")
    print("2. Generador de Boleto de Lotería")
    print("3. Test de Reflejos y Tiempo de Reacción")
    print("4. Generador de Contraseñas Seguras")
    print("5. Salir")
    print("========================================")

    opcion = input("Selecciona una opción: ").strip().lower()

    if opcion == "1":
        ej15_1.ejecutar()
    elif opcion == "2":
        ej15_2.ejecutar()
    elif opcion == "3":
        ej15_3.ejecutar()
    elif opcion == "4":
        ej15_4.ejecutar()
    elif opcion == "5" or opcion == "salir":
        print("\n¡Gracias por usar la suite de utilidades! Hasta pronto.")
        break
    else:
        print("\n⚠️ Opción no reconocida. Por favor, selecciona un número del 0 al 4.")
