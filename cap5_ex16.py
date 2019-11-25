"""
Exercicio 16
"""


def ano(i):
    opcao = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    return opcao.get(i, 'Mês invalido')


mes = int(input('Digite o numero do mês: '))

print(ano(mes))
