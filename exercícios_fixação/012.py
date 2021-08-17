#  Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.

precoProduto = float(input('Digite o preço de um produto: '))
desconto = float(input('Digite o desconto do produto em porcentagem: '))
desconto_calculado = (100 - desconto) / 100
print('O produto com desconto de {} % ficará com o valor de R$ {:.2f}'.format(desconto,precoProduto * desconto_calculado))


