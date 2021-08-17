from datetime import datetime
cadastro = {}
cadastro['Nome'] = input('Digite seu nome: ')
ano_nascimento = int(input('Digite seu ano de nascimento: '))
cadastro['Idade'] = datetime.now().year - ano_nascimento
ctps = int(input('Digite sua carteira de trabalho: '))
if ctps != 0:
    cadastro['CTPS'] = ctps
    cadastro['Contratação'] = int(input('Digite o seu ano de contratação: '))
    cadastro['Salário'] = float(input('Digite o seu salário: R$ '))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] - ano_nascimento)+35
else:
    cadastro['CTPS'] = 0
for chave,valor in cadastro.items():
    print(f'{chave} tem o valor {valor}')
