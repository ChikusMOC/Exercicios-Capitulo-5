"""
Exercicio 41 -
"""


def imc(a, b, c):
    print(f"Calculando o imc de {a}, que possui altura {b} e peso em kilos {c}")
    return c / (b * b)


def calc_altura():
    while True:
        try:
            al = input(f"Informe sua altura em metros: ")
            al = al.replace(',', '.')
            al = float(al)
            if al >= 2.5:
                al = al / 100
            return al
        except ValueError:
            print("Você não digitou sua altura corretamente.")


#  return al


def calc_peso():
    while True:
        try:
            pe = input("Digite agora seu peso em kilos: ")
            pe = pe.replace(',', '.')
            pe = float(pe)
            #  break
            return pe
        except ValueError:
            print("Voce não digitou seu peso corretamente, tente de novo:")


#  return pe


def categoria(a):
    if a < 18.5:
        print("Você esta abaixo do peso")
    elif a >= 18.5 and a <= 24.9:
        print("Saudavel")
    elif a >= 25 and a <= 29.9:
        print("Peso em excesso")
    elif a >= 30 and a <= 34.9:
        print("Grau obesidade 1")
    elif a >= 35 and a <= 39.9:
        print("Grau obesidade 2(severa)")
    elif a >= 40:
        print("Grau obesidade 3(mórbida)")


def tratamento(a):
    a = a.lower()
    if a == 'sim':
        a = 's'
    elif a == 'nao' or a == 'não':
        a = 'n'
    while a != 's' and a != 'n':
        print("Digite corretamente se deseja(S) ou não(N) que o programa inicie: ")
        a = input()
        a = a.lower()
        if a == 'sim':
            a = 's'
        elif a == 'nao' or a == 'não':
            a = 'n'
    return a


print("Deseja calcular seu IMC? S/N")
valor = input()
valor = tratamento(valor)
while valor == 's':
    print("Digite seu nome: ", end="")
    nome = input()
    altura = calc_altura()
    peso = calc_peso()
    seuimc = imc(nome, altura, peso)
    seuimc = round(seuimc, 2)
    print(f"Então {nome}, seu imc é {seuimc}. ", end="")
    categoria(seuimc)
    print("Deseja usar o programa novamente? S/N")
    valor = input()
    valor = tratamento(valor)
