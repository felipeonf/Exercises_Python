''' Faça um programa que leia 7 números inteiros e no final mostre o somatório
entre eles.'''
soma = 0
for num in range(1,8):
    numero = int(input(f'{num}° numero: '))
    soma += numero
print(f'A soma desses numeros é {soma}')
