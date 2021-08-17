# conversor bases numericas(binario,octal,hexadecimal)
numero = int(input('Digite um numero inteiro: '))
print('''Escolha a base para converter:
1- Binário
2- Octal
3- Hexadecimal
''')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print(f'O número {numero} convertido para binário é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} convertido para octal é {oct(numero)[2:]}')
   
elif opcao == 3:
    print(f'O número {numero} convertido para hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida, tente novamente.')
