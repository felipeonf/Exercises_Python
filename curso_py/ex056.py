matriz = []
elementos = []
for linha in range(3):
    elementos.clear()
    for coluna in range(3):
        elementos.append(int(input(f'Digite o valor para {[linha,coluna]} : ')))
    matriz.append(elementos[:])
for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]} ]',end=' ')
    print()
