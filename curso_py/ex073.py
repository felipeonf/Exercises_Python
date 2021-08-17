def ficha(j='<desconhecido>',g=0):
    print(f'O jogador {j} fez {g} gol(s) no campeonato.')


print('-'*25)
nome = input('Digite o nome do jogador: ')
gols = input('Digite quantos gols ele fez? ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(g=gols)
else:
    ficha(nome,gols)
