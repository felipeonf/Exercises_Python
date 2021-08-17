''' O programa acima vai ter um problema quando digitarmos o primeiro valor
maior que o último. Resolva esse problema com um código que funcione em qualquer
situação.'''
inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))
incremento = int(input('Digite o incremento: '))
if inicial < valor_final:
    for num in range(inicial,valor_final+1,incremento):
        print(num,end=' ')
    print('Acabou!')
elif inicial > valor_final:
    for num in range(inicial,valor_final-1,-incremento):
        print(num,end=' ')
    print('Acabou!')
else:
    print('Os números são iguais! Tente novamente!')
