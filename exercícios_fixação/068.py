'''Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura
“para”. No final, mostre na tela:
a) Quantas mulheres foram cadastradas
b) Quantos homens pesam mais de 100Kg
c) A média de peso entre as mulheres
d) O maior peso entre os homens'''
mulheres = 0
homens_100 = 0
peso_mulheres = 0
maior_peso_homem = 0
for pessoa in range(0,9):
    sexo = input('Digite o seu sexo (m/f) : ').strip().lower()[0]
    if sexo == 'm':
        peso = int(input('Digite o seu peso: '))
        if peso > maior_peso_homem:
            maior_peso_homem = peso
        if peso > 100:
            homens_100 += 1
    elif sexo == 'f':
        mulheres += 1
        peso = int(input('Digite o seu peso: '))
        peso_mulheres += peso
print(f'Foram cadastradas {mulheres} mulheres')
print(f'{homens_100} homens pesam mais que 100 kg')
print('A média de peso entre as mulheres foi de {:.2f} Kg'.format(peso_mulheres/mulheres))
print(f'O maior peso entre os homens foi de {maior_peso_homem} Kg')
