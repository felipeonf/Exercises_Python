''' Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa
vai parar quando for digitada a idade 999. No final, mostre quantos alunos
existem na turma e qual é a média de idade do grupo.'''
print('>>>>>>>>>> Leitura de dados da turma >>>>>>>>>>')
idades = 0
qtde = 0
print('Vamos realizar o cadastro, para sair digite 999')
while True:
    idade = int(input(f'Digite a idade do {qtde+1}° aluno: '))
    if idade == 999:
        break
    else:
        idades += idade
        qtde += 1
print('A média de idade dos {} alunos cadastrados é {:.2f} '.format(qtde,idades/qtde))
