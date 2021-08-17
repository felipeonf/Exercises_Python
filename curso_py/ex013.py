from random import choice
lista = []
i = 0
while i < 4:
    lista.append(input(f'Digite o nome do {1+i}° aluno: '))
    i+=1
print(f'O aluno escolhido foi {choice(lista)}.')







