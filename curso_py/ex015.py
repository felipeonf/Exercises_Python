frase =  ' fe l i p e oli vei ra'

lista = []
for char in frase:
    lista.append(char)

for elemento in lista:
    if elemento == ' ':
        lista.remove(elemento)
print(lista)