estatisticas = {}
gols = []
while True:
    nome = input("Digite o nome do jogador: ")
    partidas = int(input("Quantas partidas ele jogou? "))
    contador = 1
    while contador <= partidas:
        gols.append(int(input(f'Partida {contador}: ')))
        contador += 1
    estatisticas[nome] = gols[:]
    gols.clear()
    opcao = input('Deseja continuar? [s/n] ').strip().lower()[0]
    if opcao == 'n':
        break
print(f'{">"*10} Estatísticas {"<"*10} ')
contador = 0
levantamento = {}
for chave in estatisticas.keys():
    print(f"[{contador}] => Jogador {chave} /// Gols nas partidas => {estatisticas[chave]} - Total de Gols => {sum(estatisticas[chave])}")
    levantamento[contador] = [chave,estatisticas[chave]]
    contador += 1
while True:
    opcao = int(input('Mostrar dados de qual jogador? (Parar parar digite 999) '))
    if opcao > contador and opcao != 999:
        print('Esse código não existe, tente novamente! ')
        print()
    elif opcao == 999:
        print('>>>> ENCERRADO <<<<')
        break
    else:
        print(f'{">"*10} Levantamento do jogador {levantamento[opcao][0]} {"<"*10}')
        contador = 0
        for gol in levantamento[opcao][1]:
            print(f'No jogo {contador+1}, fez {gol} gols')
            contador += 1
      