'''Refaça o exercício 91, só que agora em forma de função Maior(), mas faça uma
adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o
maior entre eles.'''
def Maior(a,b,c):
    if a>b>c or a>c>b:
        return 'O primeiro valor é o maior'
    elif b>c>a or b>a>b:
        return 'O segundo valor é o maior'
    elif c>b>a or c>a>b:
        return 'O terceiro valor é o maior'
a = int(input('Valor 1: '))
b = int(input('Valor 2: '))
c = int(input('Valor 3: '))
print(Maior(a,b,c))
