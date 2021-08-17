'''
Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai
perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
a) qual é a maior idade lida
b) quantos homens foram cadastrados
c) qual é a idade da mulher mais jovem
d) qual é a média de idade entre os homens'''
print('>>>>>>>>>> Leitura de dados >>>>>>>>>>')
numero_homens = 0
numero_mulheres = 0
idades_homens = 0
maior_idade = 0
n_pessoas = 0
menor_idade_mulher = 0
while True:
    print(f'.......... Cadastro {n_pessoas+1}° pessoa ..........')
    n_pessoas += 1
    sexo = input('Digite seu sexo: ').strip().lower()[0]
    if sexo  == 'm':
        idade = int(input('Digite sua idade: '))
        idades_homens += idade
        numero_homens += 1
        if idade > maior_idade:
            maior_idade = idade
    elif sexo == 'f':
        numero_mulheres += 1
        idade = int(input('Digite sua idade: '))
        if idade > maior_idade:
            maior_idade = idade
        if numero_mulheres == 1:
            menor_idade_mulher = idade
        elif idade < menor_idade_mulher:
            menor_idade_mulher = idade
    else:
        print('Sexo inválido, Tente novamente! ')
    opcao = input('Deseja continuar? ').strip().lower()[0]
    if opcao == 'n':
        break
print(f'A maior idade lida foi {maior_idade}')
print(f'A quantidade de homens cadastrados foi {numero_homens}')
print(f'A idade da mulher mais jovem é {menor_idade_mulher}')
print('A média de idade entre os homens é {:.2f}'.format(idades_homens/numero_homens))
