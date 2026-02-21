# Importamos el módulo pickle de la biblioteca estándar de Python
import shelve

# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio


# Creamos el path completo del archivo
path_alumnos_centro = directorio() + '/alumnos_centro'

# Abrimos el archivo
alumnos_centro = shelve.open(path_alumnos_centro)

# Código sencillo para introducir alumnos mientras no salgamos del bucle
while True:
    codigo = input("Introduce el código de la matrícula del alumno (o 'fin' para terminar): ")
    if codigo.lower() == "fin":
        break
    nombre = input("Introduce el nombre del alumno: ")
    apellidos = input("Introduce los apellidos del alumno: ")
    direccion = input("Introduce la dirección del alumno: ")
    curso = input("Introduce el curso del alumno: ")

    alumnos_centro[codigo] = {
        'nombre': nombre,
        'apellidos': apellidos,
        'direccion': direccion,
        'curso': curso
    }
    print("Alumno añadido correctamente.\n")
print("Programa finaliado correctamente")
