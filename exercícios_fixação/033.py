'''
Escreva um programa para aprovar ou não o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Em quantos anos quer pagar a casa? '))

prestacao = valorCasa / (anos * 12)

if prestacao > 0.3 * salario:
    print('Empréstimo negado.')
else:
    print('Empréstimo aceito.')
