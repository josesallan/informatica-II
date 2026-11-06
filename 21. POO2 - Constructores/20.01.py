# Definimos la clase Alumno
class Alumno():

    # Utilizamos un método constructor para definir las propiedades de los objetos de la clase
    # El método recibirá como parámetros los valores iniciales de las propiedades name y score
    def __init__(self, name, score):
        self.nombre = name
        self.nota = score

    # Definimos el método que imprimirá por pantalla las propiedades de los objetos de la clase
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    # Defiimos el método que informará sobre el aprobado/suspenso de un objeto de la clase
    def aprobado(self):
        if self.nota >= 5:
            return "En alumno ha aprobado"
        else:
            return "El alumno ha suspendido"


# ------------------ Programa principal --------------------#

# Creo un objeto de la clase Alumno, envío como parámetros los valores de las propiedades
# nombre y nota a asignar al objeto.
alumno1 = Alumno("Lucas", 7)

# Mostramos las propiedades del objeto llamando al método imprimir.
alumno1.imprimir()
# Informamos sobre el aprobado/suspenso del alumno llamando al método aprobado
print(alumno1.aprobado())
