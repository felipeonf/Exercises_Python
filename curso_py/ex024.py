#detector de primos
numero = int(input('Digite um número: '))
div = 0
for contador in range(1,numero+1):
    if numero % contador == 0:
        print('\033[33m',end='')
        div += 1
    else:
        print('\033[31m',end='')
    print(contador,end=' ')
print(f'\n\033[mO número {numero} foi divisível {div} vezes')
if div == 2:
    print('Por isso ele é PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')

