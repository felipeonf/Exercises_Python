#Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
#para todos, mas especialmente para mulheres. Faça um programa que leia nome,
#sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
# - Homens ganham 5% de desconto
# - Mulheres ganham 13% de desconto

name = input('What´s your name? ')
sex = input('Put your sex (m/w): ')
buyValue = float(input('How much you will spent? '))

if sex == 'm':
    print(f'You will spent R${buyValue*0.95} now.')
elif sex == 'w':
    print(f'Congratulations! You will spent R${buyValue*0.87} now.')



