"""
Exercicio 26 - Ler distancia em Km e quantidade de litros de gasolina consumidos por um carro em um percurso.
calcular o consumo em km/l e escrever mensagem de acordo com tabela.
----------------------------------------------
Consumo     |    (Km/l)  |    Mensagem        |
----------------------------------------------
menor que   |      8     |  Venda o carro!    |
----------------------------------------------
entre       |   8 e 14   |   Econômico!       |
----------------------------------------------
maior que   |      12    |  Super econômico!  |
----------------------------------------------
"""


class StatusCar:
    def __init__(self, km, consumo):
        self.km = km
        self.consumo = consumo

    def verifica(self):
        aux = self.km / self.consumo
        if aux < 8:
            print('Venda o Carro!')
        elif 8 <= aux <= 14:
            print('Econômico!')
        elif aux > 12:
            print('Super Econômico!')
        else:
            print('Algo deu errado')


distancia = float(input('Distancia percorrida: '))
consumo = float(input('Consumo realizado: '))
carro = StatusCar(distancia, consumo)
carro.verifica()
