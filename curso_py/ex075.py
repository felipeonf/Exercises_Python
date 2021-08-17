def analiseNotas(*notas,situacao=True):
    turma = {}
    turma['notas'] = notas[:-1]
    turma['maior nota'] = max(notas[:-1])
    turma['menor nota'] = min(notas[:-1])
    turma['media'] = sum(notas[:-1])/len(notas[:-1])
    if notas[-1] == True:
        if turma['media'] >= 7.0:
            turma['situacao'] = 'BOA'
        elif 6 <= turma ['media'] < 7.0:
            turma['situacao'] = 'RAZOAVEL'
        elif turma['media'] < 6.0:
            turma['situacao'] = 'RUIM'
    print(turma)


analiseNotas(1,2,3,4,5,6,True)
