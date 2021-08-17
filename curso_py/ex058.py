from random import randint
from time import sleep
print(f'{"=>"*10} MEGA SENA {"=<"*10}')
jogos = int(input('Digite a quantidade de jogos: '))
lista_jogos = []
while jogos > 0:
    lista_jogos.append([randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)])
    jogos -=1
print(f'{"=>"*5} Sorteando os jogos{"=<"*5}')
for jogo in range(len(lista_jogos)):
    print(f'Jogo {jogo+1} : {lista_jogos[jogo]} ')
    sleep(1)
print(f'{"=>"*10} BOA SORTE! {"=<"*10}')
