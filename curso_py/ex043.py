tabela = ('Vasco','São Paulo','Chapecoense','Botafogo','Náutico','Fortaleza','Bahia','Cruzeiro',
'Coritiba','ABC','Vitória','Fluminense','Flamengo','Ceará','Goiás','Gama','Brasiliense','Bangu','Internacional','Grêmio')
print(f'Os primeiros cinco colocados da tabela são:',end=' ')
# primeiros colocados da tabela
for elemento in tabela[0:5]:
    if tabela.index(elemento) < 4:
        print(elemento,end=', ')
    else:
        print('e',elemento)
# últimos quatro colocados da tabela
print()
print(f'Os últimos quatro colocados da tabela são:',end=' ')
for elemento in tabela[-4::+1]:
    if tabela.index(elemento) < 19:
        print(elemento,end =', ')
    else:
        print('e',elemento)
# lista com times organizados em ordem alfabetica
print()
print(f'Aqui está uma lista com os times organizados em ordem alfabética:')
print(sorted(tabela))
# posição do time chapecoense na tabela
print()
time = 'Chapecoense'
print(f'O time da Chapecoense se encontra na {tabela.index(time)+1}° posição da tabela')
