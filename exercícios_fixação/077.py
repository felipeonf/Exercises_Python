'''Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No
final, mostre uma listagem com todos os nomes informados, na ordem inversa
daquela em que eles foram informados.'''
nomes = []
for pessoa in range(1,8):
    nomes.append(input('Digite o seu nome: '))
print(nomes[::-1])
