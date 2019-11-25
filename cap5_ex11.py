"""
Exercicio 11
"""


soma = 0
num = int(input("digite um numero: "))
while num > 0:
    strnum = num.__str__()
    n = strnum.__len__()
    for i in range(n):
        auxiliar = tuple(strnum)[i]
        auxiliar = int(auxiliar)
        soma = soma + auxiliar
    print(soma)
    soma = 0
    num = int(input("digite um numero: "))
print("Numero invalido")
