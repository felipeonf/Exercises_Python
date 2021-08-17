# Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
#média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
#não um bom aproveitamento (se ficou acima da média 7.0).

name = input('What´s your name? ')
score1 , score2 = (float(x) for x in input('Set two scores: \n').split())
a =  (score1 + score2) / 2
if a > 7.0 :
    print(f'Your average is {a}. Congratulations {name}, you´re usefullnes!')
else:
    print(f'Your average is {a}. Practice more my friend!')