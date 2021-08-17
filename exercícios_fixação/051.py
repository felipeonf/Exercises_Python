''' Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela
qual foi o maior e qual foi o menor preço digitados.'''
maiscaro = 0
maisbarato = 0
for produto in range(1,9):
    preco = float(input(f'{produto}° produto: R$ '))
    if produto == 1:
        maiscaro = preco
        maisbarato = preco
    if preco > maiscaro:
        maiscaro = preco
    if preco < maisbarato:
        maisbarato = preco
print(f'O produto mais caro ficou R${maiscaro} e o mais barato R${maisbarato}')
