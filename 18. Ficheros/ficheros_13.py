# Solicitamos por teclado el texto_a_codificar a encriptar
texto_a_codificar = input('Introduce el texto a encriptar: ')

# Solicitamos por teclado la clave a utilizar (será un número entero)
clave = int(input('Introduce la clave de encriptación: '))

#Inicializamos una variable que almacenará el texto_a_codificar resultante
texto_codificado = ''

#Comenzamos el proceso de codificación leyendo cada uno de los caracteres del texto original
for caracter in texto_a_codificar:
    # Calculamos el nuevo código ascii del caracter codificado
    codigo_ascii = ord(caracter) + clave
    # Seleccionamos el caracter ascii correspondiente al nuevo código
    nuevo_caracter = chr(codigo_ascii)
    # Añadimos el nuevo caracter a la cadena codificad
    texto_codificado = texto_codificado + nuevo_caracter

# Mostramos el texto codificado por pantalla
print(texto_codificado)
