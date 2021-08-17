''' Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.
O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
a) O nome da pessoa mais velha
b) O nome da mulher mais jovem
c) A média de idade do grupo
d) Quantos homens tem mais de 30 anos
e) Quantas mulheres tem menos de 18 anos'''
pessoa_velha = ''
idade_pessoa_velha = 0
nome_mulher_jovem = ''
numero_pessoas = 0
homens_30 = 0
mulheres_18 = 0
idades = 0
idade_mulher_jovem = 0
n_mulheres = 0
print('>>>>>>>>>> Leitura de dados >>>>>>>>>>')
while True:
    print(f'.......... Cadastro {numero_pessoas+1}° pessoa ..........')
    numero_pessoas += 1
    sexo = input('Digite o seu sexo: ').strip().lower()[0]
    if sexo == 'm':
        nome = input('Digite o seu nome: ')
        idade = int(input('Digite a sua idade: '))
        idades += idade
        if idade > 30:
            homens_30 += 1
        if idade > idade_pessoa_velha:
            idade_pessoa_velha = idade
            pessoa_velha = nome
    elif sexo =='f':
        n_mulheres += 1
        nome = input('Digite o seu nome: ')
        idade = int(input('Digite a sua idade: '))
        idades += idade
        if idade < 18:
            mulheres_18 += 1
        if idade > idade_pessoa_velha:
            idade_pessoa_velha = idade
            pessoa_velha = nome
        if n_mulheres == 1:
            idade_mulher_jovem = idade
            nome_mulher_jovem = nome
        elif n_mulheres > 1:
            if idade < idade_mulher_jovem:
                nome_mulher_jovem = nome
    else:
        print('Opção inválida. Tente novamente!')          
    opcao = input('Deseja continuar(s/n)? ').strip().lower()[0]
    if opcao == 'n':
        break
print(f'O nome da pessoa mais velha é {pessoa_velha}')
print(f'O nome da mulher mais jovem é {nome_mulher_jovem}')
print('A média de idade do grupo é {:.2f}'.format(idades/numero_pessoas))
print(f'A quantidade de homens que possuem mais de 30 anos é {homens_30}')
print(f'A quantidade de mulheres que tem menos de 18 anos é {mulheres_18}')
    