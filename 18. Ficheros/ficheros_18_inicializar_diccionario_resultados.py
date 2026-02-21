# Importamos el módulo pickle de la biblioteca estándar de Python
import shelve

# Importamos desde el módulo ficheros_01 a función directorio
# Esta función devuelve una cadena de texto con el directorio del archivo ejecutado
from ficheros_01 import directorio

# Montamos el path completo del archivo a gestionar
# Creamos el path completo del archivo
path_best_scores = directorio() + '/mejores_puntuaciones_tragaperras'

# Creamos un diccionario shelve vacío que recibirá las puntuaciones.
best_scores = shelve.open(path_best_scores)

# Añadimos tres datos vacíos para inicializar el diccionario

best_scores['1'] = {'score': 0, 'nombre': '------------'}
best_scores['2'] = {'score': 0, 'nombre': '------------'}
best_scores['3'] = {'score': 0, 'nombre': '------------'}

print(best_scores)
for marcas in best_scores:
    print(marcas, best_scores[marcas])