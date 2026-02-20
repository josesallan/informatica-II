import cronometro

print('Introduce el primer tiempo')
a = int(input('horas: '))
b = int(input('minutos: '))
c = int(input('segundos: '))

primerTiempo = cronometro.aseg(a, b, c)

print('Introduce el segundo tiempo')
a = int(input('horas: '))
b = int(input('minutos: '))
c = int(input('segundos: '))

segundoTiempo = cronometro.aseg(a, b, c)

print('Introduce el tercer tiempo')
a = int(input('horas: '))
b = int(input('minutos: '))
c = int(input('segundos: '))

tercerTiempo = cronometro.aseg(a, b, c)

total = primerTiempo + segundoTiempo + tercerTiempo

print('Tiempo total:', cronometro.hhmmss(total)[0], 'h:', cronometro.hhmmss(total)[1], 'm:', cronometro.hhmmss(total)[2], 's')
