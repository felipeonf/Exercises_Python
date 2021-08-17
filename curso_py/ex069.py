def maior (*num):
    cont = 0
    maior = 0
    num = list(num)
    for valor in num:
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor digitado entre {num} foi {maior}')
    linha()    
def linha():
    print('~'*50)


maior(1,2,3,4,5)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
