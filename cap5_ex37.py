"""
Exercicio 37 -
"""
import datetime
while True:
    entrada = input("Digite a hora de entrada HH:MM: ")
    saida = input("Digite a hora de saída HH:MM: ")
    try:
        hora_entrada = datetime.datetime.strptime(entrada, "%H:%M")
        hora_saida = datetime.datetime.strptime(saida, "%H:%M")
        break
    except ValueError:
        print('Você digitou as horas errado, tente de novo')

if hora_saida < hora_entrada:
    aux = str(hora_saida - hora_entrada)
    print(f'Tempo total {aux.split(" ")[2]}')
    if int(aux.split(" ")[2].split(":")[1]) != 0:
        tempo = int(aux.split(" ")[2].split(":")[0]) + 1
    else:
        tempo = int(aux.split(" ")[2].split(":")[0])
else:
    aux = str(hora_saida - hora_entrada)
    print(f'Tempo Total {aux}')
    if int(aux.split(":")[1]) != 0:
        tempo = int(aux.split(":")[0]) + 1
    else:
        tempo = int(aux.split(":")[0])

print(f'Tempo total a pagar {tempo} horas')

if tempo <= 2:
    print(tempo*1)
elif tempo >= 3 and tempo <= 4:
    print(2+tempo*1.4)
else:
    print(((tempo-4)*2) + 4.8)
