#programa que calcula descontos de acordo com os tipos de pagamentos
print('>='*10,'CASAS FELPS','>='*10)
preco = float(input('Qual é o preço do seu produto? R$'))
print('As opções de pagamento são: ')
print('''(1) - À VISTA NO DINHEIRO OU CHEQUE
(2)- À VISTA NO CARTÃO
(3)- EM ATÉ 2X NO CARTÃO
(4)- 3X OU MAIS NO CARTÃO''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print(f'10% de desconto. Preço final do produto = R${preco*0.9}')
elif opcao == 2:
    print(f'5% de desconto. Preço final do produto = R${preco*0.95}')
elif opcao == 3:
    parcela = preco / 2
    print(f'Nenhum desconto. Preço das parcelas = R${parcela}')
elif opcao == 4:
    total = preco + (preco * 20 /100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'20% de juros, serão {totalparc} parcelas no valor de R${parcela}')
    print(f'O preço final do produto vai ser de R${total}')
else:
    print('Opção inválida, tente novamente!')
