cadastro = {}
idades = 0
acima_media = []
pessoas = 1
while True:
    nome = input('Nome: ')
    sexo = input('Sexo: [m/f] ').strip().lower()[0]
    if sexo in 'mf':
        idade = int(input('Idade: '))
        cadastro[pessoas] = [nome,sexo,idade]
        idades += idade
        opcao = input('Deseja continuar? [s/n] ').strip().lower()[0]
        if opcao == 'n':
            break
        else:
            pessoas += 1
    else:
        print('Sexo inválido, digite apenas m ou f! ')
        print()
media = idades/ pessoas
print(f'=> Foram cadastradas {pessoas} pessoas')
print('=> A média de idade é de {:.2f}'.format(media))
print('=> As mulheres cadastradas foram:',end=' ')
for chave, valor in cadastro.items():
    if valor[1] == 'f':
        print(valor[0],end=' ')
print(f'\n=> A lista de pessoas que estão acima da média: ')
for chave, valor in cadastro.items():
    if valor[2] > media:
        print(cadastro[chave])
print(f'{">>"*5} ENCERRADO {"<<"*5}')
