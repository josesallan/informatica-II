import fechas  # Importamos nuestro módulo de gestión de fechas

print("--- VALIDADOR DE FECHAS Y CALCULADORA DE DÍAS ---")

# Bucle de validación: solicita la fecha hasta que es_fecha_valida() devuelva True
while True:
    dia = int(input("Introduce el día (DD): "))
    mes = int(input("Introduce el mes (MM): "))
    anyo = int(input("Introduce el año (AAAA): "))

    if fechas.es_fecha_valida(dia, mes, anyo):
        break  # La fecha es válida, salimos del bucle

    print("  [!] Fecha incorrecta. Revisa los datos e inténtalo de nuevo.\n")

# Una vez validada la fecha, realizamos las comprobaciones y cálculos
bisiesto = fechas.es_bisiesto(anyo)
if bisiesto:
    texto_bisiesto = "Sí"
else:
    texto_bisiesto = "No"

dia_numero = fechas.dia_del_anyo(dia, mes, anyo)

# Mostramos el informe final
print("\n" + "=" * 40)
print("             INFORME DE FECHA")
print("=" * 40)
print(f"• Fecha introducida: {dia:02d}/{mes:02d}/{anyo}")
print(f"• ¿El año {anyo} es bisiesto?: {texto_bisiesto}")
print(f"• Corresponde al día número: {dia_numero} del año")
