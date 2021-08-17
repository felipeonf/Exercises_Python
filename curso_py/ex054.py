pessoas = []
dados = []
while True:
    nome = input('Digite seu nome: ').strip()
    peso = int(input('Digite seu peso: Kg '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    opcao = input('Deseja continuar? [s][n] ').strip().lower()[0]
    if opcao == 'n':
        pesadas = []
        leves = []
        for pessoa in pessoas:
            if pessoa[1] >= 100:
                pesadas.append(pessoa[0])
            elif pessoa [1] <= 70:
                leves.append(pessoa[0])
        print(f'Foram cadastradas {len(pessoas)} pessoas ')
        print(f'As pessoas mais pesadas foram: {pesadas}')
        print(f'As pessoas mais leves foram: {leves}')
        break
