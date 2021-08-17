#detector de palíndromos
frase = input('Digite uma frase: ').strip().upper()
sep = frase.split()
junto = ''.join(sep)
if junto == junto[::-1]:
    print('A frase é um palíndromo')
