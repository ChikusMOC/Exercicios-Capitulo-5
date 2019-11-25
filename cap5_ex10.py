"""
Exercicio 10
"""


sexo = input("Digite seu sexo M/F: ")
sexo = sexo.upper()
altura = float(input("Digite sua altura: "))

if sexo == 'M':
    print(f"peso ideal = {72.7*altura-58}")
elif sexo == 'F':
    print(f"Peso ideal = {62.1*altura-44.7}")
else:
    print("sexo informado não esta definido.")
