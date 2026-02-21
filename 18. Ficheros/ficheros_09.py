# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio


# Definimos dos variables para guardar la suma de las coordanadas x e y de los disparos.
sumatorio_x = 0
sumatorio_y = 0

# Definimos una variabla para guardar el número de disparos realizados
disparos_realizados = 0


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

    ''' Modificaciones ejercicio 8 sobre el 7:
    - Debemos tratar los valores como números decimales. Por lo tanto los transformaremos aplicando float'''
    # 1. Extraemos las coordenadas del disparo actual
    x_disparo = float(linea[1:5])
    y_disparo = float(linea[6:10])

    # Calculamos la media acumulada de las coordenadas x e y
    sumatorio_x = sumatorio_x + x_disparo
    sumatorio_y = sumatorio_y + y_disparo
    disparos_realizados = disparos_realizados + 1
    x_media = sumatorio_x / disparos_realizados
    y_media = sumatorio_y / disparos_realizados

    # Calculamos el error medio acumulado como la distancia entre las coordenadas medias
    # y el centro de la diana que está en el punto de coordenadas 4,4
    error = ((x_media - 4) ** 2 + (y_media - 4) ** 2) ** (1 / 2)

    # Mostraremos los resultados para la línea, aplicando formato de dos decimales para el
    # disparo actual y 3 para el acumulado

    print('Disparo ' + str(disparos_realizados) + ':    ', end='')
    print('x =', '{0:.2f}'.format(x_disparo), end='')
    print(' y =', '{0:.2f}'.format(y_disparo), end='')
    print('      xmed =', '{0:.3f}'.format(x_media), 'ymed =', '{0:.3f}'.format(y_media), end='')
    print("   Error:", '{0:.3f}'.format(error))


