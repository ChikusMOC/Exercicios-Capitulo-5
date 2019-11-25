"""
Exercicio 20
"""


class triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def verifica(self):
        if self.lado1 < self.lado2 + self.lado3 and self.lado2 < self.lado1 + self.lado3:
            if self.lado1 + self.lado2 > self.lado3:
                print("São valores de um Triangulo.")
                if self.lado1 == self.lado2 == self.lado3:
                    print("Se trata de um triangulo equilatero.")
                elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                    print("Se trata de um triangulo isosceles.")
                else:
                    print("Se trata de um triangulo escaleno")
            else:
                print("Valores informados não correspondem a um triangulo")
        else:
            print("Valores informados não correspondem a um triangulo")


num1 = int(input("Valor do primeiro lado: "))
num2 = int(input("Valor do segundo lado: "))
num3 = int (input("valor do terceiro lado: "))
tri = triangulo(num1, num2, num3)
tri.verifica()
