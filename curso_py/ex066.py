def area(l,c):
    return largura * comprimento
def caixa(mensagem):
    print('-'*len(mensagem))
    print(mensagem)
    print('-'*len(mensagem))


caixa('CONTROLE DE TERRENOS')
largura = int(input('Largura (m): '))
comprimento = int(input('Comprimento (m): '))
caixa(f'A área do terreno de {largura} x {comprimento} é {area(largura,comprimento)} m²')
