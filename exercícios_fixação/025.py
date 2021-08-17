# Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.

stop = 'y'

while stop == 'y':

    number = int(input('Write a number: '))

    if number % 2 == 0:
        print('This number is pair.')
    else:
        print('This number is odd.')

    stop = input('Do you want to continue?(y/n)')
    if stop == 'n':
        print('Bye!')
