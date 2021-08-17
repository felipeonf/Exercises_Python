valores = []
for v in range(5):
    valor = int(input('Digite um valor: '))
    if v == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Valor adicionado no final da lista')
    else:
        posicao = 0
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao,valor)
                print(f'Valor adicionado na posicao {posicao}')
                break
            posicao += 1
print(f'A lista ficou assim : {valores}')
