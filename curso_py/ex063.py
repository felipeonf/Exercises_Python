estatisticas = {}
estatisticas['nome'] = input('Digite o nome do jogador: ')
partidas = int(input(f'Quantas partidas {estatisticas["nome"]} jogou? '))
contador = 1
while contador <= partidas:
    estatisticas[f'{contador}° partida'] = int(input(f'Gols {contador}° partida: '))
    contador +=1
print("-="*20)
contador = 0
total_gols = 0
for gols in estatisticas.values():
    if contador == 0:
        print(f'O jogador {estatisticas["nome"]} jogou {partidas} partidas')
    else:
        print(f'{"=>"} Na {contador}° partida, fez {gols} gols.')
        total_gols += gols
    contador += 1
print(f'O total de gols foi {total_gols}')
