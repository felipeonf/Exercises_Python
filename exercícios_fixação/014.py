# A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
#um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
#sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

def calculaPreco(km,d):
    return (km * 0.20) + (d * 90)
kmPercorridos = float(input('Quantos km o carro percorreu? '))
diasUtilizados = int(input('Quantos dias você esteve com o carro? '))

print(f'O valor total do aluguel do carro com {kmPercorridos}km percorridos e {diasUtilizados} dias utilizados será de R${calculaPreco(kmPercorridos,diasUtilizados)}')
