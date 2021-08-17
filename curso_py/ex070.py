from random import randint


def sorteia():
    lista = []
    cont = 0
    while cont <= 5:
        lista.append(randint(1,10))
        cont += 1
    return lista
def somaPar (vetor):
    pares = []
    for num in vetor:
        if num  % 2 == 0:
            pares.append(num)
    return sum(pares)


numeros = sorteia()
print(f'Os números sorteados foram {numeros}')
print(f'A soma dos números pares sorteados foi {somaPar(numeros)}')
