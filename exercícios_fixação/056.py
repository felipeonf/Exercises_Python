'''
Crie um programa que leia vários números pelo teclado e mostre no final o
somatório entre eles.
Obs: O programa será interrompido quando o número 1111 for digitado
'''
soma = 0
qtde = 0
print('Digite a quantidade de números que quiser e veja a soma entre eles, Para cancelar a contagem digite 1111')
while True:
    num = int(input(f'Digite o {qtde+1}° número: '))
    if num == 1111:
        break
    soma += num
    qtde += 1
print(f'A soma entre os {qtde} números digitados é {soma}')
    