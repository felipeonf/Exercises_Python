''' Escreva um programa que leia 15 números e guarde-os em um vetor. No final,
mostre o vetor inteiro na tela e em seguida mostre em que posições foram
digitados valores que são múltiplos de 10.'''
numeros = []
for numero in range(0,16):
    numeros.append(int(input('Digite um número inteiro: ')))
print(numeros)
print('Os valores digitados que são múltiplos de 10 estão nas posições:')
for elemento in numeros:
    if elemento % 10 == 0:
        print(numeros.index(elemento),end=' ')
