soma = 0
maior = 0
menor = 0
cont = 1
while True:
    numero = int(input('Digite um número: '))
    soma += numero
    if cont == 1 and numero > maior:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    opcao = input('Deseja continuar(s/n)? ')
    if opcao == 'n':
        break
    cont += 1
media = soma / cont
print()
print(f'A media dos {cont} números digitados é {media}')
print(f'O maior valor digitado é {maior} e o menor é {menor}')
    