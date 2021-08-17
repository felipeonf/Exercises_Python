from time import sleep


def boasVindas():
    mensagem = 'SISTEMA DE AJUDA PyHELP'
    print(f'\033[0;30;43m{"*"*len(mensagem)}')
    print(mensagem)
    print(f'{"*"*len(mensagem)}\n')
def entrada():
    fb = input('\033[1;37;40mFunção ou biblioteca => ')
    return fb
def encerra(fim):
    mensagem = 'ATÉ LOGO!'
    print(f'\033[0;30;41m{"*"*len(mensagem)}')
    print(mensagem)
    print(f'{"*"*len(mensagem)}\033[m\n')
def acesso(funbiblio):
    mensagem = f'ACESSANDO O MANUAL DO COMANDO {funbiblio.upper()}...'
    print(f'\033[0;37;44m{"*"*len(mensagem)}')
    print(mensagem)
    print(f'{"*"*len(mensagem)}\033[m')
    sleep(1)
def ajuda(funbiblio):
    print(f'\033[4;33;40m')
    help(funbiblio)
    


boasVindas()
while True:
    usuario = entrada()
    if usuario == 'FIM':
        sleep(1)
        encerra(usuario)
        break
    acesso(usuario)
    ajuda(usuario)
    