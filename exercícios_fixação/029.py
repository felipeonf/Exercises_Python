'''
 Desenvolva um programa que leia o nome de um funcionário, seu salário,
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
acordo com a tabela a seguir:
 - Até 3 anos de empresa: aumento de 3%
 - entre 3 e 10 anos: aumento de 12.5%
 - 10 anos ou mais: aumento de 20%
'''
nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
anosTrabalho = int(input('Há quantos anos você trabalha na empresa? '))

if anosTrabalho <= 3 :
    print(f'O seu salário reajustado será de R${salario * 1.03}')
elif 3 < anosTrabalho < 10 :
    print(f'O seu salário reajustado será de R${salario * 1.125}')
elif anosTrabalho >= 10:
    print(f'O seu salário reajustado será de R${salario * 1.2}')
