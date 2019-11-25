"""
Exercicio 25
"""
import sys


class RaizEquacao:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def delta(self):
        aux = self.b**2 - 4 * self.a * self.c
        if aux < 0:
            print('Não existe raiz')
        elif aux == 0:
            print(f'{((-self.b+aux**0.5)/2*self.a)} Raiz Unica')
        else:
            aux = aux**0.5
            print(f'As raizes são {(((-self.b)+aux)/2*self.a):.2f} e {(((-self.b)-aux)/2*self.a):.2f}')

    def verifica(self):
        if self.a == 0:
            print(f'Não é equação de segundo grau. Pois {self.a}x² = 0')
            sys.exit()
        else:
            print('Iniciando a equação.')


a = int(input("Valor de 'a': "))
b = int(input("Valor de 'b': "))
c = int(input("Valor de 'c': "))
equacao = RaizEquacao(a, b, c)
equacao.verifica()
equacao.delta()
