dici = {}
dici['nome'] = input('Nome: ')
dici['média'] = float(input(f'Media de {dici["nome"]}: '))
print(f'=> Nome é igual a {dici["nome"]} ')
print(f'=> Média é igual a {dici["média"]} ')
if dici['média'] >= 7.0:
    dici['situacao'] = 'Aprovado'
elif 5 <= dici['média'] < 7.0:
    dici['situacao'] = 'Recuperação'
else:
    dici['situacao'] = 'Reprovado'
print(f'=> A situação do aluno é igual a {dici["situacao"]} ')