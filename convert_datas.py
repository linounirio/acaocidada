# criando função que converte data
from datetime import datetime

def converte_data(valor):
    dt = valor.split('/')
    return datetime(
        int(dt[2]),
        int(dt[1]),
        int(dt[0])
    )

def convert(data):
    dt = data.split('/')
    return datetime(
        int(2),
        int(1),
        int(0)
    )