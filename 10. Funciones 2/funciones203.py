# Factura el tiempo de uso de un teléfono

# El usuario ingresa la tarifa por segundo, cuántas
# comunicaciones se realizaron, y la duracion de cada
# comunicación expresada en horas, minutos y segundos. Como
# resultado se informa la duración en segundos de cada
# comunicación y su costo.

# Importamos el módulo cronometro que contiene las funciones que
# permiten cambiar el formato de los tiempos.
import cronometro


# Almacenamos el coste en una variable de tipo decimal
f = float(input("¿Cuánto céntimos cuesta 1 segundo de comunicación?: "))
# Almacenamos el número de llamadas en una variable de tipo entero
n = int(input("¿Cuántas llamadas hay que facturar?: "))

# Un bucle se repetirá en tantas ocasiones como lladas haya que facturar
for x in range(n):
    # Recojo la información de la llamada
    hs = int(input("¿Cuántas horas?: "))
    mn = int(input("¿Cuántos minutos?: "))
    seg = int(input("¿Cuántos segundos?: "))
    # Utilizo la función para pasar el tiempo a segundos
    segcalc = cronometro.aseg(hs, mn, seg)
    # Calculo el coste
    coste = segcalc * f
    # Muestro el resultado de la llamada
    print("Duracion: ", segcalc, "segundos. Coste: ", coste, "c€.")
