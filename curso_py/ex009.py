velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80.0:
    print(f'Você foi multado no valor de {(velocidade - 80)*7}')
else:
    print(f'Pode seguir')