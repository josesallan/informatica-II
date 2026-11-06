# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio

# Solicitamos los datos del archivo
titulo = input('Título de la canción: ')
autor = input('Nombre del autor: ')

# Construimos el path completo del archivo de origen
nombreorigen = directorio() + '/1.txt'

# Construimos el path completo del archivo de destion
nombrefichero = directorio() + '/' + titulo + '.txt'

# Abrimos el archivo de origen en modo por defecto (lectura, r)
origen = open(nombreorigen)

# Abrimos el archivo de destion en modo escritura/lectura (si existe, borra el contenido)
destino = open(nombrefichero, 'w+')

# Escribimos la primera lína con el nombre del título y el autor
destino.write(titulo + ' - ')
destino.write(autor + '\n')

# A través de un for leemos cada una de las líneas y la escribimos en el destino
for linea_origen in origen:
    destino.write(linea_origen)

'''Como acabamos de escribir en dicho archivo, el puntero está al destino del texto.
Si leemos diretamente a través de un for no se mostará el contenido ya que necesitamos
llevar el puntero al inicio.

Esto lo podemos hacer de dos formas:
    1. Volviendo a abrir el archivo en modo lectura
    2. Utilizando la función seek para llevarlo a la posición 0
En este ejemplo lo haremos con la función seek'''
destino.seek(0)

for linea_destino in destino:
    print(linea_destino.rstrip())
