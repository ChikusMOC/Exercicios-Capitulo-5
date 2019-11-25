"""
Exercicio 21
"""

menu = {
    1: 'Escolha a opção:',
    2: '1- Soma de 2 números',
    3: '2- Diferença entre 2 numeros (maior pelo menor)',
    4: '3- Produto entre 2 numeros.',
    5: '4- Divisão entre 2 numeros (0 denominador não pode ser zero)'
}
i = 1
for i in menu:
    print(menu.get(i))
    i += 1
i = True
while i:
    op = int(input("Opcão: "))
    if 1 <= op <= 4:
        i = False
    else:
        print('Opção invalida.')

num = int(input("Numero: "))
num1 = int(input('Numero: '))
if op == 2:
    if num < num1:
        num, num1 = num1, num
        print('Numeros foram trocados devido a opção selecionada')
elif op == 4:
    if num1 == 0:
        aux = input("Denominador igual a 0, deseja trocar os numeros s/n? ")
        if aux == 's':
            num, num1 = num1, num


opcao = {
    1: f'Soma = {num + num1}',
    2: f'Subtração = {num - num1}',
    3: f'Multiplicação = {num * num1}',
    4: f'Divisão = {num / num1}'
}


print(opcao.get(op))

