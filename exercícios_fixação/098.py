'''Crie um programa que tenha uma função SuperSomador(), que vai receber dois
números como parâmetro e depois vai retornar a soma de todos os valores no
intervalo entre os valores recebidos.
Ex:
SuperSomador(1, 6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
SuperSomador(15, 19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85'''
def SuperSomador(a,b):
    soma = 0
    for numero in range(a,b+1):
        soma += numero
    return soma
a = int(input('Começo: '))
b = int(input('Fim: '))
print(SuperSomador(a,b))