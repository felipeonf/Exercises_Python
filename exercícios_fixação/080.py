''' Faça um algoritmo que preencha um vetor de 30 posições com números entre 1 e
15 sorteados pelo computador. Depois disso, peça para o usuário digitar um
número (chave) e seu programa deve mostrar em que posições essa chave foi
encontrada. Mostre também quantas vezes a chave foi sorteada.'''
from random import randint
numeros =[]
for num in range(1,31):
    numeros.append(randint(1,15))
chave = int(input('Digite um número entre 1 e 15: '))
print(numeros)
print(f'O numero {chave} foi encontrado {numeros.count(chave)} vezes')
if numeros.count(chave) == 0:
    exit()
else:
    print('Nas posições: ')
    for posicao in range(len(numeros)):
        if numeros[posicao] == chave:
            print(posicao,end=' ')