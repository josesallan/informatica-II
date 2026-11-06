# Importamos el módulo pickle de la biblioteca estándar de Python
import pickle

# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio

# Solicitamos por teclado el texto_a_codificar a encriptar
texto_a_codificar = input('Introduce el texto a encriptar: ')

# Solicitamos por teclado la clave a utilizar (será un número entero)
clave = int(input('Introduce la clave de encriptación: '))

# Inicializamos una variable que almacenará el texto_a_codificar resultante
texto_codificado = ''

# Comenzamos el proceso de codificación leyendo cada uno de los caracteres del texto original
for caracter in texto_a_codificar:
    # Calculamos el nuevo código ascii del caracter codificado
    codigo_ascii = ord(caracter) + clave
    # Seleccionamos el caracter ascii correspondiente al nuevo código
    nuevo_caracter = chr(codigo_ascii)
    # Añadimos el nuevo caracter a la cadena codificado
    texto_codificado = texto_codificado + nuevo_caracter

# Mostramos el texto codificado por pantalla
print(texto_codificado)

# ------------------Iniciamos el proceso de grabado de la información --------------- #

# Creamos el path completo del archivo
path_mensaje_codificado = directorio() + '/mensaje_codificado.pkl'

# Abrimos el archivo
archivo_codificado = open(path_mensaje_codificado, 'wb')
pickle.dump(texto_codificado, archivo_codificado)

# Ciero el archivo
archivo_codificado.close()