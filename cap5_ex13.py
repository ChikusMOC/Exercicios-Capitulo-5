"""
Exercicio 13
"""


nota_final = 0
for i in range(3):
    nota = float(input("digite nota: "))
    if i == 2:
        nota_final = nota_final + nota * 2
    else:
        nota_final = nota_final + nota
if nota_final >= 60:
    print(f"Aluno aprovado com nota igual a {nota_final}")
else:
    print(f"Aluno reprovado com nota igual a {nota_final}.")
