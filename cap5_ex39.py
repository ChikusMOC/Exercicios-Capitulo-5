"""
Exercicio 39 -
"""


salario = float(input("Digite o salario do funcionario: "))
tempo = int(input("Digite o tempo de serviço desse funcionario em ano(s), 0 caso ainda sejam meses: "))

if salario <= 500:
    salario = salario * 1.25
elif salario > 500 and salario <= 1000:
    salario = salario * 1.20
elif salario > 1000 and salario <= 1500:
    salario = salario * 1.15
elif salario > 1500 and salario <= 2000:
    salario = salario * 1.10
else:
    print('Funcionario não tem direito a reajuste salarial.')
if tempo < 1:
    print('Funcionario não tem direito a bonus por tempo')
elif tempo >= 1 and tempo <= 3:
    salario = salario + 100
elif tempo >= 4 and tempo <= 6:
    salario = salario + 200
elif tempo >= 7 and tempo <= 10:
    salario = salario + 300
else:
    salario = salario + 500
print(f'Salario final = {salario:.2f}')
