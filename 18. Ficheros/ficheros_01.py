def directorio():
    # Función que devuelve la dirección del módulo que está ejecutando dicha función

    # Este valor es útil cuando se trabaja con órdenes de gestión de ficheros para poder definir
    # la dirección del archivo a utilizar.

    import os
    # dirección absoluta completa del módulo en el que se está trabajando
    ruta_modulo = os.path.abspath(__file__)
    # nombre del directorio que contiene el archivo activo:
    directorio_modulo = os.path.dirname(ruta_modulo)

    # La función devuelve el path del archivo que la ejecuta.
    return directorio_modulo