#  Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
#dela e depois mostre se ela pode ou não votar.

anoNascimento = int(input('Que ano você nasceu? '))
idade = 2020-anoNascimento
if idade >= 18:
    print('Você já pode votar.')

elif idade == 16 or idade == 17:
    print('Você pode votar, mas é opcional no momento.')

else:
    print('Você ainda não pode votar.')
