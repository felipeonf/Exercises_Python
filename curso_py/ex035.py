from time import sleep
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = 1
mensagem = 'Ok, saindo do programa...'
while termo <= 10:
    if termo == 1:
        print(f'{termo}° termo = {primeiro} ')
    if termo != 1:
        print(f'{termo}° termo = {(primeiro) + (termo-1)*razao} ')
    termo += 1
while True:
    opcao = input('Você quer mostrar mais termos (s/n)?\n').strip().lower()
    if opcao == 's':
        quantidade = int(input('Digite a quantidade que quer mostrar: '))
        if quantidade == 0:
            print(mensagem)
            break
        else:
            cont = 1
            while cont <= quantidade:
                cont += 1
                print(f'{termo}° termo = {(primeiro) + (termo-1)*razao} ')
                termo += 1
    elif opcao == 'n':
        print(mensagem)
        sleep(1)
        break
