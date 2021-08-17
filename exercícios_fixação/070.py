''' [DESAFIO] Faça um programa que mostre os 10 primeiros elementos da Sequência
de Fibonacci:
1 1 2 3 5 8 13 21...'''
termos = int(input('Digite a quantidade de termos que quer ver: '))
termo = 1
termo_anterior = 0
print(0,end=' ')
print(1,end=' ')
for num in range(3,termos+1):
        termo3 = termo_anterior + termo
        print(termo3,end=' ')
        termo_anterior = termo
        termo = termo3
