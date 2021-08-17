# Faça um algoritmo que pergunte a distância que um passageiro deseja
#percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
#viagens até 200Km e R$0.45 para viagens mais longas.

distance = int(input('How far you want to travel? '))

if distance > 200 :
    print(f'The ticket will cost R${distance* 0.45}')
else:
    print(f'The ticket will cost R${distance* 0.50}')

