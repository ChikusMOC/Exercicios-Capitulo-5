"""
Exercicio 17
"""


basemaior = 0
basemenor = 0
altura = 0
i = 0

while i == 0:
    if basemaior <= 0:
        basemaior = int(input('Base maior: '))
    elif basemenor <= 0:
        basemenor = int(input('Base menor: '))
    elif altura <= 0:
        altura = int(input('Altura: '))
    else:
        i = i + 1


area = ((basemaior+basemenor)*altura)/2
print(area)
