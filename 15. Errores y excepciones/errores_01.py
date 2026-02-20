'''1. Localiza el error en el siguiente bloque de código. Crea una excepción para
evitar que el programa se bloquee y que explique al usuario la causa y/o solución:

resultado = 10/0

No es posible dividir entre cero, debes introducir un número distinto.'''

# Incluimos el bloque de código (una única línea en este caso) que va generar el error dentro de un bloque try
try:
    resultado = 10 / 0
# Capturamos la excepeción y generamos un menasaje por pantalla.
except ZeroDivisionError:
    print("No es posible dividir entre cero, debes introducir un número distinto")
