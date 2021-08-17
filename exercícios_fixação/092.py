'''Crie uma lógica que leia um número inteiro e passe para um procedimento
ParOuImpar() que vai verificar e mostrar na tela se o valor passado como
parâmetro é PAR ou ÍMPAR.'''
def ParOuImpar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
numero = int(input('Digite um número: '))
print(ParOuImpar(numero))