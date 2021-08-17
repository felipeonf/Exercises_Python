import random
def gerador(tamanhostring):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    resultado = ''
    for i in range(tamanhostring):
        resultado += alfabeto[random.randrange(27)]
    return resultado


def pontuacao(pretendido,stringteste):
    letras_iguais = 0
    for i in range(len(pretendido)):
        if pretendido[i] == stringteste[i]:
            letras_iguais += 1
    return letras_iguais / len(pretendido)


def main():
    string_pretendida = 'methinks it is like a weasel'
    nova_string = gerador(28)
    melhor = 0
    nova_pontuacao = pontuacao(string_pretendida,nova_string)
    while nova_pontuacao < 1:
        if nova_pontuacao > melhor:
            print(nova_string)
            melhor = nova_pontuacao
        nova_string = gerador (28)
        nova_pontuacao = pontuacao(string_pretendida,nova_string)
main()
    