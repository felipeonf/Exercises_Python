'''Crie um programa que tenha uma função Media(), que vai receber as 2 notas de
um aluno e retornar a sua média para o programa principal.'''
def Media(nota1,nota2):
    return (nota1 + nota2)/2
nota1,nota2 = (float(x) for x in input('Digite a nota 1 e 2: ').split())
print(f'Média = {Media(nota1,nota2)}')