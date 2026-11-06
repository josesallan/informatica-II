# Importamos del módulo random de la libreria estándar
import random

print('GENERADOR DE NÚMEROS ALEATORIOS')

# Creo la variable que controla la generación de números aleatorios
# Le asigno el valor S para que la condicón del bucle siguiente sea cierta en la primera pasada
# y con ello siempre se genere un primer número aleatorio
resp = 'S'
while resp == 'S' or resp == 's':
    print(random.randint(1, 6))
    resp = input('Para generar un nuevo número pulsa S o s, otra tecla para terminar: ')
print('programa terminado')
