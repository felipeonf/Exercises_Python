'''[DESAFIO] Crie uma lógica que preencha um vetor de 20 posições com números
aleatórios (entre 0 e 99) gerados pelo computador. Logo em seguida, mostre os
números gerados e depois coloque o vetor em ordem crescente, mostrando no final
os valores ordenados.'''
from random import randint
numeros = []
for numero in range(1,21):
    numeros.append(randint(0,99))
print(numeros)
print('Ordem crescente:',end=' ')
print(sorted(numeros))
print('Ordem decrescente:',end=' ')
print(sorted(numeros,reverse=True))