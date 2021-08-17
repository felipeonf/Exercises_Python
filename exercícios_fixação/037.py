'''
 Uma empresa precisa reajustar o salário dos seus funcionários, dando um
aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
No final, mostre o seu novo salário, baseado na tabela a seguir:
- Mulheres
 - menos de 15 anos de empresa: +5%
 - de 15 até 20 anos de empresa: +12%
 - mais de 20 anos de empresa: +23%
- Homens
 - menos de 20 anos de empresa: +3%
 - de 20 até 30 anos de empresa: +13%
 - mais de 30 anos de empresa: +25%
 '''
salario = float(input('Digite o seu salário atual: '))
genero = input('Qual seu gênero?(m/f) ')
anos = int(input('Há quantos anos você trabalha na empresa? '))


if genero == 'f':
    if anos < 15:
        print('O seu novo salário será de R${:.1f}'.format(salario*1.05))
    elif 15 <= anos <= 20:
        print('O seu novo salário será de R${:.1f}'.format(salario*1.12))
    elif anos > 20:
        print('O seu novo salário será de R${:.1f}'.format(salario*1.25))

elif genero == 'm':
    if anos < 20:
        print('O seu novo salário será de R${:.1f}'.format(salario*1.03))
    elif 20 <= anos <= 30:
        print('O seu novo salário será de R${:.1f}'.format(salario*1.13))
    elif anos > 30:
        print('O seu novo salário será de R${:.1f}'.format(salario*1.25))




