# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio

# Construimos el path completo del archivo a abrir
ruta_origen = directorio() + '/1.txt'

# En una mimsa línea abriremos el archivo origen y lo leeremos con la función read
# El objeto fichero será pues una cadena de texto (y por lo tanto una lista)
fichero = open(ruta_origen).read()

# Mostramos los caracteres deseados
print(fichero[10: 17])

# A través de un for leemos de nuevo los caracteres, cada print finaliza con un retorno de carro
# con ello el texto quedará en vertical
for car in range(10, 17, 1):
    # La función upper aplicada a un caracter devuelve la versión en mayúsculas del mismo
    print(fichero[car].upper())