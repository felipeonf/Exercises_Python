lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = input('Deseja continuar?(s/n) ').strip().lower()[0]
    if opcao == 'n':
        break
print(f'A quantidade de valores digitados foi {len(lista)}')
print(f'Os valores em ordem decrescente são {sorted(lista,reverse=True)}')
print(f'O valor 5 apareceu na lista {lista.count(5)} vezes')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')