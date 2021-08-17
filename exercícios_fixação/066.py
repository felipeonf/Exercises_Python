'''Escreva um programa que leia um número qualquer e mostre a tabuada desse
número, usando a estrutura “para”.
Ex: Digite um valor: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15 ...'''
while True:
    numero = int(input('Digite um valor: '))
    for num in range(1,11):
        print(f'{numero} X {num} = {numero*num}')
    opcao = input('Deseja continuar(s/n)? ').strip().lower()[0]
    if opcao == 'n':
        break
