lista_palavras = ['gato','rato','coelho']
lista_letras = []
[lista_letras.append(palavra[caracter]) for palavra in ['gato','rato','cachorro'] for caracter in range(len(palavra)) if palavra[caracter] not in lista_letras]
print(lista_letras)

