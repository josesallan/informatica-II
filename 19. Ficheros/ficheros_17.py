# Importamos el módulo pickle de la biblioteca estándar de Python
import shelve

# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio


# Creamos el path completo del archivo
path_alumnos_centro = directorio() + '/alumnos_centro'

# Abrimos el archivo
alumnos_centro = shelve.open(path_alumnos_centro)

# Bucle que va a leer los codigos de todos los alumnos
for codigo in alumnos_centro:
    datos = alumnos_centro[codigo]
    nombre_completo = datos['nombre'] + " " + datos['apellidos']
    print(f"Código: {codigo} - Nombre: {nombre_completo} - Dirección: {datos['direccion']} - Curso: {datos['curso']}")
