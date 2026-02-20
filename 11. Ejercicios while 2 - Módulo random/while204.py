# while204
# José Antonio Sallán

# Importamos del módulo random de la librería estándar
import random

print('LANZANDO DOS DADOS II')
print('------------------')
# En este caso tenemos dos jugadores, dos dados y dos condiciones de parada independientes.

# Creo las dos variables que controlarán la generación de los dos números aleatorios
# Les asigno el valor S para que la condición del bucle siguiente sea cierta en la primera pasada
# y con ello siempre se genere una primera pareja de números aleatorios
resp1 = resp2 = 'S'
# Creo dos variables total1 y total2 para almacenar la suma de las tiradas de cada jugador
# Su valor inicial será 0
total1 = total2 = 0

# Bucle que generará los valores aleatorios
while resp1 == 'S' or resp1 == 's' or resp2 == 'S' or resp2 == 's':
    # Guardaré el valor conseguido en las tiradas actual en la variable tirada1 y tirada2
    # A través de un if controlo quien de los dos jugadores quiere seguir jugando
    if resp1 == 'S' or resp1 == 's':
        tirada1 = random.randint(1, 6)
    else:
        tirada1 = 0
    if resp2 == 'S' or resp2 == 's':
        tirada2 = random.randint(1, 6)
    else:
        tirada2 = 0
    # Sumo las tiradas actuales a las sumas de tiradas
    total1 = total1 + tirada1
    total2 = total2 + tirada2
    # Muestro el resultado por pantalla
    print('Primer jugador:\t\tTirada actual:', tirada1, '\tTotal acumulado:', total1)
    print('Segundo jugador:\tTirada actual:', tirada2, '\tTotal acumulado:', total2)
    if resp1 == 'S' or resp1 == 's':
        resp1 = input('Jugador 1: Para lanzar el dado pulsa S o s, otra tecla para terminar: ')
    if resp2 == 'S' or resp2 == 's':
        resp2 = input('Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: ')
# Mostraremos el resultado final
print('*************************************************************************')
if total1 > total2:
    # Ha ganado el primer jugador
    print('Vencedor: Primer jugador.\tResultado final: Jugador 1:', total1, '- Jugador 2:', total2)
elif total1 < total2:
    # Ha ganado el segundo jugador
    print('Vencedor: Segundo jugador.\tResultado final: Jugador 1:', total1, '- Jugador 2:', total2)
else:
    # Empate
    print('Primer jugador y segundo jugador han empatado a ', total1, 'puntos')
print('*************************************************************************')
