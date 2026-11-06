# while205
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
    # Por defecto inicializo el valor del tiro del dado a cero.  Con ello evito que cuando uno
    # de los dos jugadores deje de jugar se continúe sumando en los siguientes turnos el valor
    # obtenido en su última tirada.
    tirada1 = tirada2 = 0
    if resp1 == 'S' or resp1 == 's':
        tirada1 = random.randint(1, 6)
    if resp2 == 'S' or resp2 == 's':
        tirada2 = random.randint(1, 6)
    # Sumo las tiradas actuales a las sumas de tiradas
    total1 = total1 + tirada1
    total2 = total2 + tirada2
    # Muestro el resultado por pantalla
    print('Primer jugador:\t\tTirada actual:', tirada1, '\tTotal acumulado:', total1)
    print('Segundo jugador:\tTirada actual:', tirada2, '\tTotal acumulado:', total2)
    # Antes de generar más números aleatorios estudiamos el caso en que alguno o los dos jugadores
    # haya superado los 21 puntos.  En ese caso se muestra resultado y salimos del bucle
    # Mostraremos el resultado final
    # Hay múltiples posibilidades
    fin = 'no'
    # fin es una variable que controlará si ya hemos mostrado el resultado final.  Su valor inicial es 'no'
    # si mostramos resultado cambiaremos su valor por 'yes'
    if total1 <= 21 and total2 > 21:
        # Gana el primero porque el segundo se ha pasado
        print('*************************************************************************')
        print('Vencedor: Primer jugador. \t El segundo jugador ha sobrepasado los 21 puntos')
        print('*************************************************************************')
        fin = 'yes'
        break
    elif total2 <= 21 and total1 > 21:
        # Gana el segundo porque el primero se ha pasado
        print('*************************************************************************')
        print('Vencedor: Segundo jugador. \t El primer jugador ha sobrepasado los 21 puntos')
        print('*************************************************************************')
        fin = 'yes'
        break
    elif total1 > 21 and total2 > 21:
        # Empate
        print('*************************************************************************')
        print('Los dos jugadores han perdido por superar los 21 puntos')
        print('*************************************************************************')
        fin = 'yes'
        break
    # En caso contrario aun hay que seguir:
    # Solo en el caso de que el jugador haya tirado el dado, preguntamos si quiere seguir jugando
    if resp1 == 'S' or resp1 == 's':
        resp1 = input('Jugador 1: Para lanzar el dado pulsa S o s, otra tecla para terminar: ')
    if resp2 == 'S' or resp2 == 's':
        resp2 = input('Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: ')
    print('-------------------------------------------------------------------------------')

# Mostraremos el resultado final salvo que ya se haya mostado (variable fin='yes')
# Hay múltiples posibilidades
if fin != 'yes':
    print('*************************************************************************')
    if total1 > total2 and total1 <= 21:
        # Ha ganado el primer jugador
        print('Vencedor: Primer jugador.\tResultado final:Jugador1:', total1, '- Jugador2:', total2)
    elif total1 < total2 and total2 <= 21:
        # Ha ganado el segundo jugador
        print('Vencedor: Segundo jugador.\tResultado final:Jugador1:', total1, '- Jugador2:', total2)
    else:
        # Ambos se han pasado de 20 puntos
        print('Los dos jugadores han perdido al haber sobrepasado los 20 puntos')
    print('*************************************************************************')
