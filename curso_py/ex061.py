from random import randint
from time import sleep
import operator
jogadas = {}
for jogador in range(4):
    jogadas[f'Jogador {jogador+1}'] = randint(1,6)
print(f'{">"*10} Valores sorteados {"<"*10}')
for chave,valor in jogadas.items():
    print(f'{chave} tirou {valor}')
    sleep(0.5)
valores = sorted(jogadas.items(),reverse=True , key= operator.itemgetter(1))
print(f'{">"*10} RANKING {"<"*10}')
for posicao in range(1,5):
    print(f'{posicao}° lugar: {valores[posicao-1][0]} que tirou {valores[posicao-1][1]}')
    sleep(1)
