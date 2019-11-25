"""
Exercicio 6
"""


num1 = int(input('1º numero: '))
num2 = int(input('2º numero: '))

if num1 > num2:
    print(f'1º numero é maior que 2º numero com uma diferença de {num1-num2}')
elif num2 > num1:
    print(f'2º numero é maior que 1º numero com uma diferença de {num2-num1}')
else:
    print('são numeros iguais')
