
"""
numero = int(input("Fatorial de: ") )

resultado=1
for n in range(1,numero+1):
    resultado *= n

print(resultado)
-------------------------------------------------------------------------------------------------------------------
numero = int(input('Digite um número inteiro: '))
resultado = 1 #o valor mínimo de um fatorial de um número é 1
fatorial = 1 #contador para multiplicar o fatorial, comecarei de tras pra frente.

while fatorial <= numero: #enquanto o contador for menor ou igual ao número
    resultado *= fatorial #multiplico o contador pelo resultado
    fatorial += 1 #aumento o contador para fazer o fatorial
print(f'{numero}! = {resultado}') #no final do laço vai haver o resultado do fatorial do numero digitado.

"""
numero = int(input('Digite um número para calcular seu fatorial: '))
contador = numero
fatorial = 1
print(f'{numero}! = ',end='')
while contador > 0:
    print(contador,end=' ')
    print(f'X' if contador > 1 else '= ',end=' ')
    fatorial *= contador
    contador -= 1
print(fatorial)
    
