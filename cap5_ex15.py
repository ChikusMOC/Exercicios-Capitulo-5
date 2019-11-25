"""
Exxercicio 15
"""


print("Digite um numero de 1 a 7")
dia = int(input("dia da semana: "))


def semana(i):
    opcoes = {
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado',
        1: 'Domingo'
    }
    return opcoes.get(i, "Dia invalido.")


print(semana(dia))
