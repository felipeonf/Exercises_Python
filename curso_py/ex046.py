marcador = '*'*20
tupla = (input(f'{marcador}\n1° produto: '),float(input('Seu preço: ')),
input(f'{marcador}\n2° produto: '),float(input('Seu preço: ')),
input(f'{marcador}\n3° produto: '),float(input('Seu preço: ')),
input(f'{marcador}\n4° produto: '),float(input('Seu preço: ')),
input(f'{marcador}\n5° produto: '),float(input('Seu preço: ')),
input(f'{marcador}\n6° produto: '),float(input('Seu preço: ')))
print(f'{marcador} Preços {marcador}')
cont = 1
par = 0
total = 0
while cont <= 6:
    print(f'{tupla[par]:.<30} R$ {tupla[par+1]}')
    total += tupla[par+1]
    cont+=1
    par += 2
print(marcador*2+'*'*8)
print(f'{"Total":.<30} R$ {total}')

