# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio

# Definimos el path del archivo de trabajo
path_fichero_coordenadas = directorio() + '/coordenadas.txt'

# Abrimos el contenido en modo lectura, aplicamos el método readlines para leer su contenido
# y guardamos el resultado de la lectura como lista en la variable datos_disparos
datos_disparos = open(path_fichero_coordenadas, 'r').readlines()

''' A través de un for vamos a ir leyendo cada una de las líneas.
Cada pasada por el for, formatea los datos contenidos en la línea activa para mostrar
los datos con el formato deseado'''
for linea in datos_disparos:
    ''' Todas las líneas se comportan como una lista (cadena de texto) y tienen el mismo formato:
        - El valor de la coordenada x comienza en la posición 1 y termina en la posición 5)
        - El valor de la coordandad y comienza en la posición 6 y termina en la posición 10).
    Leeremos dichos datos, teniendo en cuenta de que se más adelante los trataremos como números
    por lo que los transformaremos en datos float'''

    # 1. Extraemos las coordenadas del disparo actual
    x_disparo = linea[1:5]
    y_disparo = linea[6:10]

    # 2. Mostramos datos disparo por pantalla
    print('X =', x_disparo, '- Y =', y_disparo)
