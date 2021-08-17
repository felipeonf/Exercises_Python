tupla = (int(input('1° valor: ')),int(input('2° valor: ')),int(input('3° valor: ')),int(input('4° valor: ')))
print(f'Você digitou os valores {tupla}')
if 9 in tupla:
    print(f'O número 9 aparece {tupla.count(9)} vezes')
else:
    print('Não há aparições do número 9 na sequência')
if 3 in tupla:
    print(f'A primeira aparição do número 3 foi na {tupla.index(3)+1}° posição')
else:
    print('Não há o elemento 3 na sequência')
print('Elementos pares da sequência:',end= ' ')
pares = 0
for elemento in tupla:
    if elemento % 2 == 0:
        pares += 1
        print(elemento,end =' ')
if pares == 0:
    print('Não há números pares',end =' ')
