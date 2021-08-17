'''Crie um programa que preencha automaticamente (usando lógica, não apenas
atribuindo diretamente) um vetor numérico com 15 posições com os primeiros
elementos da sequência de Fibonacci:
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'''
termo1 = 1
termo2 = 2
lista = []
for termo in range(0,16):
    if termo == 0:
        lista.append(0)
    elif termo == 1 or termo == 2:
        lista.append(1)
    else:
        termo3 = termo1 + termo2
        lista.append(termo3)
        termo1 = termo2
        termo2 = termo3
print(lista)
        