numeros = []
pares = []
impares = []
for num in range(7):
    numero = int(input(f'{num+1}° numero: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
numeros.append(pares)
numeros.append(impares)
print(f'Os números pares que digitou são: {sorted(numeros[0])}')
print(f'Os números ímpares que digitou são: {sorted(numeros[1])}')
