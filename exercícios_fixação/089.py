'''Crie um programa que melhore o procedimento Gerador() da questão anterior
para que o programador possa escolher uma entre três bordas:
 +-------=======------+ Borda 1
 ~~~~~~~~:::::::~~~~~~~ Borda 2
 <<<<<<<<------->>>>>>> Borda 3
Ex: Uma chamada válida seria Gerador("Portugol Studio", 3, 2)
~~~~~~~~:::::::~~~~~~~
 Portugol Studio
 Portugol Studio
 Portugol Studio
~~~~~~~~:::::::~~~~~~~'''
def Gerador(mensagem,repeticoes,borda):
    if borda == 1:
        print('~~~~~~~~{}~~~~~~~~'.format(':'*len(mensagem)))
        while repeticoes > 0:
            print(' '*6,mensagem)
            repeticoes -= 1
        print('~~~~~~~~{}~~~~~~~~'.format(':'*len(mensagem)))
    elif borda == 2:
        print('+-------{}-------+'.format('='*len(mensagem)))
        while repeticoes > 0:
            print(' '*6,mensagem)
            repeticoes -= 1
        print('+-------{}-------+'.format('='*len(mensagem)))
    else:
        print('$$$$$$$${}$$$$$$$$'.format('@'*len(mensagem)))
        while repeticoes > 0:
            print(' '*6,mensagem)
            repeticoes -= 1
        print('$$$$$$$${}$$$$$$$$'.format('@'*len(mensagem)))



mensagem = input('Digite uma mensagem: ')
repeticoes = int(input('Digite as repetições: '))
borda = int(input('''Escolha uma borda:
~~~~~~~~::::::~~~~~~~~ [1]
+-------======-------+ [2]
$$$$$$$$@@@@@@$$$$$$$$ [3]'''))
Gerador(mensagem,repeticoes,borda)
