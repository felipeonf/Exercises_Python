'''
 [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado.
'''
from random import choice
lista = [1,2,3,4,5]
numeroEscolhido = choice(lista)

escolha = int(input('Escolha um número de 1 a 5 e saiba se foi o número sorteado. '))

while escolha != numeroEscolhido:
    escolha = int(input('Continue Tentando!\n'))

if escolha == numeroEscolhido:
    print('Parabéns, você acertou o número sorteado!')

    




