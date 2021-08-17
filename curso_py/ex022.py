soma = 0
for num in range(0,6):
    number = int(input('Digite um número inteiro: '))
    if number % 2 == 0:
        soma += number
print(f'A soma dos números pares digitados são {soma}')
