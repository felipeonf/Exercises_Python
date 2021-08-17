import random
lista = []
i = 0 
while i < 4 :
    lista.append(input(f'Digite o nome do {1+i}° aluno: '))
    i+=1

random.shuffle(lista)

print(f'A ordem de apresentação escolhida foi {lista}')
