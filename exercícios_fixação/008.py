#  Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
distancia = float(input('Digite uma distância em metros: '))
print(f'A distância de {distancia}m corresponde a:\n')
print('*'*(50))
print(f'{distancia/1000} km            {distancia*10} dm')
print(f'{distancia/100} hm            {distancia*100} cm')
print(f'{distancia/10} dam            {distancia*1000} mm')

