primeiro = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
#calc = primeiro + (termo - 1)* razao
for t in range(1,11):
    termo = primeiro + ((t-1)*razao)
    print(f'a{t} = {termo}',end = '  ')
#solução secundária
p  = int(input())
r = int(input())
posi = 0
for t in range(1,11,r):
    posi += 1
    print(f'a{posi} = {t}')

