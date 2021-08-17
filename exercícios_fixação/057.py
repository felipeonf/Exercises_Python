'''
 Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
No final, mostre o total de salários pagos aos homens e o total pago às
mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não
sempre que ler os dados de um funcionário.'''
print(f'>>>>>>>>>>>>>Extrato Salarial>>>>>>>>>>>>>')
salarios_homens = 0
salarios_mulheres = 0
while True:
    print('.............Dados.............')
    sexo = input('Digite seu sexo(m/f): ')
    if sexo == 'm':
        salario = int(input('Digite o seu salário: '))
        salarios_homens += salario
    elif sexo == 'f':
        salario = int(input('Digite o seu salário: '))
        salarios_mulheres += salario
    else:
        print('Sexo inválido para o cadastro.Tente novamente!')
    opcao = input('Deseja continuar(s/n)?: ')
    if opcao in 'nNAOnaoNnãoNão':
        break
print(f'O total de salários pagos aos homens é R${salarios_homens}, já o de mulheres é R${salarios_mulheres}')
