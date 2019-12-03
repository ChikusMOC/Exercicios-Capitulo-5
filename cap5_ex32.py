"""
Exercicio 32 - Escreva um programa que leia o código do produto escolhido do cardápio de uma lanchonete
e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que cada execução somente
será calculado um pedido. O cardapio da lanchonete segue o padrão abaixo:

Produto -------- Codigo ------ Preço
Cachorro quente - 100 -------- 1.20
Bauru Simples --- 101 -------- 1.30
Bauru com Ovo --- 102 -------- 1.50
Hamburguer ------ 103 -------- 1.20
Cheeseburguer --- 104 -------- 1.70
Suco ------------ 105 -------- 2.20
Refrigerante ---- 106 -------- 1.00
"""

cardapio = {
    100: 1.20,
    101: 1.30,
    102: 1.50,
    103: 1.20,
    104: 1.70,
    105: 2.20,
    106: 1.00
}


def comanda():
    valor_final = 0
    while True:
        try:
            codigo = int(input('Codigo do produto: '))
            quantidade = int(input('Quantidade: '))
            if 100 <= codigo <= 106:
                valor_final = valor_final + (quantidade * cardapio.get(codigo))
                aux = input('Mais produtos s/n? ')
                if aux == 'n':
                    return valor_final
            else:
                print('Codigo informado não corresponde a um produto do cardapio.')
        except ValueError:
            print('Alguma coisa foi informada errada.')


total = comanda()
print(f'{total:.2f}')
