'''Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
a) Qual é a média de idade do grupo
b) Quantas pessoas tem mais de 18 anos
c) Quantas pessoas tem menos de 5 anos
d) Qual foi a maior idade lida'''
idades = 0
maisdezoito = 0
menorcinco = 0
maior = 0
for pessoa in range(1,11):
    idade = int(input(f'Idade da {pessoa}° pessoa: '))
    if idade == 1:
        maior = idade
    if idade > maior:
        maior = idade
    if idade > 18:
        maisdezoito += 1
    if idade < 5:
        menorcinco += 1
    idades += idade
media = idades / 10
print()
print(f'A media das idades digitadas é {media}')
print(f'Entre as idades digitadas, {maisdezoito} pessoas possuem mais de 18 anos')
print(f'Entre as idades digitadas, {menorcinco} pessoas possuem menos de 5 anos')
print(f'A maior idade digitada foi {maior}')
