''' Crie um programa que leia o nome e a idade de 9 pessoas e guarde esses
valores em dois vetores, em posições relacionadas. No final, mostre uma listagem
contendo apenas os dados das pessoas menores de idade.'''
nomes = []
idades = []
for pessoa in range(9):
    nomes.append(input('Nome: '))
    idades.append(int(input('Idade: ')))
print('As pessoas menores de idade são:')
for posicao in range(9):
    if idades[posicao] < 18:
         print(f'{nomes[posicao]}',end=' ')
