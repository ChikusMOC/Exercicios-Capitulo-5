"""
Exercicio 27 - Escreva um programa que, dada a idade de um nadador, classifique-o em uma das categorias.

Infantil A - Idade (5 a 7)
Infantil B - Idade (8 a 10)
Juvenil A - Idade (11 a 13)
Juvenil B - Idade (14 a 17)
Sênior - Idade (Maiores de 18 anos)
"""


class Nadador:
    def __init__(self, idade):
        self.idade = idade

    def verifica(self):
        if 5 <= self.idade <= 7:
            print(f'Infantil A idade - {self.idade}')
        elif 8 <= self.idade <= 10:
            print(f'Infantil B idade - {self.idade}')
        elif 11 <= self.idade <= 13:
            print(f'Juvenil A idade - {self.idade}')
        elif 14 <= self.idade <= 17:
            print(f'Juvenil B idade - {self.idade}')
        elif self.idade >= 18:
            print(f'Sênior idade - {self.idade}')
        else:
            print('Idade informada não se adequa à tabela existente.')


idade = int(input('Digite sua idade: '))
nadador = Nadador(idade)
nadador.verifica()
