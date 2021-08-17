'''Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No
final, mostre:
a) Qual é a média de idade das pessoas cadastradas
b) Em quais posições temos pessoas com mais de 25 anos
c) Qual foi a maior idade digitada (podem haver repetições)
d) Em que posições digitamos a maior idade'''
idades = []
cont = 0
for pessoa in range(1,9):
    idades.append(int(input('Digite a sua idade: ')))
print('>>>>>>>>>> Informações <<<<<<<<<<')
print('A média das pessoas cadastradas é {:.2f}'.format(sum(idades)/len(idades)))
print('As posições das pessoas com mais de 25 anos são: ')
for posicao in range(len(idades)):
    if idades[posicao] > 25:
        print(f'{posicao+1}°',end=' ')
    else:
        cont +=1
if cont == 8:
    print(f'Não há pessoas com mais de 25 anos.')
print(f'\nA maior idade digitada foi {max(idades)}')
print(f'A maior idade apareceu nas posições:')
for posicao in range(len(idades)):
    if idades[posicao] == max(idades):
        print(f'{posicao+1}°',end=' ')
