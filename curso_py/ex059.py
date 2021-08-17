#informacoes = [[[nome],[notas],[media]]
from time import sleep
informacoes = []
while True:
    nome = input('Nome do aluno: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    informacoes.append([nome,[nota1,nota2],[media]])
    opcao0 = input('Deseja continuar?[s][n] ').strip().lower()[0]
    if opcao0 == 'n':
        print(f'{">"*10} Boletim {"<"*10} ')
        for aluno in range(len(informacoes)):
            print(f'ALUNO {aluno+1} : {informacoes[aluno][0]} >>> Média: {informacoes[aluno][2]}')
        print(">"*35)
        break
while True:
    opcao1 = int(input('Deseja ver notas de qual aluno? (999 interrompe) '))
    if opcao1 == 999:
        print('FINALIZANDO...')
        sleep(1)
        print(f'{">"*10} Volte Sempre! {"<"*10} ')
        break
    else:
        print(f'Notas de {informacoes[opcao1-1][0]} são {informacoes[opcao1-1][1]}')
