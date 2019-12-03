"""
Exercicio 40 -
"""

custo = float(input("Digite o custo de fabrica: "))

if custo <= 12000:
    custo = custo * 1.05
elif custo > 12000 and custo <= 25000:
    custo = custo * 1.25
else:
    custo = custo * 1.35
print(f'Valor final pro consumidor = {custo}')
