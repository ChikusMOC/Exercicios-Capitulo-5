"""
Exercicio 19
"""


def _divisor(i):
    if i % 3 == 0 and i % 5 != 0:
        print('numero divisivel por 3')
    elif i % 5 == 0 and i % 3 != 0:
        print('numero divisivel por 5')
    else:
        print('numero informado quebrou alguma regra.')


num = int(input("Digite um numero: "))
_divisor(num)
