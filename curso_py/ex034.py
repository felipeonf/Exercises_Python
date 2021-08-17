'''primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = 1
while termo <= 10:
    if termo == 1:
        print(f'{termo}° termo = {primeiro} ')
    if termo != 1:
        print(f'{termo}° termo = {(primeiro) + (termo-1)*razao} ')
    termo += 1
'''
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
count = 1
while count <= 10:
    print(f'{termo} - ',end=' ')
    termo += razao
    count +=1
print('Acabou!')
