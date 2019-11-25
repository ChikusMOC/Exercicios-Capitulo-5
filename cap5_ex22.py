"""
Exercicio 22
"""


class Aposentar:

    def __init__(self, idade, trabalho):
        self.idade = idade
        self.trabalho = trabalho

    def verificar(self):
        if self.idade >= 65:
            print('Pode se aposentar pela idade.')
        elif self.trabalho >= 30:
            print('Pode se aposentar pelo tempo de serviço.')
        elif self.idade >= 60 and self.trabalho >= 25:
            print('Pode se aposentar pelo somatorio da idade com o tempo de serviço.')
        else:
            print('Você ainda não pode se aposentar.')


idade = int(input('Qual sua idade: '))
servico = int(input('Qual seu tempo de serviço (em anos): '))
aposentar = Aposentar(idade, servico)
aposentar.verificar()
