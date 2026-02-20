# random103
# José Antonio Sallán

# Importamos del módulo random de la librería estándar
import random
# Creo la variable terminar.  Su función es guardar la información sobre el fin de la
# partida.  Si el valor es 'n' el juego no termina.  En cualquier otro caso si.
# El valor inicial de terminar es 's' para conseguir que al comenzar el juego la condición
# del bucle inicial sea cierta y con ello se genere una primera lista de números
# y se pregunte sobre la continuidad o no de la partida.
terminar = 's'

# Comenzamos preguntando por la cantidad que el jugador quiere apostar
dinero = 0
# En otra variable acumularemos el premio
premio = 0
while dinero <= 0:
    dinero = float(input('¿Que cantidad quieres apostar (€)? '))

# Bucle principal
# El bucle termina cuando contesto n
# Defino una nueva variable que almacena el dinero que tengo antes de jugar
antesDeJugar = dinero
while terminar != 'n':
    # Genero los tres números al azar con randint
    # No puedo utilizar random.sample porque los números se pueden repetir
    n1 = random.randint(1, 5)
    n2 = random.randint(1, 5)
    n3 = random.randint(1, 5)
    print('---------------------')
    print('Tirada:\t| ' + str(n1) + ' | ' + str(n2) + ' | ' + str(n3) + ' |')
    print('---------------------')
    # En esta parte vamos a detectar cuantos números iguales hemos obtenido en la tirada y en función de ello
    # calculamos el premio

    # Tres números iguales, lo importante es el orden.  Debemos ir del caso más partícular al más general.
    if (n1 == n2 and n2 == n3 and n3 == 5):
        print('Has conseguido tres cincos.  Has multiplicado por diez tu dinero.')
        premio = 10 * antesDeJugar
    # Dos cincos
    elif (n1 == n2 and n1 == 5) or (n1 == n3 and n1 == 5) or (n2 == n3 and n2 == 5):
        print('Has conseguido dos cincos.  Has multiplicado por cuatro tu dinero.')
        premio = 5 * antesDeJugar
    # Un cinco.  Tenemos dos subcasos
    elif (n1 == 5 or n2 == 5 or n3 == 5):
        # Si los otros dos números son iguales
        if (n1 == n2 or n1 == n3 or n2 == n3):
            print('Has conseguido un cinco y dos números iguales.  Has multiplicado por tres tu dinero.')
            premio = 3 * antesDeJugar
        else:  # Si los otros dos números son distintos
            print('Has conseguido un cinco.  Recuperas tu dinero.')
            premio = antesDeJugar

    # tres números iguales
    elif n1 == n2 and n1 == n3 and n2 == n3:
        print('Los tres números son iguales.  Has multiplicado por cinco tu dinero.')
        premio = 5 * antesDeJugar
    # Dos números iguales
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Dos de los tres números son iguales.  Has duplicado tu dinero.')
        premio = 2 * antesDeJugar
    else:
        print('Los tres números son distintos.  Has perdido todo tu dinero.')
        premio = 0.00
        break
    print('¡Enhorabuena! Has ganado', premio - antesDeJugar, '€.  Ahora tienes', premio, '€.')
    antesDeJugar = premio
    terminar = input('Pulsa n para terminar, otra tecla para volver a jugar: ')
if premio > 0:
    print('Enhorabuena has ganado', premio - dinero, '€.')
else:
    print('Programa terminado.')
