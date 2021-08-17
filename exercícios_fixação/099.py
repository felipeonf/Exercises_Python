'''Faça um programa que possua uma função chamada Potencia(), que vai receber
dois parâmetros numéricos (base e expoente) e vai calcular o resultado da
exponenciação.
Ex: Potencia(5,2) vai calcular 52 = 25 '''
def Potencia(base,potencia):
    return base**potencia
base = int(input('Digite a base: '))
potencia = int(input('Digite a potência: '))
print(Potencia(base,potencia))