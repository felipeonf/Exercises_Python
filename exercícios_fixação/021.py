# Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
# situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.

born = int(input('When were you born? '))
age = 2020 - born 
if age < 18:
    print(f'There are {18-age} years for you enlistment')
else:
    print(f'Has been passed {age-18} years for you enlistment')