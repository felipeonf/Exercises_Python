maisvelho = 0
nome_mais_velho = ''
idades = 0
mulheres_menos_20 = 0
for pessoa in range(1,5):
    print('**********{}° Pessoa**********'.format(pessoa))
    nome = input('Nome: ').strip()
    sexo = input('Sexo(m/f): ').strip().lower()
    idade = int(input('Idade: '))
    if pessoa == 1 and sexo == 'm':
        maisvelho = idade
        nome_mais_velho = nome
    elif pessoa != 1 and sexo == 'm':
        if idade > maisvelho:
            maisvelho = idade
            nome_mais_velho = nome
    elif sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1
    idades += idade
media = idades / 4
print(f'A média de idades das pessoas selecionadas é {media}')
print(f'O nome do homem mais velho é {nome_mais_velho}')
print(f'A quantidade de mulheres com menos de 20 anos é {mulheres_menos_20}')
