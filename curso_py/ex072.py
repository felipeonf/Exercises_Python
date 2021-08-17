def fatorial(num,show = True):
    fat = 1
    if show != True:
        for contador in range(num, 0, -1):
            fat *= contador
            if contador > 1:
                print(f'{contador} X',end=' ')
            else:
                print(f'{contador}',end=' ')
        print(f'= {fat}')
    else:
        for contador in range(num, 0, -1):
            fat *= contador
        print(fat)

        
numero = int(input('Digite um número: '))
opcao = input('Deseja mostrar os cálculos?[s/n] ').strip().lower()[0]
if opcao == 's':
    fatorial(numero,opcao)
else:
    fatorial(numero)
