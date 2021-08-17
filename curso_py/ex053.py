lista = []
lista.append(input('Digite uma expressão: '))
aberto = 0
fechado = 0
for elemento in lista[0]:
    if elemento == '(':
        aberto += 1
    elif elemento == ')':
        fechado += 1
if aberto == fechado:
    print('Essa expressão é válida')
else:
    print('Essa expressão é invalida')
