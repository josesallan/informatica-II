# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio

# Definimos los paths de cada uno de los archivos de trabajo
path_fichero_ingles = directorio() + '/1.txt'
path_fichero_espanol = directorio() + '/traduccion.txt'

# Abrimos los archivos de trabajo, el original en modo lectura, el destino lectura/escritura y borrado
fichero_ingles = open(path_fichero_ingles, 'r')
fichero_espanol = open(path_fichero_espanol, 'w+')

# A través de un for gestionamos cada una de las líneas del archivo origen
for linea_a_traducir in fichero_ingles:
    # Mostramos la línea a traducir
    print(linea_a_traducir)
    # Solicitamos la traducción
    traduccion = input('Traducción línea:')
    # Escribimos la traducción en el archivo de destion
    fichero_espanol.write(traduccion + '\n')

# Llevamos el puntero al comienzo para poder leer
fichero_espanol.seek(0)

# Mostramos el resultado
for linea in fichero_espanol:
    print(linea.rstrip())
