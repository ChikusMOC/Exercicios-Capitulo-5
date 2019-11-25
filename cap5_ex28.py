"""
Exercicio 28 - Faça um programa que leia três numeros inteiros positivos e efetue o cálculo de uma das
seguintes medidas de acordo com um valor numérico digitado pelo usuário;

1 - Geométrica: (valx * valy * valz) ** (1/3)
2 - Ponderada: (valx + (2 * valy) + (3 * valz)) / 6
3 - Harmônica: 1 / ((1 / valx) + (1 / valy) + (1 / valz))
4 - Aritmética: (valx + valy + valz) / 3
"""


class Metodos:

    def __init__(self, valx, valy, valz):
        self.valx = valx
        self.valy = valy
        self.valz = valz

    def geometrica(self):
        aux = (self.valx * self.valy * self.valz) ** (1/3)
        print(f'Geométrica = {aux:.2f}')

    def ponderada(self):
        aux = (self.valx + (2 * self.valy) + (3 * self.valz)) / 6
        print(f'Ponderada = {aux:.2f}')

    def harmonica(self):
        aux = 1 / ((1 / self.valx) + (1 / self.valy) + (1 / self.valz))
        print(f'Harmônica = {aux:.2f}')

    def aritmetica(self):
        aux = (self.valx + self.valy + self.valz) / 3
        print(f'Aritmética = {aux:.2f}')


valx = int(input('Valor de x: '))
valy = int(input('Valor de y: '))
valz = int(input('Valor de z: '))
op = int(input('1 - Geométrica;\n2 - Ponderada;\n3 - Harmônica;\n4 - Aritmética\nSua opção é: '))
equacao = Metodos(valx, valy, valz)
if op == 1:
    equacao.geometrica()
elif op == 2:
    equacao.ponderada()
elif op == 3:
    equacao.harmonica()
elif op == 4:
    equacao.aritmetica()
else:
    print('Você selecionou uma opção que não existe!')
