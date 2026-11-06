# while203
# José Antonio Sallán


# Importamos del módulo random de la librería estándar
import random

print('LANZANDO DOS DADOS')
print('------------------')

# Creo la variable que controla la generación de números aleatorios
# Le asigno el valor S para que la condicón del bucle siguiente sea cierta en la primera pasada
# y con ello siempre se genere un primer número aleatorio
resp = 'S'
# Creo dos variables total1 y total2 para almacenar la suma de las tiradas de cada jugador
# Su valor inicial será 0
total1 = total2 = 0

# Bucle que generará los valores aleatorios
while resp == 'S' or resp == 's':
    # Guardaré el valor conseguido en las tiradas actual en la variable tirada1 y tirada2
    tirada1 = random.randint(1, 6)
    tirada2 = random.randint(1, 6)
    # Sumo las tiradas actuales a las sumas de tiradas
    total1 = total1 + tirada1
    total2 = total2 + tirada2
    # Muestro el resultado por pantalla
    print('Primer jugador:\t\tTirada actual:', tirada1, '\tTotal acumulado:', total1)
    print('Segundo jugador:\tTirada actual:', tirada2, '\tTotal acumulado:', total2)
    resp = input('Para generar un nuevo número pulsa S o s, otra tecla para terminar: ')
# Mostraremos el resultado final
print('*************************************************************************')
if total1 > total2:
    # Ha ganado el primer jugador
    print('Vencedor: Primer jugador.\tResultado final:Jugador1:', total1, '- Jugador2:', total2)
elif total1 < total2:
    # Ha ganado el segundo jugador
    print('Vencedor: Segundo jugador.\tResultado final:Jugador1:', total1, '- Jugador2:', total2)
else:
    # Empate
    print('Primer jugador y segundo jugador han empatado a ', total1, 'puntos')
print('*************************************************************************')
