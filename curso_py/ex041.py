from random import randint
from time import sleep
opcoes = ('Pedra','Papel','Tesoura')
comp = randint(0,2)
print('>'*22)
print('''Escolha a sua jogada:
(0) Pedra
(1) Papel
(2) Tesoura''')
print('>'*22)
jog = int(input('Qual é sua jogada? '))
if jog > 3:
    print('JOGADA INVALIDA!')
    exit()
else:
    jogada = opcoes[jog]
    print('PROCESSANDO...')
    sleep(2)
    computador = opcoes[comp]
    print('>'*25)
    print(f'O jogador jogou {jogada}')
    print(f'O computador jogou {computador}')
    print('>'*25)
    if comp == 0:
        if jog == 0:
            print('HOUVE UM EMPATE!')
        elif jog == 1:
            print('JOGADOR VENCEU!')
        elif jog == 2:
            print('COMPUTADOR VENCEU!')
        else:
            print('JOGADA INVÁLIDA1')  
    elif comp == 1:
        if jog == 0:
            print('COMPUTADOR VENCEU!')
        elif jog == 1:
            print('HOUVE UM EMPATE!')
        elif jog == 2:
            print('JOGADOR VENCEU!')
        else:
            print('JOGADA INVÁLIDA!')
    elif comp == 2:
        if jog == 0:
            print('JOGADOR VENCEU!')
        elif jog == 1:
            print('COMPUTADOR VENCEU!')
        elif jog == 2:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA!')
