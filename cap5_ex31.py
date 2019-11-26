"""
Exercicio 31
"""


class Classificacao:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso

    def verifica(self):
        if self.altura < 1.2:
            if self.peso < 60:
                print('Categoria A')
            elif 60 <= self.peso <= 90:
                print('Categoria D')
            elif self.peso > 90:
                print('Categoria G')
            else:
                print('Categoria não encontrada.')
        elif 1.2 <= self.altura <= 1.7:
            if self.peso < 60:
                print('Categoria B')
            elif 60 <= self.peso <= 90:
                print('Categoria E.')
            elif self.peso > 90:
                print('Categoria H.')
            else:
                print('Categoria não encontrada')
        elif self.altura > 1.7:
            if self.peso < 60:
                print('Categoria C')
            elif 60 <= self.peso <= 90:
                print('Categoria F.')
            elif self.peso > 90:
                print('Categoria I.')
            else:
                print('Categoria não encontrada')
        else:
            print('Altura não se enquadra na tabela existente.\nCategoria não encontrada.')


def altura():
    while True:
        try:
            aux = input('Informe sua altura em metros, exemplo "1.65": ')
            aux = aux.replace(',', '.')
            aux = float(aux)
            return aux
        except ValueError:
            print('Você digitou algo errado, tente novamente')


def peso():
    while True:
        try:
            aux = input('Informe seu peso em kilos, exemplo "65.6": ')
            aux = aux.replace(',', '.')
            aux = float(aux)
            return aux
        except ValueError:
            print('Você digitou algo errado, tente novamente')


altura = altura()
peso = peso()
categoria = Classificacao(altura, peso)
categoria.verifica()


