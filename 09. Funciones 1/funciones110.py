def print_asegundos(horas, minutos, segundos):
    valor = (horas * 60 + minutos) * 60 + segundos
    print(valor, 'segundos')


h = int(input('¿Horas?'))
m = int(input('¿Minutos?'))
s = int(input('¿Segundos?'))
print_asegundos(h, m, s)
