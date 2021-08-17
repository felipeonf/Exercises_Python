'''
[DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
'''
jogador1 = input('Qual sua opção?(pedra/papel/tesoura) ')
jogador2 = input('Qual sua opção?(pedra/papel/tesoura) ')

if jogador1 == 'pedra' and jogador2 == 'pedra'\
    or jogador1 =='papel' and jogador2 == 'papel'\
        or jogador1 =='tesoura' and jogador2 == 'tesoura':
        print('EMPATE')

elif jogador1 == 'papel' and jogador2 == 'pedra'\
    or jogador1 == 'pedra' and jogador2 == 'tesoura'\
         or jogador1 == 'tesoura' and jogador2 == 'papel':
         print('JOGADOR 1 VENCEU')

elif jogador2 == 'papel' and jogador1 =='pedra'\
    or jogador2 == 'pedra' and jogador1 == 'tesoura'\
        or jogador2 == 'tesoura' and jogador1 =='papel':
        print('JOGADOR 2 VENCEU')
