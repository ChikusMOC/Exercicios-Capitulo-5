"""
Exercicio 18
"""


class calculadora:

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def soma(self):
        print(self.val1 + self.val2)

    def sub(self):
        print(self.val1 - self.val2)

    def mult(self):
        print(self.val1 * self.val2)

    def divi(self):
        print(self.val1 / self.val2)


numero1 = int(input('Primeiro numero: '))
numero2 = int(input('Segundo numero: '))
soma = calculadora(numero1, numero2)
op = input("Escolha uma das operações matematicas.\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\nSua opção: ")

if op == '1':
    soma.soma()
elif op == '2':
    soma.sub()
elif op == '3':
    soma.mult()
elif op == '4':
    soma.divi()
else:
    print("Opção escolhida não foi validada. Reinicie o programa.")
