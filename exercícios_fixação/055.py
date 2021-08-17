'''[DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de
agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4
tentativas para tentar acertar.'''
from random import randint
numerosorteado = randint(1,10)
for tentativa in range(1,5):
    print('*'*30)
    print('Você possui 4 tentativas no total')
    print(f'e essa é a sua {tentativa}° tentativa!')
    print('*'*30)
    numero = int(input('Digite o valor que quer adivinhar: '))
    if numero == numerosorteado:
        print('PARABENS! VOCÊ ACERTOU O NÚMERO SORTEADO!')
        break
    else:
        if tentativa == 4:
            ignorar = True
        else:
            print('TENTE MAIS UMA VEZ!')
if tentativa == 4:
    print('Você não conseguiu acertar o número sorteado, quem sabe da próxima vez!')
