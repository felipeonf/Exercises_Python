''' Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
a) Quantos homens foram cadastrados
b) Quantas mulheres foram cadastradas
c) A média de idade do grupo
d) A média de idade dos homens
e) Quantas mulheres tem mais de 20 anos'''
homens = 0
mulheres = 0
idades = 0
idadeshomens = 0
mulheresvinte = 0
for pessoa in range(1,6):
    print('>>>>>>>>>>>>>>> {}° CADASTRO >>>>>>>>>>>>>>>'.format(pessoa))
    idade = int(input(f'Idade: '))
    sexo = input(f'Sexo(m/f): ').strip().lower()
    if sexo == 'm':
        homens += 1
        idadeshomens += idade
    else:
        mulheres += 1
        if idade > 20:
            mulheresvinte +=1
    idades += idade
media = idades / 5
mediahomens = idadeshomens / homens
print()
print(f'Foram cadastrados {homens} homens')
print(f'Foram cadastradas {mulheres} mulheres')
print(f'A média de idade do grupo é {media}')
print(f'A média de idade dos homens é {mediahomens}')
print(f'Há {mulheresvinte} mulheres com mais de vinte anos no cadastro')
