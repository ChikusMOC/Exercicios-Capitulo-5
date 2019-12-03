"""
Exercicio 36 -
"""


vendamensal = float(input('Digite o valor vendido no mês: '))

if vendamensal >= 100000:
    comissao = 700 + vendamensal * 0.16
elif vendamensal >= 80000 and vendamensal < 100000:
    comissao = 650 + vendamensal * 0.14
elif vendamensal >= 60000 and vendamensal < 80000:
    comissao = 600 + vendamensal * 0.14
elif vendamensal >= 40000 and vendamensal < 60000:
    comissao = 550 + vendamensal * 0.14
elif vendamensal >= 20000 and vendamensal < 40000:
    comissao = 500 + vendamensal * 0.14
elif vendamensal < 20000:
    comissao = 400 + vendamensal * 0.14
else:
    print('Algo deu errado, reinicie o sistema.')

print(f'Comissão = {comissao}')
