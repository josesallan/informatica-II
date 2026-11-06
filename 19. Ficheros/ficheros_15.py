# Importamos el módulo pickle de la biblioteca estándar de Python
import pickle

# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio


# Creamos el path completo del archivo
path_mensaje_codificado = directorio() + '/mensaje_codificado.pkl'

# Abrimos el archivo en modo lectura binaria
archivo_codificado = open(path_mensaje_codificado, 'rb')

# Leelmos la información del archivo y la guardamos en una variable
texto_codificado = pickle.load(archivo_codificado)

# Cierro el archivo (ya no lo voy a necesitar)
archivo_codificado.close()

# Inicio una variable para almacenar el texto recuperado
texto_decodificado = ''
print('Texto a desencriptar:')
print(texto_codificado)

# Solicitamos la clave de encriptación (número entero)
clave = int(input('Introduce la clave de desencriptación: '))

# Comenzamos el proceso de decodificación leyendo cada uno de los caracteres del texto encriptado
for caracter in texto_codificado:
    # Calculamos el nuevo código ascii del caracter decodificado
    caracter_decodificado = chr(ord(caracter) - clave)
    # Seleccionamos el caracter ascii correspondiente al nuevo código
    texto_decodificado = texto_decodificado + caracter_decodificado
print('Texto desencriptado:')
print(texto_decodificado)
