# la función aSegundos transforma un tiempo dado en función de tres argumentos
# (horas, minutos y segundos) a formato segundos.
def aSegundos(horas, minutos, segundos):
    segTot = (horas * 60 + minutos) * 60 + segundos
    return segTot


# la función hhmmss transforma un tiempo dado en segundos a su equivalente en
# horas, minutos y segundos.  La función devuelve estos datos como variables
# independientes
def hhmmss(segundos):
    ss = segundos % 60
    mm = segundos // 60
    hh = mm // 60
    mm = mm % 60
    return hh, mm, ss
