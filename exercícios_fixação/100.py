""" Melhore o exercício 96, criando além da função Media() uma outra função
chamada Situacao(), que vai retornar para o programa principal se o aluno está
APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber como
parâmetro o resultado retornado pela função Media()."""
def Media(nota1, nota2):
    return (nota1 + nota2) / 2





nota1,nota2 = (float(x) for x in input('Digite a nota 1 e 2: ').split())
media = Media(nota1,nota2)
print(f'Média = {Media(nota1, nota2)}')



Situacao(media)
