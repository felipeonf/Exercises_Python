''' Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em
um vetor. No final, mostre:
a) Qual é a média da turma
b) Quantos alunos estão acima da média da turma
c) Qual foi a maior nota digitada
d) Em que posições a maior nota aparece'''
notas = []
acima_media = 0
for aluno in range(1,11):
    notas.append(float(input('Nota: ')))
print('>>>>>>>>>> Informações <<<<<<<<<<')
media = sum(notas)/len(notas)
print('A média de notas da turma é {:.1f}'.format(media))
for aluno in notas:
    if aluno > media:
        acima_media +=1
print(f'{acima_media} alunos estão acima da média')
print(f'A maior nota da turma foi {max(notas)}')
print(f'E apareceu nas posições:')
for posicao in range(len(notas)):
    if notas[posicao] == max(notas):
        print(f'{posicao+1}°',end=' ')
