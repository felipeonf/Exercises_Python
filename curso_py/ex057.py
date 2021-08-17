matriz = []
elementos = []
pares = []
for linha in range(3):
    elementos.clear()
    for coluna in range(3):
        elemento = int(input(f'Digite o valor para {[linha,coluna]} : '))
        elementos.append(elemento)
        if elemento % 2 == 0:
            pares.append(elemento)
    matriz.append(elementos[:])
terceira_coluna = []
for linha in range(3):
    for coluna in range(3):
        print(f'[  {matriz[linha][coluna]}  ]',end=' ')
        if coluna == 2:
            terceira_coluna.append(matriz[linha][coluna])
    print()
print(f'A soma dos {pares} valores pares digitados é {sum(pares)}')
print(f'A soma dos valores {terceira_coluna} encontrados na terceira coluna é {sum(terceira_coluna)}')
print(f'O maior valor da primeira linha: {matriz[0]} é {max(matriz[0])}')