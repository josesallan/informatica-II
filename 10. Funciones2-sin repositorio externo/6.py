# Ejercicio 5

# tarifador.py: Factura el tiempo de uso de un sistema encriptado de comunicaciones

# El usuario ingresa la tarifa por segundo, cuántas
# comunicaciones se realizaron, y la duracion de cada
# comunicación expresada en horas, minutos y segundos. Como
# resultado se informa la duración en segundos de cada
# comunicación y su costo.

# Importamos el módulo tiemp que contiene las funciones que
# permiten cambiar el formato de los tiempos.
import tiempo

# Inicializo las dos variables que van a almacenar los resultados globales
tiempototal = 0
costetotal = 0

# Almacenamos el coste en una variable de tipo decimal
f = float(input("¿Cuánto céntimos cuesta 1 segundo de comunicación?: "))
# Almacenamos el número de llamadas en una variable de tipo entero
n = int(input("¿Cuántas llamadas hay que facturar?: "))

# Un bucle se repetirá en tantas ocasiones como llamadas haya que facturar
for x in range(n):
    # Recojo la información de la llamada
    hs = int(input("¿Cuántas horas?: "))
    mn = int(input("¿Cuántos minutos?: "))
    seg = int(input("¿Cuántos segundos?: "))
    # Utilizo la función para pasar el tiempo a segundos
    segcalc = tiempo.aSegundos(hs, mn, seg)
    # Calculo el coste
    coste = segcalc * f
    # Almacenamos los resultados parciales para mostarlos al final
    tiempototal = tiempototal + segcalc
    costetotal = costetotal + coste
    # Muestro el resultado de la llamada
    print("Duracion: ", segcalc, "segundos. Coste: ", int(coste), "c€.")

# Ejercicio 6

# Una vez mostrados los resultados parciales muestro el global
# En primer lugar utilizo la función que me devuelve el tiempo en el formato que me interesa
hs, mm, seg = tiempo.hhmmss(tiempototal)
# Arreglo el formato del improte
euros = costetotal // 100
cens = costetotal % 100
# Muestro el resultado
print("===================================================")
print('Duración total: ' + str(hs) + 'h ' + str(mm) + 'm ' + str(seg) + 's')
print('Coste total: ' + str(int(euros)) + '€,' + str(int(cens)) + 'cen')
