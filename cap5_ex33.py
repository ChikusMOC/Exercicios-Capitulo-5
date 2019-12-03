"""
Exercicio 33 - Leia o preço antigo, calcule e escreva o preço novo junto com uma mensagem
(de acordo com tabela apresentada)
"""

preco_novo = 0

preco = int(input('Valor: '))
if preco < 50:
    preco_novo = preco * 1.05
elif 50 <= preco <= 100:
    preco_novo = preco * 1.1
elif preco > 100:
    preco_novo = preco * 1.15
else:
    print('Você chegou onde não devia com esse valor.')

if preco_novo < 80:
    print(f'Preço novo = {preco_novo:.2f}. Barato.')
elif 80 <= preco_novo <= 120:
    print(f'Preço novo = {preco_novo:.2f}. Normal.')
elif 120 < preco_novo <= 200:
    print(f'Preço novo = {preco_novo:.2f}. Caro.')
elif preco_novo > 200:
    print(f'Preço novo = {preco_novo:.2f}. Muito Caro.')
else:
    print('Isso não deveria aparecer.')
