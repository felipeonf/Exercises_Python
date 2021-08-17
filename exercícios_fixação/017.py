#Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
#80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
#o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

velocidade = int(input('Qual a velocidade registrada do carro em km/h? '))
if velocidade > 80:
    print(f'Você será multado no valor de R${(velocidade-80)*5}')

