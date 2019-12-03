"""
Exercicio 34 - Leia a nota e o numero de faltas de um aluno, e escreva seu conceito, quando o aluno tem mais
de 20 faltas ocorre uma redução de conceito.
"""


nota = float(input('Nota: '))
falta = int(input('Falta: '))

if 9.0 <= nota <= 10:
    if falta <= 20:
        print('Conceito A.')
    else:
        print('Conceito B.')
elif 7.5 <= nota <= 8.9:
    if falta <= 20:
        print('Conceito B.')
    else:
        print('Conceito C.')
elif 5 <= nota <= 7.4:
    if falta <= 20:
        print('Conceito C.')
    else:
        print('Conceito D.')
elif 4.0 <= nota <= 4.9:
    if falta <= 20:
        print('Conceito D.')
    else:
        print('Conceito E.')
elif 0.0 <= nota <= 3.9:
    if falta <= 20:
        print('Conceito E.')
    else:
        print('Conceito E.')
else:
    print('Nota informada é inválida.')
