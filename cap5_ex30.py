"""
Exercicio 30 - Faça um programa que receba três numeros e mostre-os em ordem crescente.
"""


val1 = int(input('Numero inteiro: '))
val2 = int(input('Numero inteiro: '))
val3 = int(input('Numero inteiro: '))

for i in range(3):
    if val1 > val2:
        val1, val2 = val2, val1
    elif val1 > val3:
        val1, val3 = val3, val1
    elif val2 > val3:
        val2, val3 = val3, val2

print(f' ordem crescente {val1}, {val2}, {val3}')
