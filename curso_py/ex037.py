soma = 0
quantidade = 0
print('Digite números abaixo 2para ver a sua soma. Para parar digite 999')
while True:
    numerodigitado = int(input())
    if numerodigitado == 999:
        break
    else:
        soma += numerodigitado
        quantidade += 1
print(f'A soma dos {quantidade} valores digitados é {soma}')
