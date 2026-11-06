# Importamos el módulo 'area' (ubicado en la misma carpeta)
import area

# Mostramos el menú inicial de opciones
print("Selecciona una opción")
print("a) Superficie de un cuadrado")
print("b) Superficie de un rectángulo")
print("c) Superficie de un trapecio")
print("d) Superficie de un triángulo")
print("e) Superficie de un círculo")
print("f) Superficie de un romboide")

# Lista con las opciones permitidas
opciones_validas = ["a", "b", "c", "d", "e", "f"]

# Solicitamos la primera opción y la pasamos a minúscula con .lower()
opcion = input("?: ").lower()

# Bucle de validación: se repite hasta que el usuario introduzca una opción válida
while opcion not in opciones_validas:
    opcion = input("Opción incorrecta. Vuelve a intentarlo?: ").lower()

# Según la opción elegida, pedimos los datos necesarios y llamamos a la función del módulo
if opcion == "a":
    lado = float(input("¿Longitud del lado?: "))
    resultado = area.cuadrado(lado)

elif opcion == "b":
    base = float(input("¿Longitud de la base?: "))
    altura = float(input("¿Longitud de la altura?: "))
    resultado = area.rectangulo(base, altura)

elif opcion == "c":
    base_mayor = float(input("¿Longitud de la base mayor?: "))
    base_menor = float(input("¿Longitud de la base menor?: "))
    altura = float(input("¿Longitud de la altura?: "))
    resultado = area.trapecio(base_mayor, base_menor, altura)

elif opcion == "d":
    base = float(input("¿Longitud de la base?: "))
    altura = float(input("¿Longitud de la altura?: "))
    resultado = area.triangulo(base, altura)

elif opcion == "e":
    radio = float(input("¿Longitud del radio?: "))
    resultado = area.circulo(radio)

elif opcion == "f":
    base = float(input("¿Longitud de la base?: "))
    altura = float(input("¿Longitud de la altura?: "))
    resultado = area.romboide(base, altura)

# Mostramos el resultado final
print(f"Superficie: {resultado}")
