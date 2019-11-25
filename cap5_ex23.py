"""
Exercicio 23
"""


class BiSexto:
    def __init__(self, ano):
        self.ano = ano

    def verifica(self):
        if self.ano % 400 == 0 or self.ano % 4 == 0 and self.ano % 100 != 0:
            print('Ano bissexto.')
        else:
            print('Ano informado não é bissexto.')


ano = int(input('Digite o ano: '))
bisexto = BiSexto(ano)
bisexto.verifica()
