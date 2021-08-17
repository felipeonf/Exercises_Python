from random import randint
acimacinco = 0
divtres = 0
print('Os números sorteados foram:')
for num in range(0,21):
    numero = randint(0,10)
    print(numero,end=' ')
    if numero > 5:
        acimacinco += 1
    if numero % 3 == 0:
        divtres += 1
print(f'\nSão {acimacinco} números sorteados acima de cinco')
print(f'São {divtres} números sorteados divisíveis por três')   
 