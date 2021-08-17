'''Crie um programa que preencha automaticamente um vetor numérico com 7
números gerados aleatoriamente pelo computador e depois mostre os valores
gerados na tela.'''
from random import randint
numeros = []
for numero in range(1,8):
    numeros.append(randint(0,100))
print(numeros)
