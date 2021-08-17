maior = 0
menor = 0
for peso in range(1,6):
    kg = float(input(f'{peso}° pessoa.Qual é o seu peso? Kg '))
    if peso == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        if kg < menor:
            menor = kg
print(f'O maior peso foi {maior} e o menor peso foi {menor}')




