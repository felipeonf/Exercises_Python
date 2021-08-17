''' Faça um programa usando a estrutura “faça enquanto” que leia a idade de
várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou
não continuar a digitar dados. No final, quando o usuário decidir parar, mostre
na tela:
a) Quantas idades foram digitadas
b) Qual é a média entre as idades digitadas
c) Quantas pessoas tem 21 anos ou mais.'''
print('>>>>>>>>>> Leitura de dados >>>>>>>>>>')
idades = 0
n_idades = 0
pessoas_21mais = 0
while True:
    idade = int(input('Digite a sua idade: '))
    n_idades += 1
    idades += idade
    if idade >= 21:
        pessoas_21mais += 1
    opcao = input('Deseja continuar?(s/n) ').strip().lower()[0]
    if opcao == 'n':
        break
print(f'Foram digitadas {n_idades} idades')
print('A média entre as idades é {:.2f}'.format(idades/n_idades))
print(f'{pessoas_21mais} pessoas possuem 21 ou mais anos')
