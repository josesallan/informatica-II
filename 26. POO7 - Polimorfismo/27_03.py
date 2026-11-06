# =============================================================================
# EJERCICIO 3: EL CONTRATO ESTRICTO (Nivel Profesional)
# =============================================================================

# 1. LA SUPERCLASE (Nuestro contrato estricto)
class Empleado():
    def trabajar(self):
        # En lugar de usar 'pass' y quedarnos callados si alguien olvida este método,
        # lanzamos un error intencionado. Así obligamos a que todas las clases
        # hijas cumplan nuestra norma: "Todo empleado debe saber trabajar".
        raise NotImplementedError("¡Alerta de Seguridad! Has olvidado definir cómo trabaja este empleado.")


# 2. LAS SUBCLASES
# Esta clase SÍ cumple el contrato.
class Programador(Empleado):
    # Sobrescribimos el método correctamente.
    def trabajar(self):
        print("💻 Programador: Escribiendo código en Python a toda velocidad...")


# Esta clase NO cumple el contrato (fingimos que se nos ha olvidado).
class Gerente(Empleado):
    # ¡Ups! Se nos ha olvidado definir el método trabajar().
    # Como hereda de Empleado, si intentamos usar trabajar(), saltará el error.
    pass


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

print("Iniciando el sistema de gestión de la empresa...\n")

# 1. Probamos al empleado que sí hace las cosas bien
mi_programador = Programador()
print("Dando la orden al programador:")
mi_programador.trabajar()
# Resultado: Todo perfecto, funciona como la seda.

print("\n" + "-" * 50 + "\n")

# 2. Probamos al empleado al que le falta código
mi_gerente = Gerente()
print("Dando la orden al gerente (preparaos para el error):\n")

# ¡ATENCIÓN! Al ejecutar esta línea, el programa se detendrá y mostrará en rojo
# el texto que nosotros mismos hemos escrito en el NotImplementedError.
mi_gerente.trabajar()

print("Esta línea nunca se llegará a imprimir porque el programa se ha detenido por seguridad.")
