"""
Exercicio 2
"""


sal = float(input("salario: "))
pres = float(input("prestação: "))

if pres > sal*0.2:
    print(f"emprestimo não concedido pres={pres} sal={sal*0.2}")
else:
    print(f"emprestimo concedido pres={pres} sal={sal*0.2}")
