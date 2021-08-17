''' Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 +
450 + 400 + 350 + 300 + ... + 50 + 0'''
soma = 0
for num in range(500,-1,-50):
    soma += num
print(soma)
