''' Faça um programa que tenha um procedimento chamado Contador() que recebe
três valores como parâmetro: o início, o fim e o incremento de uma contagem. O
programa principal deve solicitar a digitação desses valores e passá-los ao
procedimento, que vai mostrar a contagem na tela.'''
def Contador(inicio,fim,incremento):
    for num in range(inicio,fim,incremento):
        print(num,end=' >>> ')
    print('FIM')
inicio = int(input('Digite o início da contagem: '))
fim = int(input('Digite o fim da contagem: '))
incremento = int(input('Digite o incremento da contagem: '))
Contador(inicio,fim,incremento)