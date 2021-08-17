'''Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses
valores para um procedimento Maior() que vai verificar qual deles é o maior e
mostrá-lo na tela. Caso os dois valores sejam iguais, mostrar uma mensagem
informando essa característica.'''
def Maior(a,b):
    if a > b:
        return 'O valor 1 é maior que o valor 2'
    elif a < b:
        return 'O valor 2 é maior que o valor 1'
    else:
        return 'Os valores são iguais!'
a = int(input('Valor 1: '))
b = int(input('Valor 2: '))
print(Maior(a,b))
    