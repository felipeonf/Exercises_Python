''' Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando
no final:
a) Qual foi a média de altura do grupo
b) Quantas pessoas pesam mais de 90Kg
c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.
'''
alturas = 0
maisnoventa = 0
menosCinquentaSessenta = 0
maisNoventaCem = 0
for pessoa in range(1,8):
    print('>>>>>>>>>> {}° PESSOA >>>>>>>>>>'.format(pessoa))
    peso = float(input('Peso: Kg '))
    altura = float(input('Altura (cm): '))
    if peso > 90:
        maisnoventa += 1
    if peso < 50 and altura < 160:
        menosCinquentaSessenta += 1
    if altura > 190 and peso > 100:
        maisNoventaCem += 1
    alturas += altura
media = alturas / 7
print()
print(f'A média de altura das pessoas é {media}')
print(f'{maisnoventa} pessoas pesam mais que 90kg')
print(f'{menosCinquentaSessenta} pessoas possuem menos de 50kg e medem menos de 150cm')    
print(f'{maisNoventaCem} pessoas medem mais de 190cm e pesam mais de 100kg')
