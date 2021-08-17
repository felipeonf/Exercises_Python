def lista(arquivo):
    lista = []
    for linha in arquivo:
        if '#' in  linha:
            indice = linha.find("#")
            linha = linha[:indice]
            if linha != '':
                lista.append(linha.strip('\n').strip(' ').strip('\t').strip(''))
        else:
            lista.append(linha.strip('\n').strip(' ').strip('\t').strip(''))
    return lista
    

import os
arquivo = open(input(), 'r')
if arquivo.readline(2) == 'P1':
    arquivo.seek(0)
    lista = lista(arquivo)
    lista_informacoes = lista[0:2]
    for i in range(0,2):
        lista.remove(lista[0])
    lista_auxiliar = []
    for elemento in lista:
       lista_auxiliar.append(list(elemento))
    lista_nova = []
    print(lista_auxiliar)
    for elemento in lista_auxiliar:
        for pixel in elemento:
            if pixel != ' ':
                lista_nova.append(pixel)
    print(lista_nova)
    lista_int = []
    for elemento in lista_nova:
        if elemento == '1':
            lista_int.append(1)
    print(lista_int.count(1))
else:
    arquivo.seek(0)
if arquivo.readline(2) == 'P2':
    arquivo.seek(0)
    lista = lista(arquivo)
    lista_informacoes = lista[0:3]
    valor_comparacao = int(lista_informacoes[2])/2
    for i in range(0,3):
        lista.remove(lista[0])
    count = 0
    lista_auxiliar = []
    while count < len(lista):
        variavel = lista[count].split()
        while len(variavel) < 3:
            count += 1
            variavel_aux = lista[count]
            variavel += variavel_aux.split()
        count+=1
        lista_auxiliar.append(variavel)
    contagem = 0
    for elemento in lista_auxiliar:
        lista_comparacao = []
        for valor in elemento:
            valor = int(valor)
            lista_comparacao.append(valor)
        for elemento in lista_comparacao:
            if elemento >valor_comparacao:
                contagem +=1
    print(contagem)
else:
    arquivo.seek(0)
if arquivo.readline(2) == 'P3':
    arquivo.seek(0)
    lista= lista(arquivo)
    lista_informacoes = lista[0:3]
    valor_comparacao = int(lista_informacoes[2])/2
    for i in range(0,3):
        lista.remove(lista[0])
    count = 0
    lista_auxiliar = []
    while count < len(lista):
        variavel = lista[count].split()
        while len(variavel) < 3:
            count += 1
            variavel_aux = lista[count]
            variavel += variavel_aux.split()
        count+=1
        lista_auxiliar.append(variavel)
    contagem = 0
    for elemento in lista_auxiliar:
        lista_comparacao = []
        for valor in elemento:
            valor = int(valor)
            lista_comparacao.append(valor)
        media = sum(lista_comparacao)/3
        if media > valor_comparacao:
            contagem +=1
    print(contagem)