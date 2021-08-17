'''Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses
valores para um procedimento Somador() que vai calcular e mostrar a soma entre
eles.'''
def Somador(a,b):
    return a+b
a = int(input('Valor 1: '))
b = int(input('Valor 2: '))
print(f'A soma entre esses números é {Somador(a,b)}')
