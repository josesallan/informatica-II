# Importamos el módulo pickle de la biblioteca estándar de Python
import shelve

# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio

# Gestionamos la lista de mejores puntuaciones
# Se guardarán en un fichero con nombre mejores_puntuaciones_tragaperras

# Montamos el path completo del archivo a gestionar
# Creamos el path completo del archivo
path_best_scores = directorio() + '/mejores_puntuaciones_tragaperras'
best_scores = shelve.open(path_best_scores)


# Creamos una función que muestre las mejores marcas.
def mejores_marcas():
    print("\n   1º", best_scores['1']['nombre'], (12 - len(best_scores['1']['nombre'])) * " ", end='')
    print((8 - len(str(best_scores['1']['score']))) * " ", str('{0:.2f}'.format(best_scores['1']['score'])) + '€')
    print("   2º", best_scores['2']['nombre'], (12 - len(best_scores['2']['nombre'])) * " ", end='')
    print((8 - len(str(best_scores['2']['score']))) * " ", str('{0:.2f}'.format(best_scores['2']['score'])) + '€')
    print("   3º", best_scores['3']['nombre'], (12 - len(best_scores['3']['nombre'])) * " ", end='')
    print((8 - len(str(best_scores['3']['score']))) * " ", str('{0:.2f}'.format(best_scores['3']['score'])) + '€')


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

print("\n Bienvenido al juego del tragaperras")
print(" ===================================\n")
print(" - En este momento las mejores marcas son:")
mejores_marcas()
print()
nombre = input(' ¿Cómo te llamas? ')
while dinero <= 0:
    dinero = float(input('\n ¿Que cantidad quieres apostar (€)? '))

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

# Calculo la ganancia como la diferencia entre el premio conseguido y el dinero inicial.
ganancia = (premio - dinero)
if ganancia > best_scores['1']['score']:
    best_scores['3'] = best_scores['2']
    best_scores['2'] = best_scores['1']
    best_scores['1'] = {'score': ganancia, 'nombre': nombre}
elif ganancia > best_scores['2']['score']:
    best_scores['3'] = best_scores['2']
    best_scores['2'] = {'score': ganancia, 'nombre': nombre}
elif ganancia > best_scores['3']['score']:
    best_scores['3'] = {'score': ganancia, 'nombre': nombre}
else:
    print("Tu puntuación no está entre las tres más altas")

mejores_marcas()

