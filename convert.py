### Função que formata texto
from datetime import datetime, date
#from str import casefold, lower

def formata(texto):
    txt = texto.str.casefold()
    return txt

def minuscula(texto):
    txt = texto.str.lower()
    return txt

def converte_data(valor):
    #dt = valor.str.split('/')
    #return datetime(int(dt[2]),int(dt[1]),int(dt[0]))
    return valor.strftime('%y-%m-%d') 

def convert(data):
    dt = data.split('/')
    return datetime(
        int(2),
        int(1),
        int(0)
    )