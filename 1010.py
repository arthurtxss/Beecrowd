codigo = int(input(''))
quantidade = int(input(''))
valor_peca = float(input(''))
codigo2 = int(input(''))
quantidade2 = int(input(''))
valor_peca2 = float(input(''))
valor_final = (quantidade * valor_peca) + (quantidade2* valor_peca2)

print(f'VALOR A PAGAR: R$ {valor_final:.2f}')