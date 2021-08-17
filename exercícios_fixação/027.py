'''Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
 - Média até 4.9: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: APROVADO'''
nota1 = float(input('Digite sua primeira nota:  '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/ 2

print(f'Sua média é {media}')
if media <= 4.9:
    print('REPROVADO') 
elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')
