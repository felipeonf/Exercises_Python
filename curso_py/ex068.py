from time import sleep
def contador(i,f,p): 
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)
    if i > f:
        for num in range(i,f-1,-p):
                print(num,end=' ',flush=True)
                sleep(0.5)
    elif i < f:
        for num in range(i,f+1,p):
            print(num,end=' ',flush=True)
            sleep(0.5)
    print('Fim!')
    linha()
def linha():
    print('+='*15)


contador(1,10,1)
contador(10,0,-2)
print('Agora é sua vez de escolher a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)
