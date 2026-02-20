# José Antonio Sallán

# Importamos del módulo random de la librería estándar
import random

print('LANZANDO UN DADO')
print('----------------')

# Creo la variable que controla la generación de números aleatorios
# Le asigno el valor S para que la condicón del bucle siguiente sea cierta en la primera pasada
# y con ello siempre se genere un primer número aleatorio
resp = 'S'
# Creo una variable total para almacenar la suma de las tiradas
# Su valor inicial será 0
total = 0

# Bucle que generará los valores aleatorios
while resp == 'S' or resp == 's':
    # Guardaré el valor conseguido en la tirada actual en la variable tirada
    tirada = random.randint(1, 6)
    # Sumo la tirada actual a la suma de tiradas
    total = total + tirada
    # Muestro el resultado por pantalla
    print('Tirada actual:', tirada, 'Total acumulado:', total)
    resp = input('Para generar un nuevo número pulsa S o s, otra tecla para terminar: ')
print('Puntuación final:', total, '- Programa terminado')
