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
notas['Informática II']= nota_info

# Calcularemos la nota media a través de un for que lea todos los valores
# Definimos una variable para guardar el valor suma de todas las notas
suma_notas = 0

# A través de un for leemos las notas almacenadas en el diccionario notas y sumamos sus valores
for nota in notas:
    suma_notas = suma_notas + notas[nota]

# Calculamos la media dividiendo el total por en número de elementos en el diccionario
nota_media = suma_notas / len(notas)

# Mostramos el resultado por pantalla
print('Nota media:', '{0:.2f}'.format(nota_media))
