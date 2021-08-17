'''[DESAFIO] Desenvolva um aplicativo que tenha um procedimento chamado
Fibonacci() que recebe um único valor inteiro como parâmetro, indicando quantos
termos da sequência serão mostrados na tela. O seu procedimento deve receber
esse valor e mostrar a quantidade de elementos solicitados.
Obs: Use os exercícios 70 e 75 para te ajudar na solução
Ex:
Fibonacci(5) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> FIM
Fibonacci(9) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >> FIM'''
def Fibonacci(termos):
    termo = 1
    termo_anterior = 0
    if termos == 1:
        print(0)
    elif termos == 2:
        print(0,'>>',1,'>>','FIM')
    else:
        print(0,end=' >> ')
        print(1,end=' >> ')
        for num in range(3,termos+1):
            termo3 = termo_anterior + termo
            print(termo3,end=' >> ')
            termo_anterior = termo
            termo = termo3
        print('FIM')
termos = int(input('Digite a quantidade de termos que quer ver: '))
Fibonacci(termos)
