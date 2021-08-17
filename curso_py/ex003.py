nome = input('Digite o seu nome: ')
print(f'Seu nome em minúsculo é : {nome.lower()}')
print(f'Seu nome em caixa alta é : {nome.upper()}')

lista = []
for char in nome:
    lista.append(char)
for elemento in lista:
    if elemento == ' ':
        lista.remove(elemento)
        
print(f'O tamanho do seu nome completo é : {len(lista)}')

sep = nome.split()

print(f'O tamanho do seu primeiro nome é : {len(sep[0])}')