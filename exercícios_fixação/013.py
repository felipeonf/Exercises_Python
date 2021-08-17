# Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salário: '))
aumento = float(input('Digite o seu aumento em porcentagem: '))

print(f'O seu salário com o aumento ficará R$ {salario*((aumento/100)+1)}')

