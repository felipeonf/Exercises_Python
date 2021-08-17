'''Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor.
No final, mostre quais são os números pares que foram digitados e em que
posições eles estão armazenados.'''
numeros = []
for num in range(0,10):
    numeros.append(int(input('Valor: ')))
print('Os número pares digitados e suas respectivas posições são: ')
for num in numeros:
    if num % 2 == 0:
        print(f'{num} - na {numeros.index(num)+1}° posição ',end=' ')
