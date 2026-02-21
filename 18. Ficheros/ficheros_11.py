# Importamos el módulo pickle de la biblioteca estándar de Python
import pickle

# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio


# Preguntamos por la califiación obtenida en cada materia
nota_mates = int(input('Calificación Matemáticas:'))
nota_lengua = int(input('Calificación Lengua:'))
nota_historia = int(input('Calificación Historia:'))
nota_info = int(input('Calificación Informática II:'))

# Creamos un diccionario vacío
notas = {}
# Añadimos los valores al diccionario
notas['Matemáticas'] = nota_mates
notas['Lengua'] = nota_lengua
notas['Historia'] = nota_historia
notas['Informática II'] = nota_info

# Iniciamos el proceso de escritura en el archivo notas.pkl

# Construimos el path completo del fichero a abrir o crear
fichero = directorio() + '/notas.pkl'

# Abrimos el archivo donde vamos a escribir los datos en formato binario,
fichero = open(fichero, 'wb')

# Escribimos la información
pickle.dump(notas, fichero)

# Cerramos el fichero
fichero.close()
