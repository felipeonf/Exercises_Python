#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)e mostre quantos dólares ela pode comprar.
#  Considere US$1,00 = R$3,45.
value = float(input('Digite qual valor deseja converter: '))

dolarAtual = 5.2883
print('Com a quantia de R${} você pode comprar US ${:.1f}.'.format(value,value/dolarAtual))
