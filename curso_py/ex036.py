# fibonacci
sequencia = int(input('Digite a quantidade de número que quer na sequência: '))
termo1 = 0
termo2 = 1
cont = 3
if sequencia == 0:
    print(0)
    exit()
if sequencia == 1 or sequencia == 2:
    print(1)
    exit()
print(f'{termo1} {termo2}',end= ' ')
while cont <= sequencia:
    termo3 = termo1 + termo2
    print(termo3,end=' ')
    termo1 = termo2
    termo2 = termo3
    cont+=1

                

