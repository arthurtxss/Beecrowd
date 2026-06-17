valor_1, valor_2, valor_3 = input().split()
valor_1= float(valor_1)
valor_2= float(valor_2)
valor_3= float(valor_3)

pi = 3.14159

triangulo = (valor_1 * valor_3)/2
circulo = (valor_3**2)*pi
trapezio = ((valor_1 + valor_2)* valor_3)/2
quadrado = valor_2**2
retangulo = valor_1* valor_2
print(f"TRIANGULO: {triangulo:.3F}")
print(F"CIRCULO: {circulo:.3F}")
print(F"TRAPEZIO: {trapezio:.3F}")
print(F"QUADRADO: {quadrado:.3F}")
print(F'RETANGULO: {retangulo:.3F}')