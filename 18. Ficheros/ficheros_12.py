# Importamos el módulo pickle de la biblioteca estándar de Python
import pickle

# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio

# Iniciamos el proceso de lectura en el archivo notas.pkl

# Construimos el path completo del fichero a abrir o crear
fichero = directorio() + '/notas.pkl'

# Abrimos el archivo del que vamos a leer los datos en formato binario,
fichero = open(fichero, 'rb')

# Escribimos la información, que es un diccionario.  La asociamos a una variable
notas = pickle.load(fichero)

# Cerramos el fichero (no lo vamos a volver a necesitar)
fichero.close()

# Mostramos la información, a través de un bucle que leerá cada una de las claves del diccionario
# y su valor asociado:
for materia in notas:
    print(materia, end='')
    longitud = len(materia)
    huecos = 15- len(materia)
    print(huecos * ' ', end='')
    print('->', notas[materia])