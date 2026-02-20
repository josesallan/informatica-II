# Importamos él módulo tiempo con todas sus funciones
import tiempo

# Solicitamos los tres valores y calculamos su equivalentes en segundos
print('Introduce el primer tiempo')
a = int(input('horas: '))
b = int(input('minutos: '))
c = int(input('segundos: '))

primerTiempo = tiempo.aSegundos(a, b, c)

print('Introduce el segundo tiempo')
a = int(input('horas: '))
b = int(input('minutos: '))
c = int(input('segundos: '))

segundoTiempo = tiempo.aSegundos(a, b, c)

print('Introduce el tercer tiempo')
a = int(input('horas: '))
b = int(input('minutos: '))
c = int(input('segundos: '))

tercerTiempo = tiempo.aSegundos(a, b, c)

total = primerTiempo + segundoTiempo + tercerTiempo

# Transformamos el tiempo a hh, mm y ss.
hh, mm, ss = tiempo.hhmmss(total)

# Mostramos el resultado en segundos
print("La suma de los tres tiempos es igual a: " + str(hh) + "h " + str(mm) + "m y " + str(ss) + "s")
