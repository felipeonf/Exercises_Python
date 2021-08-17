'''Crie um programa usando a estrutura “faça enquanto” que leia vários números.
A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na
tela:
a) O somatório entre todos os valores
b) Qual foi o menor valor digitado
c) A média entre todos os valores
d) Quantos valores são pares'''
print('>>>>>>>>>> Contagem de números >>>>>>>>>>')
valores = 0
menorvalor = 0
n_valores = 0
pares = 0
while True:
    valor = int(input(f'Digite o {n_valores+1}° valor: '))
    valores += valor
    n_valores += 1
    if n_valores == 1:
        menorvalor = valor
    elif n_valores > 1:
        if valor < menorvalor:
            menorvalor = valor
    if valor % 2 == 0:
        pares +=  1
    opcao = input('Deseja continuar(s/n)? ').strip().lower()[0]
    if opcao == 'n':
        break
print(f'O somatório entre todos os valores é {valores}')
print(f'O menor valor digitado foi {menorvalor}')
print('A média entre todos os valores é {:.2f}'.format(valores/n_valores))
print(f'Existem {pares} valores pares')
