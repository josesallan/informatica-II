# random102
# José Antonio Sallán

# Importamos del módulo random de la librería estándar
import random
# Creo la variable terminar.  Su función es guardar la información sobre el fin de la
# partida.  Si el valor es 'n' el juego no termina.  En cualquier otro caso si.
# El valor inicial de terminar es 's' para conseguir que al comenzar el juego la condición
# del bucle inicial sea cierta y con ello se genere una primera lista de números
# y se pregunte sobre la continuidad o no de la partida.
terminar = 's'

# El bucle termina cuando contesto n o N
while terminar != 'n':
    # Genero los tres números al azar con randint
    # No puedo utilizar random.sample porque los números se pueden repetir
    n1 = random.randint(1, 5)
    n2 = random.randint(1, 5)
    n3 = random.randint(1, 5)
    print('---------------------')
    print('Tirada:\t| ' + str(n1) + ' | ' + str(n2) + ' | ' + str(n3) + ' |')
    print('---------------------')
    # En esta parte vamos a detectar cuantos números iguales hemos obtenido en la tirada
    if n1 == n2 and n2 == n3:
        print('Los tres números son iguales')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Dos de los tres números son iguales')
    else:
        print('Los tres números son distintos')

    terminar = input('Pulsa n para terminar, otra tecla para volver a jugar: ')
print('Programa terminado')
