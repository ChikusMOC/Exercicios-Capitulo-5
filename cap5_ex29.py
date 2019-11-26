"""
Exercicio 29 - Faça uma prova de matemática para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aleatórios entra 1 e 100, e mostra na tela a pergunta:
qual é a soma de a + b, onde a e b são numeros aleatórios. Peça a resposta. Faça cinco perguntas ao aluno,
e mostre pra ele as perguntas e as respostas corretas, alem de quantas vezes o aluno acertou.
"""


from random import *
i = 0
aux = 0
aux1 = 0
list = []
list2 = []
list3 = []
print('Qual o resultado das somas:')
while i < 5:
    val1 = randint(1, 100)
    val2 = randint(1, 100)
    list.append([val1, val2])
    i = i + 1

for a, b in list:
    try:
        list2.append(a+b)
        print(f'Qual é a soma de {a}+{b}? ')
        var = int(input())
        list3.append(var)
    except ValueError:
        print('Você digitou algo errado, vamos pra proxima questão.')

for a in list2:
    for b in list3:
        if a == b:
            var1, var2 = list[aux1]
            aux = aux + 1
            print(f'Parabens, voçê acertou a questão {var1}+{var2}={b}')
    aux1 = aux1 + 1

print(f'De {aux1} respostas você acertou {aux}')
