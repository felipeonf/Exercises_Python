'''Faça um algoritmo que pergunte ao usuário um número inteiro e positivo 
# qualquer e mostre uma contagem até esse valor:
Ex: Digite um valor: 35
Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!'''
number = int(input('Digite um inteiro positivo: '))
if number > 0:
    for num in range(1,number+1):
        if num == 1:
            print('Contagem:',end=' ')
        print(num,end=' ')
    print('Acabou!')
else:
    print('Esse número não é positivo, tente novamente!')
