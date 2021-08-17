from random import randint
numerosorteado = randint(0,10)
acertou = False
tentativas = 0
print('Vamos tentar acertar o número sorteado pelo computador')
while not acertou:
    palpite = int(input('Palpite: '))
    tentativas += 1
    if palpite == numerosorteado:
        acertou = True
    else:
        print('Tente novamente!')
        if palpite > numerosorteado:
            print('Dica: é um número menor')
        else:
            print('Dica: é um número maior')
print(f'Parabéns, você acertou o número sorteado com {tentativas} tentativas.')