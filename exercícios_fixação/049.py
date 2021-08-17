''' Crie um programa que leia 6 números inteiros e no final mostre quantos deles
são pares e quantos são ímpares.'''
par = 0
impar = 0
for num in range(1,7):
    numero = int(input(f'{num}° numero: '))
    if numero % 2 == 0:
        par +=1
    else:
        impar += 1
print(f'A quantidade números pares digitados é {par}, já de números ímpares são {impar}')
