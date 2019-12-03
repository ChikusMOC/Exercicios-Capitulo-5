"""
Exercicio 35 - Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está
entres 1 e 12, e se o dia existe naquele mês.Note que fevereiro tem 29 dias em ano bissexto e
28 em ano não bissexto.
"""


data = input('Informe uma data dd/mm/aaaa: ')
data = data.split('/')
for i in range(3):
    data[i] = int(data[i])

if data[1] >= 1 and data[1] <= 12:
    if data[1] == 2:
        if data[2] % 400 == 0 or data[2] % 4 == 0 and data[2] % 100 != 0:
            if data[0] >= 0 and data[0] <= 29:
                print('Data existente.')
            else:
                print('Data não existe.')
        elif data[0] >= 0 and data[0] <= 28:
            print('Data existente.')
        else:
            print('Data não existe.')
    elif data[1] == 4 or data[1] == 6 or data[1] == 9 or data[1] == 11:
        if data[0] >= 0 and data[0] <= 30:
            print('Data existente.')
        else:
            print('Data não existe')
    else:
        if data[0] >= 0 and data[0] <= 31:
            print('Data existente.')
        else:
            print('Data não existe.')
else:
    print('data não existe')

print(data)
