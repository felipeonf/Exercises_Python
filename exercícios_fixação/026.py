""" Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
na tela uma das mensagens abaixo:
 - O primeiro valor é o maior
 - O segundo valor é o maior
 - Não existe valor maior, os dois são iguais
 """
number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))

if number1 > number2 :
    print('O primeiro valor é o maior.')

elif number2 > number1:
    print('O segundo valor é o maior.')

else:
    print('Não existe valor maior, os dois são iguais.')
