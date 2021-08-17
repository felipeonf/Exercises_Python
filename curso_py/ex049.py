valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado, não vou adicionar!')
    else:
        valores.append(valor)
    opcao = input('Deseja continuar(s/n) ?').strip().lower()[0]
    if opcao == 'n':
        break
print(f'Você digitou os valores {sorted(valores)}')
