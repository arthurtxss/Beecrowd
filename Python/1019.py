tempo = int(input())
segundos =0
minutos =0
horas = 0
horas = tempo//3600
minutos = (tempo%3600)//60
segundos = tempo%60

print(f"{horas}:{minutos}:{segundos}")