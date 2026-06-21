Valor = float(input())
a = 0
while ((Valor//100)%99): 
    Valor -100
    a=a+1
    
print(f"{a} nota(s) de 100")