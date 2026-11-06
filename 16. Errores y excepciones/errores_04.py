'''4. Crea un programa que solicite dos números enteros por pantalla y muestre el
resultado de su suma. En caso de que uno de los valores introducidos sea una
cadena de caracteres el programa debe gestionar el error informando de la
causa y solución.'''

# El bloque try solicita los dos valores, que tinenen que ser enteros.
# En caso de no serlos se generará un error tipo ValueError que gestionaremos a través de un except

# Ten en cuenta que el código que realiza la suma y muestra el resultado debe de estar dentro del try
# ya que en caso de generarse el error val1 y/o val2 no estarían definidas y al intentar encontrar la suma
# se generaría otro tipo de error que no estaría gestionado e interrumpiría la ejecución del programa.

try:
    val1 = int(input("Introduce el primer valor: "))
    val2 = int(input("Introduce el segundo valor: "))
    suma = val1 + val2
    print(val1, "+", val2, "=", suma)
except ValueError:
    print("El valor introducido no es un número entero")
