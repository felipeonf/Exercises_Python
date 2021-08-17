from time import sleep
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print('''>>>>>>>>>>> MENU >>>>>>>>>>>
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
while True:
    opcao = int(input('>>>>>>>>>>>> Opção >>>>>>>>>>>>\n'))
    if opcao > 5 or opcao < 0:
        print(f'Opção inválida, tente novamente!')
    elif opcao == 1:
        print(f'A soma dos dois valores é {numero1+numero2}')
    elif opcao == 2:
        print(f'A multiplicação dos dois valores é {numero1 * numero2}')
    elif opcao == 3:
        if numero1 > numero2:
            print(f'O maior número entre {numero1} e {numero2} é o {numero1}')
        elif numero2 > numero1: 
            print(f'O maior número entre {numero1} e {numero2} é o {numero2}')
        else:
            print(f'Os números são iguais')
    elif opcao == 4:
        numero1 = int(input('Digite o novo primeiro número: '))
        numero2 = int(input('Digite o novo segundo número: '))
    elif opcao == 5:
        print('Saindo do programa....')
        sleep(1)
        break




