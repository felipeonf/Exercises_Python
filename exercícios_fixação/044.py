'''Crie um algoritmo que leia o valor inicial da contagem, o valor final e o
incremento, mostrando em seguida todos os valores no intervalo:
Ex: Digite o primeiro Valor: 3
Digite o último Valor: 10
Digite o incremento: 2
Contagem: 3 5 7 9 Acabou!'''
inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))
incremento = int(input('Digite o incremento: '))
if inicial < valor_final:
    for num in range(inicial,valor_final+1,incremento):
        print(num,end=' ')
    print('Acabou!')
