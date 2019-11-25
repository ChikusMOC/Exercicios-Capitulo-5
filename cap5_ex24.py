"""
Exercicio 24
"""


i = True
valor = float(input('Valor do produto: '))
while i:
    estado = input("Qual estado deseja enviar essa mercadoria?\n"
                   "'MG'- Minas Gerais\n"
                   "'SP'- São Paulo\n"
                   "'RJ'- Rio de Janeiro\n"
                   "'MS'- Mato Grosso do Sul. \n->")
    estado = estado.upper()
    if estado == 'MG' or estado == 'SP' or estado == 'RJ' or estado == 'MS':
        i = False
    else:
        print("Estado informado não é valido.")

preco = {
    'MG': (f"Valor final para MG = {valor+valor*0.07}"),
    'SP': (f"Valor final pra SP = {valor+valor*0.12}"),
    'RJ': (f"Valor final pra RJ = {valor+valor*0.15}"),
    'MS': (f"Valor final pra MS = {valor+valor*0.08}")
}
print(preco.get(estado))
