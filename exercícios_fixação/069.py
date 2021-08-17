''' [DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma
PA (Progressão Aritmética), mostrando na tela os 10 primeiros elementos da PA e
a soma entre todos os valores da sequência.'''
primeirotermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = primeirotermo
for elemento in range(1,11):
    if elemento == 1:
        print(contador,end=' > ')
    else:
        contador += razao
        if elemento < 10:
            print(contador,end =' > ')
        else:
            print(contador)
