'''
 Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
tabela a seguir:
 - Carros populares (aluguel de R$90 por dia)
 - Até 100Km percorridos: R$0,20 por Km
 - Acima de 100Km percorridos: R$0,10 por Km
 - Carros de luxo (aluguel de R$150 por dia)
 - Até 200Km percorridos: R$0,30 por Km
 - Acima de 200Km percorridos: R$0,25 por Km
 '''
tipoCarro = input('Qual o tipo do carro alugado?(popular/luxo) ')
diasAlugados = int(input('Quantos dias ele foi alugado? '))
kmPercorridos = float(input('Quantos km foram percorridos? '))

if tipoCarro == 'popular':
    if kmPercorridos <= 100:
        valor = kmPercorridos * 0.20 + 90 * diasAlugados
        print(f'O valor a ser pago será de R${valor}')
    elif kmPercorridos > 100:
        valor = kmPercorridos * 0.10 + 90 * diasAlugados
        print(f'O valor a ser pago será de R${valor}')

elif tipoCarro == 'luxo':
    if kmPercorridos <= 200:
        valor = kmPercorridos * 0.30 + 150 * diasAlugados
        print(f'O valor a ser pago será de R${valor}')
    elif kmPercorridos > 200:
        valor = kmPercorridos * 0.25 + 150 * diasAlugados
        print(f'O valor a ser pago será de R${valor}')


