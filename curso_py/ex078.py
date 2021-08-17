def leiaInt(mensagem):
    while True:
        try:
            inteiro = int(input(mensagem))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Digite um inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por não escolher nenhum número inteiro')
            return 0
        else:
            return inteiro

            
def leiaFloat(mensagem):
    while True:
        try:
            real = float(int(input(mensagem)))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Digite um real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por não escolher nenhum número real')
            return 0
        else:
            return real


num1 = leiaInt('Digite um inteiro: ')
num2 = leiaFloat('Digite um real: ')
print(f'O número inteiro digitado foi {num1} e o real foi {num2}')
