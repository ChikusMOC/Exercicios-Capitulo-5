"""
Exercicio 14
"""
import sys

nota_final = 0
i = 0
while i < 3:
    nota = float(input("informe a nota: "))
    if 0 <= nota <= 10:
        i = i + 1
        if i == 1:
            nota_final = nota_final + nota * 2
        elif i == 2:
            nota_final = nota_final + nota * 3
        else:
            nota_final = nota_final + nota * 5
    else:
        print("Nota informada não é valida.")
nota_final = nota_final / 10

if 0 <= nota_final <= 2.9:
    print(f"aluno em reprovado com nota {nota_final}")
elif 3 <= nota_final <= 4.9:
    print(f"aluno em recuperação com nota {nota_final}")
else:
    print(f"Aluno aprovado com nota {nota_final}")
