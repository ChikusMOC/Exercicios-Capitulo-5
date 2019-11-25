"""
Exercicio 8
"""
import sys


valor = []
n = 0

for i in range(5):
    elemento = float(input("digite uma nota: "))
    valor.append(elemento)
    if 0.0 <= valor[i] <= 10.0:
        print("nota valida")
    else:
        print("nota invalida")
        sys.exit()
