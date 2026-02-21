# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio

# Construimos el path completo del archivo a leer
path_fichero_origen = directorio() + '/1.txt'

# Construimos el path completo del archivo a crear
path_fichero_destino = directorio() + '/4.txt'

# Abrimos el archivo origen en modo lectura
fichero_origen = open(path_fichero_origen, 'r')

# Abrimos el fichero destino en modo escritura y lectura (con vaciado previo)
fichero_destino = open(path_fichero_destino, 'w+')

# Realizamos la copia leyendo cada una de las líneas del origen y escribiendolas de una en una en el destino
# Para ello utilizamos un bucle
for linea in fichero_origen:
    fichero_destino.write(linea)
fichero_origen.close()

# Posicionamos el puntero en la posición deseada
fichero_destino.seek(10)
# Escribimos el nuevo texto (con sustitución)
fichero_destino.write('ser rey')
# Llevamos el puntero al inicio para poder leer el contenido.
fichero_destino.seek(0)
# Mostramos el contenido por pantalla a través de un for
for linea in fichero_destino:
    # El método rstrip elimina el final de línea del texto a escribir
    # Esto es necesario para evitar que haya controlar la separación entre líneas (el print añada ya una.)
    print(linea.rstrip())
