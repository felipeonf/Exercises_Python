valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = input('Deseja continuar(s/n)? ').strip().lower()[0]
    if opcao == 'n':
        break
for elemento in valores:
    if elemento % 2 == 0:
        pares.append(elemento)
    else:
        impares.append(elemento)
print(f'Valores digitados = {valores}')
print(f'Valores digitados pares = {pares}')
print(f'Valores digitados ímpares = {impares}')
