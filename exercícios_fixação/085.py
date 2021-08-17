''' Faça um algoritmo que leia o nome, o sexo e o salário de 5 funcionários e
guarde esses dados em três vetores. No final, mostre uma listagem contendo
apenas os dados das funcionárias mulheres que ganham mais de R$5 mil.'''
nomes = []
sexo = []
salario = []
for funcionario in range(5):
    nomes.append(input('Nome: '))
    sexo.append(input('Sexo(m/f): ').strip().lower()[0])
    salario.append(float(input('Salário: R$ ')))
print('As funcionárias que ganham mais de R$5mil são: ')
for posicao in range(5):
    if sexo[posicao] == 'f' and salario[posicao] > 5000.0:
        print(nomes[posicao],end='  ')
