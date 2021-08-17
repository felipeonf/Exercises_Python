'''Crie um programa que preencha automaticamente (usando lógica, não apenas
atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
5 3 5 3 5 3 5 3 5 3
0 1 2 3 4 5 6 7 8 9'''
lista = []
for num in range(0,9):
    if num % 2 == 0:
        lista.append(5)
    else:
        lista.append(3)
print(lista)
